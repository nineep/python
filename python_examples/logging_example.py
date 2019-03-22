#!/usr/bin/python
# -*- coding: utf-8 -*-

# 日志格式
#
# %(asctime)s
# %(filename)s
# %(pathname)s
# %(funcName)s
# %(levelname)s
# %(lineno)d
# %(module)s
# %(message)s
# %(name)s
# %(process)d
# %(processName)s
# %(thread)d
# %(threadName)s

import logging
format = logging.Formatter('%(asctime)s - %(levelname)s %(filename)s [line:%(lineno)d] %(message)s')

# 创建日志记录器
info_logger = logging.getLogger('info')
# 设置日志级别，小于INFO的日志忽略
info_logger.setLevel(logging.INFO)
# 日志记录到磁盘文件
info_file = logging.FileHandler('info.log')
# info_file.setLevel(logging.INFO)
# 设置日志格式
info_file.setFormatter(format)
info_logger.addHandler(info_file)

# 错误日志
error_logger = logging.getLogger('error')
error_logger.setLevel(logging.ERROR)
error_file = logging.FileHandler('error.log')
error_file.setFormatter(format)
error_logger.addHandler(error_file)

# 输出控制台 stdout
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(format)
info_logger.addHandler(console)
error_logger.addHandler(console)

if __name__ == "__main__":
    # 写日志
    info_logger.warning("info message.")
    error_logger.error("error message!")
