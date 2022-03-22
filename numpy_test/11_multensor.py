import numpy as np
import torch

n_a=np.arange(10).reshape(10,1)
t_b=torch.Tensor(np.arange(20).reshape(10,2))
print(n_a)
print(t_b)
t_c=t_b.mul(n_a)
print(t_c)