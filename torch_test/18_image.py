from skimage import io
import matplotlib.pyplot as plt
import torch
from tqdm import tqdm
import numpy as np

# img=io.imread(r'E:\1 codes\unfield\datas\facescape\facescape_trainset_001_100\2\models_reg\1_neutral.jpg')
# img_ten=torch.from_numpy(img)
# io.imshow(img_ten.numpy())
# plt.show()

# at=torch.tensor(np.arange(15).reshape(3,5),dtype=torch.float32)
at = torch.nn.Embedding(3, 5, max_norm=1.0)
torch.nn.init.normal_(at.weight.data,0.0,1.0)
print(at.weight)