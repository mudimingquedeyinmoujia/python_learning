import torch
from torchvision import utils
from tqdm import tqdm
import math
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
import PIL.Image
from torchvision import transforms
import random


def imageToten(loadpath, resize, norm=True):
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


def crop_ten(img_tensor, crop_size):
    x0 = random.randint(0, img_tensor.shape[-2] - crop_size)
    y0 = random.randint(0, img_tensor.shape[-1] - crop_size)
    crop_img = img_tensor[:, :, x0:x0 + crop_size, y0:y0 + crop_size]
    return crop_img
