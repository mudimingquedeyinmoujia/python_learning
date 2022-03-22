import torch
import numpy as np

# x=torch.ones(2,2,requires_grad=True)
# y=x+2
# z=y*y*3
# out=torch.mean(z)
# print(out)
# out.backward()
# print(x.grad)

print("{:06d}.tar".format(23))
print(torch.version.cuda)
print(torch.cuda.is_available())
print(torch.backends.cudnn.version())

