from typing import TypeVar, Generic

import maya.cmds as cmds

from .base import CMObject, CMNode
from CMClass import CMDetailPropertyManager, CMDetailProperty


class CMTransform(CMNode):
    def __init__(self, short_name):
        self.short_name = short_name
        self.long_name = cmds.ls(short_name, long=True)[0]

        self.translation_x = cmds.getAttr(f"{self.long_name}.translateX")
        self.translation_y = cmds.getAttr(f"{self.long_name}.translateY")
        self.translation_z = cmds.getAttr(f"{self.long_name}.translateZ")
        self.rotation_x = cmds.getAttr(f"{self.long_name}.rotateX")
        self.rotation_y = cmds.getAttr(f"{self.long_name}.rotateY")
        self.rotation_z = cmds.getAttr(f"{self.long_name}.rotateZ")
        self.scale_x = cmds.getAttr(f"{self.long_name}.scaleX")
        self.scale_y = cmds.getAttr(f"{self.long_name}.scaleY")
        self.scale_z = cmds.getAttr(f"{self.long_name}.scaleZ")
        self.visibility = cmds.getAttr(f"{self.long_name}.visibility")

        self.properties = CMDetailPropertyManager()
        self.properties.add_members([
            CMDetailProperty(display_name='translation_x', value=self.translation_x),
            CMDetailProperty(display_name='translation_y', value=self.translation_y),
            CMDetailProperty(display_name='translation_z', value=self.translation_z),
            CMDetailProperty(display_name='rotation_x', value=self.rotation_x),
            CMDetailProperty(display_name='rotation_y', value=self.rotation_y),
            CMDetailProperty(display_name='rotation_z', value=self.rotation_z),
            CMDetailProperty(display_name='scale_x', value=self.scale_x),
            CMDetailProperty(display_name='scale_y', value=self.scale_y),
            CMDetailProperty(display_name='scale_z', value=self.scale_z),
            CMDetailProperty(display_name='visibility', value=self.visibility),
        ])

    class CMTransforms():
        def __init__(self):
            pass

        def get_custom_transforms(self):
            return [CMTransform(i) for i in cmds.ls(type="transform")]
