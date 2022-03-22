# # 乘方
# print(2**3)
# # 取模
# print(10%3)
# # 向下取整数
# print(10//3)
# # 除法的结果默认为浮点数
# print(10/3)
# print(9/3)
# print(4/2)
# print(9./3)
#
# print("bool operator is shown below")
# print(True and True)
# print(True and False)
# print(True or False)
# print(not True)
#
# # 逻辑运算符号
# print("in and not in operator is shown below")
# print(4 in [i for i in range(10)])
# print(10 in [i for i in range(10)])
# print("xii" in "abcdefgxii")
# print("he" in "abcdefg")
#
# # 身份运算符 is
# # 如果是相同的内存，那么is运算的值为True, 如果值相等,==运算的值为True
# # 对于数字来说，相同的值引用相同的内存，对于数组来说，值相同的数组是有可能占用不同的内存的，因为是对象
# print("id operator is is shown below")
# a=12
# b=12
# c=a
# d=[1,2,3]
# e=[1,2,3]
# print(a is b)
# print(a == b)
# print(a is c)
# print(d is e)
# print(d == e)

name='10_dimpler.jpg'
print(name.split('.')[-1] == 'jpg')