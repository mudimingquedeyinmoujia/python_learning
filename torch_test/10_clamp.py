import torch

# 如果大于这个区间就取最大值，如果小于这个区间就取最小值，而不是等比例压缩到这个区间
# a=torch.rand(10)*10
# print(a)
# b=torch.clamp(a,min=2.0,max=5.0)
# print(a)
# print(b)
# torch.clamp_(a,min=2.0,max=5.0)
# print(a)

aa = torch.rand(10) * 10 - 5
print(aa)
aa.clamp_(0.0)
print(aa)
