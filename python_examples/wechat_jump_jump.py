#!/usr/bin/env python

import os
import math
#这两个库用于图片的操作
import matplotlib.pylot as plt
from PIL import import Image

class WechatJump:
    def __init__(self):
        #按压系数，不同分辨率手机需要做调整
        self._coefficient = 1.35
        #记录按压次数
        selp._clicl_count = 0
        #记录点击点坐标的数组
        self._coords = []

def generate_screenshot(self):
    #截图，并将图片保存为/sdcard/screenshot.png
    os.system('adb shell screencap -p /sdcard/screenshot.png')
    #pull 命令将图片从手机发送到电脑本地
    os.system('adb pull /sdcard/screenshot.png .')

def on_click(self, event):
    # event.xdata, event.ydata 分别是点击的横纵坐标，将坐标依次保存到_coords数组中
    self._coords.append((event.xdata, event.ydata))
    # 这里是每两次点击（起始点和目标点） 就会执行按压 按压屏幕操作，所以当
    # self._click_count ==2 时才执行
    self._click_count += 1
    if self._click_count ==2:
        self._click_count =0
        # 弹出第二次点击时的坐标
        _next = self._coords.pop()
        # 弹出第一次点击时的坐标
        _prev = self._coords.pop()
        # 根据勾股定理计算两点之间的距离
        self.jump_to_next(math.sqrt((_next[0] - _prev[0]) * 2 + (_next[1] - _prev[1]) * 2)

def jump_to_next

