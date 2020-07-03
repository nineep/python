# -*- coding: utf-8 -*-
# import requests
#
# session = requests.Session()
#
# i1 = session.get(url='http:')
#
# i2 = session.post(
#     url = 'http://'
#     data = {
#         'phone': 'dddddd',
#         'passwd': 'sjdksjkd',
#         'oneMonth': '1'
#     }
# )
#
# i3 = session.post(
#     url='',
# )
#
# print(i3.text)
#
# requests.post()
# url
# data
# json
# params
# cookies
# headers
# files
# stream
# auth
# allow_redirects
# timeout
# verity
# cert
# proxies
# requests.post()
# session

from bs4 import BeautifulSoup

soup = BeautifulSoup('聊天框.html', features='lxml')
