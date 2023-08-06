import asyncio
import os
from jinja2 import Environment, FileSystemLoader, PackageLoader

import maya.cmds as cmds
import custom_maya


class BatchSceneFunction():
    def __init__(self):
        pass

    def function(self):
        pass


def get_template_env(package_name='custom_maya', template_path='templates'):
    file_loader = PackageLoader(package_name, template_path)
    # 创建一个Jinja2环境
    env = Environment(loader=file_loader)
    return env


def get_file_path_list(root_dir):
    res = []
    suffix_list = ['.mb', '.ma']

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            short_file_name, suffix = os.path.splitext(os.path.basename(file))
            full_path = os.path.join(root, file)
            if suffix in suffix_list:
                res.append(full_path)
    return res


class SceneIndex():
    pass


class SceneDetails():
    pass


import custom_maya

cmop = custom_maya.CMFileOptions()
cmop.set_open_file_options(r'D:/test_scenes/test_joints.mb', open=True, force=True, ignoreVersion=True)

cma = custom_maya.CMApplication()
cma.open_file(cmop)

cm_scene = custom_maya.CMScene()

for i in cm_scene.property_list:
    print('------------------')
    print(i)
    print(i, getattr(cm_scene, i)())

cmse = custom_maya.CMSceneEvaluate()
cmse.get_scene_evaluate()
# for k,v in cmse.get_scene_evaluate().items():
#     print(k, v)
#
# for k,v in cmse.get_scene_counter().items():
#     print(k, v)

data = {
    'Counter': cmse.get_scene_counter(),
}

dir_name = os.path.dirname(cmds.file(q=True, sn=True))
base_name, suffix = os.path.splitext(os.path.basename(cmds.file(q=True, sn=True)))
absolute_path = os.path.join(dir_name, f'{base_name}.html')

env = get_template_env()
template = env.get_template('query_scene/per_scene/per_scene.html')
output = template.render(data)
with open(absolute_path, 'w', encoding='utf-8') as f:
    f.write(output)

os.startfile(absolute_path)
