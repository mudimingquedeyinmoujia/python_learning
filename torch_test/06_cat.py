import numpy as np
import torch

tena=torch.tensor(np.arange(6).reshape(2,3))
listb=[tena for i in range(6) ]
tendimF1=torch.cat([i for i in listb],dim=-1)
tendim0=torch.cat([i for i in listb],dim=0)
tendim1=torch.cat([i for i in listb],dim=1)
tendimF2=torch.cat([i for i in listb],dim=-2)
print(tendimF1)
print(tendim0)
print(tendim1)
print(tendimF2)
# dim=0 按照行 dim=1按照列 dim=-1按照倒数第一个维度