import torch
from mmGeneration.mmgeneration.mmgen.models.architectures.stylegan.modules.styleganv2_modules import Blur
from torchvision import utils
import os
import PIL.Image
from PIL import Image
from torchvision import transforms
blur_kernel=[1, 3, 3, 1]

imgpath='./test256.png'
img=Image.open(imgpath)
device=torch.device('cuda:0')
upsample=True
downsample=False

transform_bicub = transforms.Compose([
    # transforms.Resize((target_res, target_res),interpolation=PIL.Image.BICUBIC),
    transforms.ToTensor(),
    transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))])
transform_equal = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))])

img_init=transform_equal(img).to(device).unsqueeze(0)
kernel_size=3

if upsample:
    factor = 2
    p = (len(blur_kernel) - factor) - (kernel_size - 1)
    pad0 = (p + 1) // 2 + factor - 1
    pad1 = p // 2 + 1
    blur = Blur(blur_kernel, (pad0, pad1), upsample_factor=factor)
# build blurry layer for downsampling
if downsample:
    factor = 2
    p = (len(blur_kernel) - factor) + (kernel_size - 1)
    pad0 = (p + 1) // 2
    pad1 = p // 2
    blur = Blur(blur_kernel, pad=(pad0, pad1))

img_after=blur(img_init)

utils.save_image(
            img_after,
            f'./after01.png',
            nrow=1,
            normalize=True,
            range=(-1, 1),
        )