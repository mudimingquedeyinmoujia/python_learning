import torch
import numpy as np

inputs=torch.Tensor(np.arange(60).reshape(4,5,3))
# inputs_flat = torch.reshape(inputs, [-1, inputs.shape[-2]])
# print(inputs)
# print(inputs_flat)

inputs2=torch.Tensor(np.arange(20).reshape(4,5))
print(inputs2[:,None].expand(4,5,5))
print(list(inputs.shape[:-1])+[8])
