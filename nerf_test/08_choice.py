import torch
import numpy as np

ten_a=torch.Tensor(np.array([i for i in range(20)]))
ten_b=np.random.choice(ten_a,size=10,replace=False)
print(ten_a)
print(ten_b)