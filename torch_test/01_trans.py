import torch
import numpy as np

# 使用view/reshape之后返回的是个视图,他们共享内存,和numpy的reshape不同!
# 通过[][]可以修改tensor的元素
a=torch.tensor(np.arange(10).reshape(2,5))
print(a)
b= a.reshape(5,2)
#b= a.view(5,2)
print(a)
print(b)
b[1][1]=12
print(a)
print(b)

# 查看tensor的长度用shape和size()都可以
nd_a=np.arange(15).reshape(3,5)
print(a.shape[0],a.shape[1],a.shape)
print(a.size()[0],a.size()[1],a.size())
print(nd_a.shape)

# 高级索引测试
slic=torch.tensor(np.arange(15).reshape(3,5))
print(slic)
print(slic[[0,0,2,2],[0,4,0,4]].view(2,2))

# gather
# dim=0 竖着行方向为脚标，依次按照列进行提取，所以index的个数必须要等于原列数
# dim=1 横着列方向为脚标，依次按照行进行提取，所以index的个数必须要等于原行数
# 总之最终结果的形状与index匹配
print(slic.gather(dim=0,index=torch.tensor([0,1,2,1,0]).view(1,-1)))
print(slic.gather(dim=1,index=torch.tensor([2,3,2]).view(-1,1)))

