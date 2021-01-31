# 在循环里的变量是并不是局部变量
num_out=12
for i in range(10):
    num_out=i
    num_in=14

print(num_out)
print(num_in)

# 关于函数与变量
# 如果是在函数里面，对于普通变量来说定义的变量是局部变量
# 如果想要让普通变量成为全局变量，前面加上global声明
# 但是在函数里面使用的list和dict却是全局变量
print("about function and variables")
num_glo=13
list_glo=[1,2,3]
dict_glo={}
dict_glo["name"]=1
def funadd(arg1=12,arg2=15):
    global num_glo
    num_glo=arg1+arg2
    list_glo.append([arg1,arg2])
    dict_glo["age"]=arg1
    dict_glo["time"]=arg2
    print("inside fucntion")
    print(num_glo)
    print(list_glo)
    print(dict_glo)

funadd()
print("outside the function")
print(num_glo)
print(list_glo)
print(dict_glo)