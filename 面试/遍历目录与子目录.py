#遍历目录，找到指定suffix的文件

#使用os.walk
import os
def get_files(dir, suffix):
    res = []
    for root, dirs, files in os.walk(dir):
        for filename in files:
            name,suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root, filename))
    return res

get_files('./', '.py')


#使用递归
import os
def pick(obj, suffix):
    if obj.endswith(suffix):
        print(obj)

def scan_path(ph,suffix):
    file_list = os.listdir(ph)
    for obj in file_list:
        if os.path.isfile(obj):
            pick(obj, suffix=suffix)
        elif os.path.isdir(obj):
            scan_path(obj)
scan_path('./', '.py')


#使用glob
from glob import iglob
def func(fp, postfix):
    for i in iglob(f'{fp}/**/*{postfix}', recursive=True):
        print(i)

func('./', '.py')
