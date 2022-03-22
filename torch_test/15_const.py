import numpy as np
import torch

a = np.array([1, 2, 3])  # int32
b = np.array([1.1, 3, 2.3])  # float64
f=np.ones(3)
g=torch.tensor([1,2,3])
e=torch.ones(4)
ca=torch.tensor(a)
caa=torch.Tensor(a)
cb=torch.tensor(b)
cbb=torch.Tensor(b)

print(ca.dtype,caa.dtype,cb.dtype,cbb.dtype,e.dtype,f.dtype,g.dtype)
print(ca,caa,cb,cbb)
a=a+1
b=b+1
print(ca,caa,cb,cbb)

