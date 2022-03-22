import torch
from torch.autograd import Variable

# a=torch.FloatTensor(5,8)
# print(a)
#
# b=torch.FloatTensor(5).fill_(1)
# print(b)

c=torch.tensor([[2.1,1],[4,2]],requires_grad=True)
print(c)
cc=Variable(c,requires_grad=True)
print(cc)
print(cc.grad)
d=torch.mean(cc[0][0]*5)
d.backward()
print(cc.grad)
e=torch.mean(c[0][0]*5)
e.backward()
print(c.grad)