import requests
from requests.auth import HTTPBasicAuth
import git
from git import Repo

import re
import os


def checkout_templates_file():
    """
    因为每次执行测试会根据sdk版本修改catalog name
    所以测试之前，确认pipeline-config.conf和VolatileLayerMetadataSetup.java等文件为原始状态
    """
    repo = Repo('.')
    if repo.is_dirty():
        repo.index.checkout(force=True)
        print('checkout 工作区修改的文件...')
    else:
        print('工作区无修改的文件...')


def get_sdk_latest_version():
    maven_metadata_file_url = 'https://repo.platform.hereolp.cn/artifactory/' \
                              'open-location-platform/com/here/platform/sdk-stream-bom/maven-metadata.xml'
    username = 'here-aff57f85-96a3-4ce7-86f4-96e3c10e4e3e'
    password = 'ammm/hWeQEvdwY1BEkU3Hgf4n0BaEomylGsXGkJ2w9M='

    r = requests.get(maven_metadata_file_url, auth=HTTPBasicAuth(username, password))
    text = r.text

    maven_metadata_file_latest_line = re.findall('<latest>.*</latest>', text)[0]
    sdk_latest_version = re.findall('[0-9].*\d', maven_metadata_file_latest_line)[0]
    print('已从 here olp repo 获取 sdk latest version:', sdk_latest_version)
    return sdk_latest_version


def update_sdk_version():
    """
    修改项目pom.xml文件中sdk version
    即<stream.bom.version>2.15.2</stream.bom.version>行
    """
    pom_file_relative_path = 'examples/stream-sdii-read-write'
    pom_file_basename = 'pom.xml'
    pom_file_relative_abspath = pom_file_relative_path + '/' + pom_file_basename

    # target_line = re.findall('<stream.bom.version>.*</stream.bom.version>', pom_file_relative_abspath)[0]
    # sdk_old_version = re.findall('[0-9].*\d', target_line)[0]
    sdk_latest_version = get_sdk_latest_version()

    with open(pom_file_relative_abspath, 'r', encoding='utf-8') as f1, \
            open('%s.backup' % pom_file_relative_abspath, 'w', encoding='utf-8') as f2:
        for line in f1:
            #print(line, end='')
            target_line = re.findall('<stream.bom.version>.*</stream.bom.version>', line)
            if target_line:
                print('更新pom.xml文件目标行', target_line, '中的 sdk version 为', sdk_latest_version)
                sdk_old_version = re.findall('[0-9].*\d', target_line[0])[0]
                f2.write(re.sub(sdk_old_version, sdk_latest_version, line))
            else:
                f2.write(line)

    os.remove(pom_file_relative_abspath)
    os.rename('%s.backup' % pom_file_relative_abspath, pom_file_relative_abspath)
    print('已将SDK Version 更新为', sdk_latest_version)


def execute_test_script():
    """
    执行测试脚本
    并输出日志
    """
    pass


def write_runtime_to_excel():
    """
    测试runtime结果写入到excel表格
    """
    pass


if __name__ == '__main__':
    update_sdk_version()
