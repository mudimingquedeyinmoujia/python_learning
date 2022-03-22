import torch
import numpy as np

feature=torch.arange(120.).view(2,3,4,5)
# print(feature)
x=torch.linspace(-1,1,5)
y=torch.linspace(-1,1,5)
x_c,y_c=torch.meshgrid(x,y)
coord=torch.stack([y_c,x_c])
# # print(coord.shape) # 2,11,5 c h w
coord_grid=coord.permute(1,2,0).unsqueeze(0).expand(2,5,5,2) # 2,11,5,2
print(coord_grid[0][0])
res=torch.nn.functional.grid_sample(feature,coord_grid,mode='nearest',align_corners=False,padding_mode='zeros')
# # print(feature)
print(res[0][0])
# print(res.shape) # 2,3,11,5

