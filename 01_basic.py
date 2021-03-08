# coding=utf-8
print("你好")
# 防止中文编码错误，加上上面的内容即可

# 使用逗号来将不同内容输出在同一行
a=10
b=20
print(a,b,a,b,a)

# print的比较有意思用法如下 end=''意思是传入的是空字符串，末尾替换换行符号
import math
print("hello nihao",end='')
print("hello zaijian")

# 输出黑色与白色方块字符
print(chr(9632),end='')
print(chr(9633))

def print_rate(nums=20,rate=0):
    black_num=math.floor(nums*rate)
    white_num=nums-black_num
    print('|',end='')
    for i in range(black_num):
        print(chr(9632),end='')
    for i in range(white_num):
        print(chr(9633),end='')
    print(" {:>6.2f}% ".format(100*rate),end='')
    print('|',end='')

# 下面开始
sum=0
for i in range(10000):
    for j in range(100000):
        sum+=j
        sum-=j
        sum+=j
        sum-=j
    print('\r',end='')
    print_rate(rate=i/10000)
