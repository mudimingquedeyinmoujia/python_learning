import functools
import random
import math
from PIL import Image
import PIL
from torchvision import utils
import numpy as np
import torch
from torch.utils.data import Dataset
from torchvision import transforms
import os
import torch.nn.functional as F

def resize_fn(img, size):
    return transforms.ToTensor()(
        transforms.Resize(size, Image.BICUBIC)(
            transforms.ToPILImage()((img.squeeze()+1)/2))).unsqueeze(0)


def load_imageToten(loadpath, resize, norm=True):
    """
    from load path to load image to tensor
    return: [1,3,H,W]
    """
    img = Image.open(loadpath)

    if norm:
        transform_bicub = transforms.Compose([
            transforms.Resize((resize, resize), interpolation=PIL.Image.BICUBIC),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ])
    else:
        transform_bicub = transforms.Compose([
            transforms.Resize((resize, resize), interpolation=PIL.Image.BICUBIC),
            transforms.ToTensor(),
        ])

    img_res = transform_bicub(img).unsqueeze(0)
    return img_res


def save_tenimage(imgTensor, svpath, svname, norm=True):
    utils.save_image(
        imgTensor,
        os.path.join(svpath, svname),
        nrow=1,
        normalize=norm,
        range=(-1, 1),
    )


if __name__ == "__main__":
    imgten = load_imageToten('./img_01.jpg',resize=512)
    print(imgten.shape)
    # img_resize = resize_fn(imgten, (100, 100))
    img_resize=F.interpolate(imgten,size=(100,100),mode='nearest')
    print(img_resize.shape)
    save_tenimage(img_resize,'./','resized_02.png')
