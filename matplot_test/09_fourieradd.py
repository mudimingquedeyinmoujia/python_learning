import numpy as np
import matplotlib.pyplot as plt
import math

x = (np.arange(100) / 100) * 2 - 1

add_list = [[np.sin(math.pi * i * x), np.cos(math.pi * i * x)] for i in range(1, 5)]
all_list = []
for s, c in add_list:
    all_list.append(s)
    all_list.append(c)

proj1 = np.random.randn(8)
proj2 = np.random.randn(8) * 1/(np.array([1, 1, 2, 2, 3, 3, 4, 4]))
proj3 = np.random.randn(8) * 1/(np.array([1, 1, 4, 4, 8, 8, 16, 16]))
proj4 = np.random.randn(8) * 1/(np.array([1, 1, 4, 4, 8, 8, 1000, 1000]))

y1 = 0
y2 = 0
y3 = 0
y4 = 0
for index, ele in enumerate(all_list):
    y1 += ele * proj1[index]
    y2 += ele * proj2[index]
    y3 += ele * proj3[index]
    y4 += ele * proj4[index]

ax1 = plt.subplot(2, 2, 1, frameon=False)  # 两行一列，位置是1的子图
plt.plot(x, y1, 'r--')
plt.ylabel('y1')
ax2 = plt.subplot(2, 2, 2)
plt.plot(x, y2, 'r--')
plt.ylabel('y2')
plt.xlabel('x')
plt.subplot(2, 2, 3)
plt.plot(x, y3, 'r--')
plt.ylabel('y3')
plt.subplot(2, 2, 4)
plt.plot(x, y4, 'r--')
plt.ylabel('y4')
plt.show()
