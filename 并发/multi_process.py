from concurrent.futures import ThreadPoolExecutor
import requests
import time

def task(url):
    response = requests.get(url)
    print(url, response)
    # time.sleep(1)

pool = ThreadPoolExecutor(7)
url_list = [
    'https://www.baidu.com',
    'https://www.qq.com',
    'https://www.sina.com',
    'https://www.bing.com',
    'https://www.cnblogs.com',
    'https://www.zhihu.com',
    'https://www.douban.com',
]

for url in url_list:
    pool.submit(task, url)

pool.shutdown(wait=True)