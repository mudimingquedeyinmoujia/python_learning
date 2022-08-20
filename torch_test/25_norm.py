import torch

out_channels=3
in_channels=5
kernel_size=3
a=torch.arange(15*4).resize(3,5,4)*1.
print(a)
# 维度是n,那么这个维度的元素数目由k（向量数）变为1（范数）
print(a.norm(dim=0)) # 把0维度看做是一个向量，求范数
print(a.norm(dim=1)) # 把1维度看做是一个向量，求范数
print(a.norm(dim=[0,1]))