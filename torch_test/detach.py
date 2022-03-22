import torch
default_uv_shape=[256,256,3]
import numpy as np
from skimage import io
device=torch.device("cuda" if torch.cuda.is_available() else "cpu")


def process_uv(uv_coordinates):
    [uv_h, uv_w, uv_c] = default_uv_shape
    uv_coordinates=uv_coordinates.clone()
    uv_coordinates[:, 0] = uv_coordinates[:, 0] * (uv_w - 1)
    uv_coordinates[:, 1] = uv_coordinates[:, 1] * (uv_h - 1)
    uv_coordinates[:, 1] = uv_h - uv_coordinates[:, 1] - 1
    # uv_coordinates = np.hstack((uv_coordinates, np.zeros((uv_coordinates.shape[0], 1))))  # add z
    return uv_coordinates

# uv_np=np.array([[0.1,0.5],[0.2,0.5],[0.3,0.5],[0.1,0.2]])
# uv_coords=torch.Tensor(uv_np)
# a=process_uv(uv_coords)
# print(a)
# print(uv_coords)
a=np.ones((12,1))
print(a)
a[5,0]=3
print(a)
