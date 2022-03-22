import torch
import numpy as np

tena=torch.tensor([1,2,3,4,5])
print(tena)

tena=tena[[0,3,4]]
tena[0]=-tena[0]
print(tena)
