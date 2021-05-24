#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 错误日志
ERROR_LOG_FILE = os.path.join(BASEDIR, 'log', 'error.log')
# 运行日志
RUN_LOG_FILE = os.path.join(BASEDIR, 'log', 'run.log')

# 用于API认证的key
KEY = '299095cc-1330-11e5-b06a-a45e60bec08b'
# 用于API认证的请求头
AUTH_KEY_NAME = 'auth-key'

# Agent 模式保存服务器唯一ID的文件
CERT_FILE_PATH = os.path.join(BASEDIR, 'config', 'cert')

# 是否测试模式，测试模式时候从files目录下读取
TEST_MODE = True

# 采集方式，agent，salt，ssh
MODE = 'agent'

# SSH方式，配置SSH key，user
SSH_PRIVATE_KEY = '/home/auto/.ssh/id_rsa'
SSH_USER = 'root'
SSH_PORT = 22

# 采集硬件数据的插件
PLUGINGS_DICT = {
    'cpu': 'src.plugins.cpu.CpuPlugin',
    'disk': 'src.plugins.disk.DiskPlugin',
    'main_board': 'src.plugins.main_board.MainBoardPlugin',
    'memory': 'src.plugins.memory.MemoryPlugin',
    'nic': 'src.plugins.nic.NicPlugin',
}


# 资产信息API
ASSET_API = 'http://127.0.0.1:8000/api/asset'

"""
POST时， 返回值：{'code': xx, 'message': 'xx'}
    code:
        1000 成功
        1001 接口授权失败
        1002 数据库中资产不存在
"""