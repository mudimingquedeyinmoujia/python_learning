import torch
import numpy as np

# npa=np.arange(75).reshape(3,5,5)
# # print(npa)
# npb=np.arange(75).reshape(3,5,5)
# # print(npb)
# tcha=torch.from_numpy(npa)
# tchb=torch.from_numpy(npb)
# print(tcha.size())
# print(tchb.size())
#
# tchc=torch.sum(tcha,dim=0)
# print(tcha)
# print(tchc)
# npc=np.array([10 for i in range(25)]).reshape(5,5)
# tchd=torch.from_numpy(npc)
# print(tchd)
# tche=tchc*tchd
# print()

suma=np.arange(20).reshape(10,2)
tena=torch.Tensor(suma)
print(tena)
a=torch.sum(tena)
b=torch.mean(tena)
print(a)
print(b)