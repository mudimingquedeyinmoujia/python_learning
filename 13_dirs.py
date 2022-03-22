import os,sys

# basedir='./13_dirs/mydir/'
# expname='results'
# os.makedirs(os.path.join(basedir,expname),exist_ok=False)

# path='E:/Gits/my_forks/face3d/idea/300W-LP/300W_LP/AFW/AFW_134212_1_0.jpg'
# a=path.split('/')[-1].split('.')[0]
# print(a)

import time
now = time.localtime()
nowt = time.strftime("%Y-%m-%d-%H_%M_%S_", now)  #这一步就是对时间进行格式化
print(nowt)

