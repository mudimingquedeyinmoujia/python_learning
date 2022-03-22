import torch
import numpy as np

def get_uvcoords(H, W):
    i, j = np.meshgrid(np.linspace(0, W - 1, W), np.linspace(0, H - 1, H))
    dx = 1 / W
    dy = 1 / H
    for x in range(W):
        i[:, x] = dx / 2 + dx * x
    for y in range(H):
        j[y, :] = dy / 2 + dy * y

    j = np.flipud(j)
    uvs = np.stack((i, j), axis=2).reshape(H * W, 2)
    return uvs

def img2flat(img):
    """
    [H,W,C] to [H*W,C] from row top down
    :param img:
    :return:
    """
    rows=torch.chunk(img,len(img))
    flat=torch.cat(rows,dim=1)
    return flat.squeeze()

def flat2img(flat,H):
    """
    [H*W,C] to [H,W,C] follow row top down rule
    :param flat:
    :return:
    """
    rows=torch.chunk(flat,H)
    img=torch.stack(rows)
    return img


# img=torch.tensor(np.arange(75).reshape((5,5,3)))
# print(img)
# print(flat2img(img2flat(img),len(img)))
#
# ten=torch.Tensor(np.arange(25*3).reshape(25,3))
# # print(ten)
# # rows=torch.chunk(ten,5,dim=0)
# # img=torch.stack(rows)
# # print(img.shape)
# # img.transpose_(0,2) # hwc-cwh
# # img.transpose_(1,2) # cwh-chw
# # print(img.shape)
# print(ten.data)

ten1=torch.tensor(np.arange(15).reshape(5,3))
ten2=torch.tensor(np.arange(15).reshape(5,3)+1)
ten3=torch.tensor(np.arange(15).reshape(5,3)+2)
lis=[ten1,ten2,ten3]
ten4=torch.cat(lis,dim=0)
print(ten4)
