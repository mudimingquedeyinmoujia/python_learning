import torch
# 在指定位置加上维度为1的维度
a=torch.randn(3,4)
a_x=a.unsqueeze(0) # 1,3,4
a_y=a.unsqueeze(1) # 3,1,4
a_z=a.unsqueeze(2) # 3,4,1
print(a)
print(a_x)
print(a_y)
print(a_z)

# 针对一行的元素可以进行转置
b=torch.randn(4)
print(b)
bb=b.unsqueeze(1)
print(bb) # 变成四行一列
bbb=b.unsqueeze(0)
print(bbb) # 变成一行四列

print("----------")
c=torch.randn(4,4,3)
c2=torch.randn(4,4,3)
list_c=c,c2
ite=[list_c[i] for i in range(1) ]
print(ite)