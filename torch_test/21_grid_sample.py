import torch
import numpy as np

feature = torch.arange(120.).view(2, 3, 4, 5)
rx=2/4/2
ry=2/5/2
# print(feature)
x = torch.linspace(-1, 1, 5)+1e-6+rx*5/3
y = torch.linspace(-1, 1, 6)+1e-6+ry*5/3
x_c, y_c = torch.meshgrid(x, y)
coord = torch.stack([x_c, y_c]) # 2,5,11 坐标通道，行数，列数
coord_grid = coord.permute(1, 2, 0).unsqueeze(0).expand(2, x.shape[0], y.shape[0], 2)  # 变成batch,行数,列数,坐标通道
print(coord_grid)

res = torch.nn.functional.grid_sample(feature, coord_grid.flip(-1), mode='nearest', align_corners=False, padding_mode='zeros') # 得到N,C,H,W
# # # print(feature)
print(res[0][0])

