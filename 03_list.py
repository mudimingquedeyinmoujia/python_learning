# 下面开始反转list,使用脚标反转不会改变内存的值，使用reverse()会改变原先的值
# 当列表使用脚标运算符的时候，必须要保证冒号:的左边小于右边,即使是负数脚标
# list_a=["a","b","c","d","e","f","g"]
# list_b=[i+1 for i in range(10)]
# print(list_a)
# print(list_b)
# list_a+=list_b
# print(list_a)
# list_a.append(1)
# print(list_a)
# list_a_reverse=list_a[-1::-1]
# print("list a is ",list_a)
# list_a_reverse_false=list_a[-3:-1]
# print(list_a_reverse)
# print(list_a_reverse_false)
#
# # step list_b
# list_b_step=list_b[1:8:3]
# print(list_b_step)
#
# # copy twice of list_a and reverse
# list_a_copy=(list_a*2)[-1::-1]
# print(list_a_copy)
#
# # add and delete list and check length
# list_c_pre=["a","b","c"]
# list_c_pre.append("abc")
# print(list_c_pre)
# del list_c_pre[0]
# print(list_c_pre)
# print(len(list_c_pre))
# list_c_pre.reverse()
# print(list_c_pre)
#
# # 追加多个元素
# list_d=["li","zhang","wang"]
# list_d.extend(list_c_pre)
# print(list_d)

# 0和1作为脚标第三个

# list_c=list_a[1:5:0]#非法！！！非法
# list_d=list_a[1:5:1]
# list_e=list_a[1:5:2]
# # print(list_c)
# print(list_d)
# print(list_e)
# print(list_a+list_a)

# # range
# for i in range(5,0,-1):
#     print(i)

# a=list([4,5,3,4,5,6,7])
# b=list(['a','b','c'])
# for i,j in zip(a,b):
#     print(i,j)

a=[1,3]+[3,4]+[3]*6
a.append([0])
print(a)