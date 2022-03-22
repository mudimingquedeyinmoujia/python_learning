import torch
import numpy as np
focal=1
W=10
H=10
# 1. 基本用法
# i, j = torch.meshgrid(torch.linspace(0, W-1, W), torch.linspace(0, H-1, H))  # pytorch's meshgrid has indexing='ij'
# print(i)
# print(j)
# i = i.t()
# j = j.t()
# print(i)
# print(j)
# 2. 射线的坐标转换
c2w=np.array([
                [
                    -0.9999021887779236,
                    0.004192245192825794,
                    -0.013345719315111637,
                    -0.05379832163453102
                ],
                [
                    -0.013988681137561798,
                    -0.2996590733528137,
                    0.95394366979599,
                    3.845470428466797
                ],
                [
                    -4.656612873077393e-10,
                    0.9540371894836426,
                    0.29968830943107605,
                    1.2080823183059692
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    1.0
                ]
            ])
c2w=torch.tensor(c2w)
K = np.array([
            [focal, 0, 0.5*W],
            [0, focal, 0.5*H],
            [0, 0, 1]
        ])
i, j = torch.meshgrid(torch.linspace(0, W-1, W), torch.linspace(0, H-1, H))  # pytorch's meshgrid has indexing='ij'
i = i.t() # 转置之后，矩阵的列成了x坐标，行成了y坐标，y再取负之后，就更符合坐标系了
j = j.t()
dirs = torch.stack([(i-K[0][2])/K[0][0], -(j-K[1][2])/K[1][1], -torch.ones_like(i)], -1)# [H W 3]
print(dirs)

# rays_d = torch.sum(dirs[..., np.newaxis, :] * c2w[:3,:3], -1)  # dot product, equals to: [c2w.dot(dir) for dir in dirs]
# print(rays_d.shape)
# Translate camera frame's origin to the world frame. It is the origin of all rays.
# rays_o = c2w[:3,-1].expand(rays_d.shape)
# print(rays_o)
# 3. torch * 与枚举
# ten_a=torch.tensor(np.arange(10))
# # print(ten_a.shape)
# # for i in ten_a:
# #     print(i)
# ten_b=torch.tensor(np.arange(10).reshape(2,5,1))
# # print(ten_b.shape)
# # for i in ten_b:
# #     print(i)
# ten_c=torch.tensor(np.arange(30).reshape(2,5,3))
# # print(ten_c.shape)
# # for i in ten_c:
# #     print(i)
# ten_d=ten_b*ten_c
# print(ten_d)