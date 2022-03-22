import numpy as np
import torch

x=torch.Tensor([[3,4,5,6,8,3],[2,3,5,7,2,1],[1,2,3,4,5,6],[3,4,5,6,8,3],[2,3,5,7,2,1],[1,2,3,4,5,6]])
input_ch=3
input_ch_views=3
input_pts, input_views = torch.split(x, [input_ch, input_ch_views],dim=-1)
print(input_pts)
print(input_views)

