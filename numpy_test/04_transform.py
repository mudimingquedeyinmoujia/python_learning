import numpy as np
a=np.arange(15).reshape(3,5)
print(a)
a=a+1
print(a)
a=a*2
print(a)

# .T和transpose代表对数组进行转置，返回转置的一个新的数组,不会对原数组进行操作
print(a.T)
print(np.transpose(a))
print(a)

# 连接矩阵
# 轴为0,相当于np.vstack((b,c))
# 轴为1,相当于np.hstack((b,c))
print("concat new matrix")
b=np.arange(15).reshape(3,5)
c=b+100
concat_mat=np.concatenate((b,c),axis=0) # 轴为0,相当于np.vstack((b,c))
print(concat_mat)

# 切分矩阵
print("split matrix")
e=np.arange(32).reshape(4,8)
print(e)
f=np.split(e,4,axis=1)
print(f)
