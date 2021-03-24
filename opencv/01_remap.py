import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from skimage import io

# 将图像100到200像素位置放大，mapx指的是列，mapy指的是行
# img = io.imread('../matplot_test/image002.jpg')
# row,col=img.shape[0],img.shape[1]
# print(row,col)
# listx=[np.linspace(100,200,col) for i in range(col)]
# listy=listx
# mapx = np.array(listx,dtype=np.float32)
# mapy = np.array(listy,dtype=np.float32).T
#
# dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
# plt.subplot(121)
# plt.imshow(img)
# plt.subplot(122)
# plt.imshow(dst)
# plt.show()

# 上 [100,150] 左 [150,50] 右 [160,200] 下[200,160] 这四个点
img = io.imread('../matplot_test/image002.jpg')
row,col=img.shape[0],img.shape[1]
print(row,col)


mapx = np.array(listx,dtype=np.float32)


dst = cv.remap(img, mapx, None, cv.INTER_LINEAR)
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(dst)
plt.show()

