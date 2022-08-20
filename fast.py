import functools
import os
import random
import math
from PIL import Image
from tqdm import tqdm
import numpy as np
import torch
from torch.utils.data import Dataset
from torchvision import transforms

a = torch.randn(1, 3, 4, 4)
print(a.shape)

print(a.squeeze(0).shape)
