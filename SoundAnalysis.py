# -*- coding: utf-8 -*-
import wave
import struct
from pylab import *
import os





def traverse(path):
    global num
    global threshold
    files = os.listdir(path)
    for file in files:  # 遍历文件夹
        if not os.path.isdir(os.path.join(path, file)):  # 判断是否是文件夹，不是文件夹才打开
            filter_file = file.split('.')
            if filter_file[1] != 'wav':
                continue
            wavefile = wave.open(path+"/"+file, 'r')  # open for writing
            # 读取wav文件的四种信息的函数。期中numframes表示一共读取了几个frames，在后面要用到。
            numframes = wavefile.getnframes()
            y = zeros(numframes)
            maxAmp = 0
            for i in range(numframes):
                val = wavefile.readframes(1)
                left = val[0:2]
                # right = val[2:4]
                v = struct.unpack('h', left)[0]
                y[i] = v

            if abs(max(y)) < int(threshold):  # 设置一个阈值
                print(os.path.join(path, file))
                num = num + 1
        else:
            traverse(os.path.join(path, file))


# path = "/Users/hongbowang/Downloads/250ms"  # 文件夹目录
threshold = raw_input("Please input threshold value(usually 200~300):")
path = raw_input("Please input the full path of target dir:")
num = 0
try:
    traverse(path)
    print("Found " + str(num) + " suspicious file(s)")
except OSError:
        print("Wrong file or file path")


