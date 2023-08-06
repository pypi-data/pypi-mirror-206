import os
import asyncio
import re
import time
import builtins
from concurrent.futures import ThreadPoolExecutor
import requests
import json
from bs4 import BeautifulSoup

import maya.standalone
from _path import DOMAIN_PATH, LOGIN_URL, SEND_DATA_TO_URL
from CMClass import CMApplication, CMFileOptions, CMSceneCounter, CMSceneEvaluate, CMFileProperty
from CMClass.custom_transform import CMTransform, CMTransforms

from tools.custom_svn import *

maya.standalone.initialize(name='python')


class CustomPath():
    def __init__(self, version, description, path, local_checkout_path):
        self.version = version
        self.description = description
        self.path = path
        self.local_path = os.path.normpath(os.path.normpath(local_checkout_path) + os.path.normpath(self.path[6:]))

    def get_data(self):
        return {
            'scene_version': self.version,
            'scene_version_description': self.description,
            'path': self.path,
            'local_path': self.local_path
        }


class SceneVersionData():
    def __init__(self):
        pass


class Client():
    def __init__(self, email, password, data={}):
        self.email = email
        self.password = password
        session = self.login(self.email, self.password)
        self.send_data_to_server(data, session)

    def login(self, email, password):
        session = requests.Session()
        login_page = session.get(LOGIN_URL)
        soup = BeautifulSoup(login_page.text, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
        # 发送登录请求
        login_data = {
            'email': email,
            'password': password,
            'csrfmiddlewaretoken': csrf_token,
        }
        login_response = session.post(LOGIN_URL, data=login_data)

        # 检查登录是否成功
        if login_response.status_code == 200:
            print('Login successful')
        else:
            print('Login failed')
        return session

    def send_data_to_server(self, data, session):
        target_page = session.get(SEND_DATA_TO_URL)
        soup = BeautifulSoup(target_page.text, 'html.parser')
        csrf_token = session.cookies.get('csrftoken')

        # 需要提交的数据
        post_data = {
            'csrfmiddlewaretoken': csrf_token,
            'scene_data': json.dumps(data),
        }
        # 发送POST请求
        response = session.post(SEND_DATA_TO_URL, data=post_data)

        # 处理响应内容
        print(response.text)

    def get_overview_data(self):
        pass

    def get_file_details_data(self):
        pass

    def get_version_data(self):
        pass


class CustomClientData():
    def __init__(self):
        self.scene_evaluate = SceneEvaluateData()
        self.scene_details = SceneDetailsData()
        self.scene_file_details = SceneFileDetailsData()
        self.scene_version = SceneVersionData()

    def get_data(self):
        return {
            **{}
        }


class SceneEvaluateData():
    def __init__(self):
        self.scene_counter = SceneCounterData()
        self.scene_settings = SceneSettingsData()


class SceneDetailsData():
    def __init__(self):
        pass


class SceneFileDetailsData():
    def __init__(self, file_path):
        self.file_evaluate = CMFileProperty(file_path).get_file_evaluate()
        self.file_path = file_path

    def get_data(self):
        return {
            'full_path': self.file_path,
            'FileSize': self.file_evaluate.get('Size'),
            'FileSuffix': self.file_evaluate.get('Suffix'),
            'IsPathAscii': self.file_evaluate.get('IsPathAscii'),
            'FirstLetterIsNumber': self.file_evaluate.get('FirstLetterIsNumber'),
            'IsExisted': True,
        }


class SceneSettingsData():
    def __init__(self):
        self.custom_scene_evaluate = CMSceneEvaluate()

    def get_data(self):
        settings = self.custom_scene_evaluate.get_settings_evaluate()
        return {
            'up_axis': settings.get('Up axis'),
            'linear': settings.get('Linear'),
            'angular': settings.get('Angular'),
            'start_frame': settings.get('AnimStartTime'),
            'end_frame': settings.get('AnimEndTime'),
            'current_frame': settings.get('CurrentTime'),
            'playback_start_frame': settings.get('PlaybackStartTime'),
            'playback_end_frame': settings.get('PlaybackEndTime'),
            'fps': settings.get('Framerate'),
        }


class SceneCounterData():
    def __init__(self):
        pass

    def get_data(self):
        # 1. get scene counter
        counter = CMSceneCounter()
        all_counts = counter.get_scene_counter()
        return {
            'Transforms': all_counts.get('Transforms'),
            'Groups': all_counts.get('Groups'),
            'Empty Groups': all_counts.get('EmptyGroups'),
            'Polygons': all_counts.get('Meshes'),
            'Materials': all_counts.get('Materials'),
            'Textures': all_counts.get('Textures'),
            'Cameras': all_counts.get('Cameras'),
            'Joints': all_counts.get('Joints'),
            'Lights': all_counts.get('Lights'),
            'Blend Shapes': all_counts.get('BlendShapes'),
            'Morph Targets': all_counts.get('MorphTargets'),
            'Verts': all_counts.get('Verts'),
            'Edges': all_counts.get('Edges'),
            'Faces': all_counts.get('Faces'),
            'Tris': all_counts.get('Tris'),
            'UVs': all_counts.get('UVs'),
            'N Polygons': all_counts.get('Ngons'),
            'Root Nodes': all_counts.get('RootNodes'),
        }


def send_data(custom_path: CustomPath):
    """
    Asynchronously read a Maya file using the cmds module
    :param sd_obj:
    :param file_path: Maya文件的路径
    :return:
    """
    # Maya path
    file_path = custom_path.local_path

    app = CMApplication(standalone_mode=False)
    op = CMFileOptions()
    op.set_open_file_options(file_path, force=True, open=True)
    app.open_file(op)

    scene_data = {
        "scene_evaluate": {
            "scene_counter": SceneCounterData().get_data(),
            'SceneSettings': SceneSettingsData().get_data(),
        },
        'scene_version': custom_path.get_data(),
        "scene_file_details": SceneFileDetailsData(file_path).get_data(),  # {
        "scene_details": {
            # 'BlendShapes': [
            #     {
            #         'name': 'blendShape1',
            #         'num_targets': 2,
            #         'weight': 0.51,
            #         'MorphTargets': [
            #             {'name': 'morphTarget11212121212212121212121213213123123123', 'weight': 0.5},
            #         ],
            #     },
            #     {
            #         'name': 'blendShape2',
            #         'num_targets': 3,
            #         'weight': 0.52,
            #         'MorphTargets': [
            #             *[{'name': f'mtttttttttttaatttttttttt2_{i}', 'weight': 0.5} for i in range(10)],
            #         ]
            #     },
            # ],
            'Transforms': CMTransforms().get_send_data(),

        }
    }

    c = Client('g-qiao@spik-chunsoft.co.jp', 'Kadykady3', data=scene_data)  # TODO:Set email and password

    print(f"Successfully read file: {file_path}")


async def read_file(custom_path: CustomPath):
    """
    Asynchronously read a Maya file using the cmds module
    """
    # open the Maya file using cmds.file
    send_data(custom_path)
    print(f"Successfully read file: {custom_path}")


async def main(file_paths: list[CustomPath]):
    """
    Asynchronously read multiple Maya files
    """
    # create a list of tasks
    tasks = [asyncio.create_task(read_file(file_path)) for file_path in file_paths]
    # wait for all tasks to complete
    await asyncio.gather(*tasks)
    print("Finished reading all files")


if __name__ == '__main__':
    root_local_repo_path = r'C:\Proj\Korat\SS-Data'  # TODO:Set local repo dir path
    match_root_dir = os.path.normpath(os.path.join(root_local_repo_path, 'Character'))
    svn_xml = SVNXml(local_repo_path=root_local_repo_path, limit_revision=1000)
    count_version = 0
    for version in reversed(svn_xml.get_revisions()):
        files = version.files
        file_list = []
        for file in files.get_files():

            cv = CustomPath(version.revision, version.msg, file.path, root_local_repo_path)
            match_basename = re.match(r'.*\d{4}_\d{2}_\d{2}', cv.local_path)

            if cv.local_path.endswith(('.mb', '.ma')) and match_basename and os.path.normpath(cv.local_path).startswith(
                    match_root_dir):
                file_list.append(cv)

        if len(file_list) > 0:
            print(f'更新中:{version.revision}')
            version.update_svn(match_root_dir)
            print(f'更新了:{version.revision}')


            # 批处理
            asyncio.run(main(file_list))
