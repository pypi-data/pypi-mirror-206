import os
import time
import xml.etree.ElementTree
import xml.etree.ElementTree as ET

import subprocess


# tree = ET.parse(r'svn_log_output.xml')
# root = tree.getroot()


class SVNBase():
    #
    xml_dir = os.path.join(os.path.expanduser('~'), 'custom-maya', 'xml')

    def __init__(self):
        pass

    def create_xml_folders(self):
        print('正在创建xml文件夹')
        print(self.xml_dir)
        if not os.path.exists(self.xml_dir):
            os.makedirs(self.xml_dir)
            print('已经创建xml文件夹')

    @property
    def update_character_reference(self):
        '''
        记录svn update中的更新状态参照
        :return:
        '''
        return {
            'A': 'Added',
            'D': 'Deleted',
            'U': 'Updated',
            'C': 'Conflict',
            'G': 'Merged',
            'E': 'Existed',
            'R': 'Replaced',
        }


class SVNRevision(SVNBase):
    def __init__(self, revision: xml.etree.ElementTree.Element, local_repo_path=None):
        super().__init__()
        self.__revision = revision
        self.revision: str = revision.attrib.get('revision') if revision.tag == 'logentry' else None
        self.author: str = revision.find('author').text
        self.date: str = revision.find('date').text
        self.msg: str = revision.find('msg').text
        self.files = SVNFiles(self.__revision)
        self.local_repo_path = local_repo_path

    def get_revision(self):
        return self.__revision

    def get_data(self):
        return {
            'revision': self.revision,
            'author': self.author,
            'date': self.date,
            'msg': self.msg,
            'files': self.files.get_data()
        }

    def update_svn(self, dir):
        print(' '.join(['svn', 'update', '-r', f'{self.revision}', dir]))
        return subprocess.run(
            ['svn', 'update', '-r', f'{self.revision}', dir],
            capture_output=True,
            text=True
        ).stdout


class SVNFile():
    def __init__(self, path: xml.etree.ElementTree.Element):
        super().__init__()
        self._path = path
        self.path = path.text
        self.action = self._path.attrib.get('action')

    def get_data(self):
        return {
            'path': self.path,
            'action': self.action,
        }


class SVNFiles():
    def __init__(self, revision: xml.etree.ElementTree.Element):
        self._revision = revision
        self.__files: list[SVNFile] = []
        self.set_files()

    def set_files(self):
        for path in self._revision.find('paths'):
            self.__files.append(SVNFile(path))

    def get_files(self):
        return self.__files

    def get_data(self):
        return [i.get_data() for i in self.get_files()]


class SVNInfo(SVNBase):
    def __init__(self, info: xml.etree.ElementTree.Element):
        super().__init__()
        entry = info.find('entry')
        self.local_checkout_dir = entry.attrib.get('path')

    def get_data(self):
        return {
            'local_checkout_dir': self.local_checkout_dir
        }


class SVNXml(SVNBase):
    def __init__(self, local_repo_path: str = None, limit_revision=1, *args, **kwargs):
        self.create_xml_folders()
        super().__init__()
        self.limit_revision = limit_revision
        self.local_repo_path = local_repo_path

        self.__revisions: list[SVNRevision] = []
        self._xml: xml.etree.ElementTree.Element = self.get_svn_log_xml()
        self._info: xml.etree.ElementTree.Element = self.get_svn_info_xml()

        self.set_revisions()
        self.info = SVNInfo(self._info)

    def set_revisions(self):
        for xe in self._xml:
            self.__revisions.append(SVNRevision(xe, local_repo_path=self.local_repo_path))

    def get_revisions(self) -> list[SVNRevision]:
        return self.__revisions

    def get_svn_log_xml(self):
        svn_xml_path = os.path.join(self.xml_dir, 'svn_log_xml.xml')
        if self.limit_revision != 0:
            limit_cmd = f'-l {self.limit_revision}'
        else:
            limit_cmd = ''
        command = f'svn log "{self.local_repo_path}" -v {limit_cmd} --xml > {svn_xml_path}'
        print(command)
        subprocess.run(command, shell=True, text=True)

        tree = ET.parse(svn_xml_path)
        return tree.getroot()

    def get_svn_info_xml(self):
        svn_info_xml_path = os.path.join(self.xml_dir, 'svn_info_xml.xml')
        cmd = f'svn info {self.local_repo_path} --xml > {svn_info_xml_path}'
        subprocess.run(cmd, shell=True, text=True)

        tree = ET.parse(svn_info_xml_path)
        return tree.getroot()
