from torchvision.utils import make_grid
import torch
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from tensorboardX import SummaryWriter

transform = transforms.Compose([
    transforms.Resize((512, 512)),
    transforms.ToTensor(),
    # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # (-1,1)
])

img1=Image.open('img_01.jpg')
img2=Image.open('img_02.jpg')
img3=Image.open('img_03.jpg')
img4=Image.open('img_04.jpg')

img1_trans=transform(img1)
img2_trans=transform(img2)
img3_trans=transform(img3)
img4_trans=transform(img4)

ten=torch.stack([img1_trans,img2_trans,img3_trans,img4_trans])
# for i in ten[:3]:
#     print(i)
# grid=make_grid(ten,nrow=2).numpy().transpose(1, 2, 0)
grid_ten=make_grid(ten,nrow=2) # C,H,W
# imshow(grid)
# plt.show()

writer=SummaryWriter('runs/exp4')
batch_list=[grid_ten for i in range(4)]
for epoch in range(10):
    for index,img in enumerate(batch_list):
        writer.add_image('img_{:03d}_list{}'.format(epoch,index),img,epoch)