a=10201
print(str(a))

# 前面带着r的字符串是原始字符串，无转义字符之说
str1="abc\nef"
str2=r"abc\nef"
print(str1)
print(str2)

# 关于格式化字符串，使用{}与format
# 关于format的用法，里面可以接收不同的参数，string,*args,**kwargs,传入list就在前面加上*,传入dict就在前面加上**,
# 这样就可以随心所欲使用位置值或者key值来格式化了
print("format 的用法如下")
dic1={"name":"xixi","number":123}
list1=[1,2,3,4,5,6]
print("the normal use is {} {}".format("hello","xixi"))
print("the name is {name} and the number is {number}".format(**dic1))
print("the list is {0}{1}{3}{2}{4}".format(*list1))
print("the list is {0[0]}{0[1]}{0[3]}{0[2]}{0[4]}".format(list1))

# 关于format的对象的用法，注意使用0这个位置值代替对象
print("format 的对象用法如下")
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))
