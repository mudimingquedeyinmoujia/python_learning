import torch
import numpy as np

torch.set_printoptions(threshold=np.inf)
torch.set_default_tensor_type('torch.cuda.DoubleTensor')
ten_pi=torch.tensor(np.pi)
print(f'loss {ten_pi}')
print(ten_pi.dtype)