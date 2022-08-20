import torch
import numpy as np

# N C H W + N h w 2 = N C h w
feature = torch.arange(120.).view(2, 3, 4, 5)
rx=2/4/2
ry=2/5/2
print('-'*20)
print(feature[0][0])
print('-'*20)
h = torch.linspace(-1, 1, 5)+1e-6
w = torch.linspace(-1, 1, 6)+1e-6
h_c, w_c = torch.meshgrid(h, w)
coord = torch.stack([h_c, w_c]) # 2,5,6 坐标通道，行数，列数
# print(coord)
# coord_grid = coord.permute(1, 2, 0).unsqueeze(0).expand(2, h.shape[0], w.shape[0], 2).flip(-1) # 变成batch,行数,列数,坐标通道
coord_grid = coord.permute(1, 2, 0).unsqueeze(0).expand(2, h.shape[0], w.shape[0], 2).clone() # 变成batch,行数,列数,坐标通道
coord_grid[:,:,:,0]=coord_grid[:,:,:,0]+0.1
coord_grid[:,:,:,1]=coord_grid[:,:,:,1]
print('-'*20)
print(coord_grid[0])
print(coord_grid.shape)
print('-'*20)
res = torch.nn.functional.grid_sample(feature, coord_grid, mode='nearest', align_corners=False, padding_mode='zeros') # 得到N,C,H,W
# # # print(feature)
print(res[0][0])

