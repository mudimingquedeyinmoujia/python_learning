import os
# 如果split的前面部分重合,那么第一个元素是空
# 如果字符串与自己split,那么返回两个空
# 如果split的后面部分重合，那么最后一个元素是空
# 也就是说，split操作默认给字符串前后都加了空字符
str_a="whatisthis"
str_spl=str_a.split("what")
str_spl2=str_a.split(str_a)
str_spl3=str_a.split("this")
print(str_spl)
print(str_spl2)
print(str_spl3)

# 遍历指定路径下的所有文件夹与文件，以及所有文件夹内的文件，默认从外向内,从上至下深度优先
# 注意root只可能是文件夹,不可能是文件
inputdir="E:\AboutGit\pythontest\python_learning"
for root,dirs,files in os.walk(inputdir,topdown=True):
    print(root,dirs,files)
    print("--------")
    for i in root.split(inputdir):
        print(i)