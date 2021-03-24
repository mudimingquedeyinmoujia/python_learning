from skimage import io
import matplotlib.pyplot as plt

image=io.imread('./image002.jpg') / 255
# 是否除以 255 无差别
io.imshow(image)
plt.show()