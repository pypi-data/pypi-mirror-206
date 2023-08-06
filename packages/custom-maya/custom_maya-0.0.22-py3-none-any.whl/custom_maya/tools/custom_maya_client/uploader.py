import requests
import json
from bs4 import BeautifulSoup
from _path import DOMAIN_PATH, LOGIN_URL, SEND_DATA_TO_URL
from CMClass import CMApplication, CMFileOptions, CMSceneCounter, CMSceneEvaluate, CMFileProperty

from CMClass.custom_transform import CMTransform, CMTransforms

file_path = r'D:\test_scenes\0000_00_ff.mb'
# file_path = r'D:\test_scenes\reference_scene.mb'


class Client():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        session = self.login(self.email, self.password)
        self.send_data_to_server(scene_data, session)

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

    def get_data(self):
        return {
            'full_path': self.file_evaluate.get('FullPath'),
            'FileSize': self.file_evaluate.get('Size'),
            'FileSuffix': self.file_evaluate.get('Suffix'),
            'IsPathAscii': self.file_evaluate.get('IsPathAscii'),
            'FirstLetterIsNumber': self.file_evaluate.get('FirstLetterIsNumber'),
            'IsExisted': True,
        }


class SceneVersionData():
    def __init__(self):
        pass

    def get_data(self):
        return {
            "scene_version": "7.15",
            "scene_version_description": '''7.15
            设计哲学

如果你有编程背景，或者你习惯于将编程代码直接混入 HTML 的语言，你要记住，Django 模板系统并不是简单的将 Python 嵌入到 HTML 中。这是设计上的：模板系统是为了表达表现形式，而不是程序逻辑。

Django 模板系统提供了类似于一些编程结构的标签——布尔测试的 if 标签，循环的 for 标签等等。——但这些并不是简单地作为相应的 Python 代码来执行，模板系统不会执行任意的 Python 表达式。默认情况下只支持下面列出的标签、过滤器和语法（尽管你可以根据需要在模板语言中添加 你自己的扩展）。
            ''',
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


app = CMApplication()
op = CMFileOptions()
op.set_open_file_options(file_path, force=True, open=True)
app.open_file(op)

scene_data = {
    "scene_evaluate": {
        "scene_counter": SceneCounterData().get_data(),
        'SceneSettings': SceneSettingsData().get_data(),
    },
    'scene_version': SceneVersionData().get_data(),
    "scene_file_details": SceneFileDetailsData(file_path).get_data(),  # {
    "scene_details": {
        'BlendShapes': [
            {
                'name': 'blendShape1',
                'num_targets': 2,
                'weight': 0.51,
                'MorphTargets': [
                    {'name': 'morphTarget11212121212212121212121213213123123123', 'weight': 0.5},
                ],
            },
            {
                'name': 'blendShape2',
                'num_targets': 3,
                'weight': 0.52,
                'MorphTargets': [
                    *[{'name': f'mtttttttttttaatttttttttt2_{i}', 'weight': 0.5} for i in range(10)],
                ]
            },
        ],

        'Transforms': CMTransforms().get_send_data(),

    }
}

c = Client('narutozb@hotmail.com', 'Kadykady3')
