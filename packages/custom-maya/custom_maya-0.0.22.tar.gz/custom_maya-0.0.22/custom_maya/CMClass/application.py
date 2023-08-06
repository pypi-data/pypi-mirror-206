import os.path

import maya.cmds as cmds
import maya.OpenMaya as om

from .base import CMNode
from .property import CMStandaloneProperty, CMFileOptions, CMObjectsInSceneProperty
from .functions import convert_unit_to_fps


class CMApplication(CMNode, CMStandaloneProperty):
    '''maya应用'''

    def __init__(self, standalone_mode=True):
        super().__init__()

        if self.is_standalone() and standalone_mode:
            '''当maya以独立模式运行时，需要初始化maya'''
            print("启动maya独立模式")
            import maya.standalone
            maya.standalone.initialize(name='python')

    def open_file(self, options: CMFileOptions):
        cmds.file(*options.get_open_file_options()[0], **options.get_open_file_options()[1])

    def save_file(self, options: CMFileOptions):
        cmds.file(*options.get_save_file_options()[0], **options.get_save_file_options()[1])


class CMScene(CMNode, CMStandaloneProperty, CMObjectsInSceneProperty):
    def __init__(self):
        super().__init__()


class CustomSceneFunction(CMNode):
    def __init__(self):
        super().__init__()

    def has_same_name_transform(self):
        for i in cmds.ls(type='transform'):
            if '|' in i:
                return True
        return False

    def has_duplicate_named_object(self, typ):
        for i in cmds.ls(type=typ):
            if '|' in i:
                return True
        return False

    def has_same_name_joint(self):
        for i in cmds.ls(type='joint'):
            if '|' in i:
                return True
        return False

    def get_objects_with_more_than_4_sides_long_list(self):
        cmds.select(cmds.ls(type='mesh'))
        sel = om.MSelectionList()
        om.MGlobal.getActiveSelectionList(sel)
        poly_objects = []
        for i in range(sel.length()):
            m_obj = om.MObject()
            sel.getDependNode(i, m_obj)
            if m_obj.hasFn(om.MFn.kMesh):
                dag_path = om.MDagPath()
                sel.getDagPath(i, dag_path)
                poly = om.MFnMesh(dag_path)
                for j in range(poly.numPolygons()):
                    vertices = om.MIntArray()
                    poly.getPolygonVertices(j, vertices)
                    if len(vertices) > 4:
                        poly_objects.append(dag_path.fullPathName())
                        break
        cmds.select(cl=True)
        return poly_objects

    def get_root_nodes(self):
        root_nodes = cmds.ls(assemblies=True, long=True)
        return root_nodes

    def get_custom_cameras(self):
        default_camera_list = [
            '|front',
            '|persp',
            '|side',
            '|top',
        ]
        res = []
        for i in cmds.ls(type='camera', long=True):
            camera_name_long = cmds.ls(cmds.listRelatives(i, parent=True), long=True)[0]
            if camera_name_long not in default_camera_list:
                res.append(camera_name_long)
        return res

    def get_empty_groups(self):
        '''
        获取空组
        '''
        empty_groups = []
        for i in cmds.ls(type='transform', long=True):
            children = cmds.listRelatives(i, shapes=False, fullPath=True)
            if not children and cmds.nodeType(i) == 'transform':
                cmds.select(i, add=True)
        return empty_groups

    def get_groups(self):
        '''
        获取组
        '''
        groups = []
        for i in cmds.ls(type='transform', long=True):
            children = cmds.listRelatives(i, children=True, shapes=True, fullPath=True)
            if not children and cmds.nodeType(i) == 'transform':
                groups.append(i)
        return groups

    def get_light_types(self):
        dag = True
        if dag:
            return list(
                set(cmds.nodeType("shape", derived=True, isTypeName=True)).intersection(cmds.listNodeTypes("light")))
        else:
            return cmds.listNodeTypes("light")


class CMSceneEvaluate(CMScene, CustomSceneFunction):
    def __init__(self):
        super().__init__()

    def get_scene_evaluate(self):
        return {
            'full_path': cmds.file(q=True, sn=True),
            'scene_version': '1.0',
            'scene_version_description': '此版本为第一次提交，没有任何修改。有了这个版本，就可以在后续的版本中进行修改。',
            'scene_size': '10mb',
            'scene_suffix': os.path.basename(cmds.file(q=True, sn=True)).split('.')[-1],
        }

    def get_settings_evaluate(self):
        return {
            'Up axis': cmds.upAxis(q=True, axis=True),
            'Linear': cmds.currentUnit(q=True, linear=True),
            'Angular': cmds.currentUnit(q=True, angle=True),
            'CurrentTime': cmds.currentTime(query=True),
            'AnimStartTime': cmds.playbackOptions(q=True, animationStartTime=True),
            'AnimEndTime': cmds.playbackOptions(q=True, animationEndTime=True),
            'PlaybackStartTime': cmds.playbackOptions(min=True, q=True),
            'PlaybackEndTime': cmds.playbackOptions(max=True, q=True),
            'Framerate': convert_unit_to_fps(cmds.currentUnit(q=True, time=True)),
        }

    def get_poly_evaluate(self):
        '''获取场景的多边形信息。'''
        __meshes = cmds.ls(type='mesh', long=True)
        return {
        }

    def get_camera_evaluate(self):
        '''获取场景的相机信息。'''
        return {
        }

    def get_index_evaluate(self):
        '''获取场景的索引信息。'''
        return {
            **{'CurrentPath': cmds.file(query=True, sceneName=True)},

        }

    def get_blendshape_evaluate(self):
        blend_shapes = cmds.ls(type='blendShape')
        morph_target_counter = 0
        for bs in blend_shapes:
            morph_target_counter += cmds.blendShape(bs, query=True, weightCount=True)

    def get_light_evaluate(self):
        return {
            **self.get_light_counter(),
            'LightList': cmds.ls(type='light'),
            **{f'{node_type}List': cmds.ls(type=node_type, long=True) for node_type in self.get_light_types()},
            'IsLightsUnique': not self.has_duplicate_named_object('light'),
        }

    def get_joint_evaluate(self):
        return {
            **self.get_joint_counter(),
            'JointList': cmds.ls(type='joint'),
            'SameNameJoints': self.has_same_name_joint(),
        }


class CMSceneCounter(CustomSceneFunction):
    def __init__(self):
        super().__init__()

    def get_scene_counter(self):
        return {
            **self.get_transform_counter(),
            **self.get_poly_counter(),
            **self.get_material_counter(),
            **self.get_texture_counter(),
            **self.get_camera_counter(),
            **self.get_joint_counter(),
            **self.get_light_counter(),
            **self.get_blendshape_counter(),
            **self.get_nurbs_counter(),
            'RootNodes': len(self.get_root_nodes()),

        }

    def get_transform_counter(self):
        return {
            'Transforms': len(cmds.ls(type='transform')),
            'Groups': len(self.get_groups()),
            'EmptyGroups': len(self.get_empty_groups()),
        }

    def get_poly_counter(self):
        '''获取场景的多边形信息。'''
        __meshes = cmds.ls(type='mesh', long=True)
        return {
            'Meshes': len(__meshes),
            'Verts': cmds.polyEvaluate(__meshes, vertex=True) if len(__meshes) > 0 else 0,
            'Edges': cmds.polyEvaluate(__meshes, edge=True) if len(__meshes) > 0 else 0,
            'Faces': cmds.polyEvaluate(__meshes, face=True) if len(__meshes) > 0 else 0,
            'Tris': cmds.polyEvaluate(__meshes, triangle=True) if len(__meshes) > 0 else 0,
            'UVs': cmds.polyEvaluate(__meshes, uv=True) if len(__meshes) > 0 else 0,
            'Ngons': len(self.get_objects_with_more_than_4_sides_long_list()),
        }

    def get_material_counter(self):
        '''获取场景的材质信息。'''
        return {
            'Materials': len(cmds.ls(type='shadingEngine')),
        }

    def get_texture_counter(self):
        '''获取场景的贴图信息。'''
        return {
            'Textures': len(cmds.ls(type='file')),
        }

    def get_blendshape_counter(self):
        blend_shapes = cmds.ls(type='blendShape')
        morph_target_counter = 0
        for bs in blend_shapes:
            morph_target_counter += cmds.blendShape(bs, query=True, weightCount=True)
        return {
            'BlendShapes': len(blend_shapes),
            'MorphTargets': morph_target_counter
        }

    def get_camera_counter(self):
        '''获取场景的相机信息。'''
        return {
            'Cameras': len(cmds.ls(type='camera')),
        }

    def get_joint_counter(self):
        '''获取场景的骨骼信息。'''
        return {
            'Joints': len(cmds.ls(type='joint')),
        }

    def get_light_counter(self):
        '''获取场景的灯光信息。'''
        return {
            'Lights': len(cmds.ls(type='light')),
        }

    def get_nurbs_counter(self):
        '''获取场景的Nurbs信息。'''
        return {
            'Nurbs': len(cmds.ls(type='nurbsCurve')),
        }
