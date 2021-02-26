import argparse
import ast
# 注意各种参数一定在 .py 文件之后
# python 11_argparse.py -nu 121 -nn 12121 -a 121
parser=argparse.ArgumentParser(description="this is my parser")
parser.add_argument('-nu','--number',default=10,type=int,help="this is the number you need to input")
parser.add_argument('-nn','--name',default=13,type=int,help="this is the name you need to input")
parser.add_argument('-a','--age',default=15,type=int,help="this is the age you need to input")
parser.add_argument('-s','--score',default=16,type=int,help="this is the score you need to input")
conf=parser.parse_args()
print(type(conf))
print(conf)
print("the conf is {} {} {} {}".format(conf.number,conf.name,conf.age,conf.score))


# 这里是尽量进行类型转换，可以用在上面的type=ast.literal,比如类型是bool类型
a_str='[1,2,3,4,5]'
a_list=ast.literal_eval(a_str)
print(type(a_list),a_list)