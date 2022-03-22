import torch
import numpy as np
# input is radian
trans_t = lambda t : torch.Tensor([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,t],
    [0,0,0,1]]).float()

rot_phi = lambda phi : torch.Tensor([
    [1,0,0,0],
    [0,np.cos(phi),-np.sin(phi),0],
    [0,np.sin(phi), np.cos(phi),0],
    [0,0,0,1]]).float()

rot_theta = lambda th : torch.Tensor([
    [np.cos(th),0,-np.sin(th),0],
    [0,1,0,0],
    [np.sin(th),0, np.cos(th),0],
    [0,0,0,1]]).float()

# input is angle not radian
# 对于点的变化来说，phi是y-->-z的纬度，theta是y-->x的经度
# 初始位置为y轴顶点，x指向原x轴负方向，z指向上方
# 对点的作用：这个矩阵（4阶）可以把原点按照上述规则变换到球面上对应的点，最后一列是最终向量在y轴正方向的偏移
# 对向量的作用：这个矩阵（3阶）可以变换x,y,z轴，从而起到变换向量到新坐标系的作用
# 关键是要寻找这个变化矩阵，这个变化矩阵看作是一系列列向量，左乘向量（3阶）或点（4阶）即可local-->world坐标转换
def pose_spherical(theta, phi, radius):
    c2w = trans_t(radius)
    c2w = rot_phi(phi/180.*np.pi) @ c2w # phi是绕x轴逆时针旋转
    c2w = rot_theta(theta/180.*np.pi) @ c2w # theta是绕y顺时针轴旋转（做了对称之后可不就是绕x旋转吗）
    c2w = torch.Tensor(np.array([[-1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])) @ c2w # 纠正矩阵，x轴对调，y轴z轴对称！
    # 不管矩阵是在最左边第几个，这个矩阵的变换永远是相对于初始坐标系来说的！
    return c2w

# 1 一般试验
# theta=45
# phi=-45
# radius=1
# my_c2w=pose_spherical(theta,phi,radius)
# my_c2w_ten=torch.Tensor(my_c2w)
#
# print(my_c2w_ten)
# x=my_c2w_ten[0][3].item()
# y=my_c2w_ten[1][3].item()
# z=my_c2w_ten[2][3].item()
# print(x,y,z)
# print(x*x+y*y+z*z)
# focal=5
# W=10
# H=10
# K = np.array([
#             [focal, 0, 0.5*W],
#             [0, focal, 0.5*H],
#             [0, 0, 1]
#         ])
# i, j = torch.meshgrid(torch.linspace(0, W-1, W), torch.linspace(0, H-1, H))  # pytorch's meshgrid has indexing='ij'
# i = i.t() # 转置之后，矩阵的列成了x坐标，行成了y坐标，y再取负之后，就更符合坐标系了
# j = j.t()
# dirs = torch.stack([(i-K[0][2])/K[0][0], -(j-K[1][2])/K[1][1], -torch.ones_like(i)], -1)# [H W 3]
# rays_d = torch.sum(dirs[..., np.newaxis, :] * my_c2w_ten[:3,:3], -1) # 只是旋转，没有平移，向量点乘旋转矩阵，得到新坐标系下的方向
# print(dirs[0][0],dirs[0][9],dirs[9][0],dirs[9][9])
# print(rays_d[0][0],rays_d[0][9],rays_d[9][0],rays_d[9][9])
# new_dir=torch.Tensor(np.array([0,1,0]))[:,np.newaxis]
# print(new_dir)
# dot_1=my_c2w_ten[:3,:3].mm(new_dir)
# print(dot_1)
# 2 单纯旋转phi
test_y_dir=torch.Tensor(np.array([0,1,0]))[:,np.newaxis]
test_x_dir=torch.Tensor(np.array([1,0,0]))[:,np.newaxis]
test_z_dir=torch.Tensor(np.array([0,0,1]))[:,np.newaxis]
phi=-30
theta=40
c2w_1=rot_phi(np.pi*phi/180.)
c2w_2=rot_theta(np.pi*theta/180.) @ c2w_1
c2w_3=torch.Tensor(np.array([[-1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])) @ c2w_2
c2w=pose_spherical(theta,phi,1)
print(c2w_1)
print(c2w_2)
print(c2w_3)
print(c2w)
# print(c2w[:3,:3].mm(test_x_dir))
# print(c2w[:3,:3].mm(test_y_dir))
# print(c2w[:3,:3].mm(test_z_dir))# 只要确定一个y,z自然确定