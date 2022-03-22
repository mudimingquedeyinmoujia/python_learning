from tensorboardX import SummaryWriter
import numpy as np
from PIL import Image
from torchvision import transforms
# 建议每跑一次就换一个文件夹存储

writer=SummaryWriter('runs/exp4')
for epoch in range(50):
    writer.add_scalar('scalar/test',np.random.rand(),epoch)
    writer.add_scalars('scalar/scalars_test',{'x2sinx':epoch*epoch*np.sin(epoch),'xcosx':epoch*np.cos(epoch)},epoch)

# writer.close()


# img=Image.open('./dark.jpg')
# for epoch in range(1,21):
#     transform = transforms.Compose([
#         transforms.Resize((512//epoch, 512//epoch)),
#         transforms.ToTensor(),
#         # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # (-1,1)
#     ])
#     img_trans=transform(img)
#     img_name='dark_{}'.format(epoch)
#     writer.add_image(img_name,img_trans,epoch)