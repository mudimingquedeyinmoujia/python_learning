# sys.path 包含了所有的模块搜索路径
# import xxx 这里导入的一定是模块的名字，也就是.py文件,要使用里面的函数得xxx.function才行而不能直接使用函数
# 如果要直接使用函数,from xxx import * 这样就可以直接使用函数了,就不用再xxx.function了
# 如果 xxx 在某个文件夹里,要使用yyy.xxx来导入

#### test 01
# import sys
# print(sys.path)
# import mymoudle_08.util_01 as util
# util.util_01_fun1()
#
# print(__name__) # 返回文件的名称,如果正在运行就是__main__如果作为模块被导入的话就是xxx.xxx模块
# print(__file__) # 返回文件的绝对路径

### test 02
# import mymoudle_08.util_02 as ut2
# print(dir(ut2)) # dir函数专门用来查看模块里面定义的各种函数名与内置变量名

### test 03
# 关于模块文件夹下__init__.py文件的作用
# 一般来说在__init__.py里面加上from xxx import * 这样就可以直接用文件夹名字当做模块的名字了,但是这样子区分度不会很高
# 所以如果在__init__.py里面加上import xxx as yyy 这样就可以在程序正文将文件夹正式看做一个模块了(也就是.py文件)
# import mymoudle_08
# mymoudle_08.util_02_fun1()
# mymoudle_08.ut3.util_03_fun1()

### test 04
# 不加sys.append会报错
# import sys
# sys.path.append("./mymoudle_08")
# import util_01
# util_01.util_01_fun1()
