import  torch

# flip 返回某个指定维度的倒序拷贝
x=torch.arange(15).view(3,5)
print(x)
y=x.flip(0)
z=x.flip(1)
t=x.flip(-1)
print(y)
print(z)
print(t)