import torch

a=torch.randn(1,3)
print(a)
b=torch.squeeze(a,0) # 如果x轴的维数为1,或者说只有一行,去掉x轴
bb=torch.squeeze(a) # 所有维数为1的都去掉
bbb=torch.squeeze(a,1) # 如果y轴的维数为1,或者说只有一列,去掉y轴
#bbbb=torch.squeeze(a,2) 这里去掉第三个维度会报错,因为a的维度本身就是两个维度
print(b)
print(bb)
print(bbb)
#print(bbbb)

c=torch.randn(3,1)
print(c)
d=c.squeeze()
print(d)

print("------")
# test1
# e=torch.randn(3,4,1)
# print(e)
# ee=e.squeeze()
# print(ee) #这里正常,原先的x是x,y是y

# test2
# f=torch.randn(3,1,4)
# print(f)
# ff=f.squeeze(1)# 如果是0或者2则不会有变化，因为其它轴的维度不是1
# print(ff) #原先的x是x,z变成y

# test3
# g=torch.randn(1,3,4)
# print(g)
# gg=torch.squeeze(g)
# print(gg) # 原先的y成了x,z成了y