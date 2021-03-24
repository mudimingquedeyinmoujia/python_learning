import numpy as np

pre=np.random.random(size=(3,4))
print(pre)
print(pre*255)
pre_chage=np.array(pre*255,dtype=np.dtype(np.int))
print(pre_chage)