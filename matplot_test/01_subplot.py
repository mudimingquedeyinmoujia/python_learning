import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y1 = np.sin(x)
y2 = np.cos(x)

ax1 = plt.subplot(2, 2, 1, frameon=False)  # 两行一列，位置是1的子图
plt.plot(x, y1, 'b--')
plt.ylabel('y1')
ax2 = plt.subplot(2, 2, 2, projection='polar')
plt.plot(x, y2, 'r--')
plt.ylabel('y2')
plt.xlabel('x')
plt.subplot(2, 2, 3, sharex=ax1)
plt.plot(x, y2, 'r--')
plt.ylabel('y2')
plt.show()

# 明确如下几点
# subplot 分别为行数，列数，第几个
# plt.plot(横坐标列表，纵坐标列表，线的形式） 总之就是代表图表的内容
# def f(t):
#     return np.exp(-t) * np.cos(2 * np.pi * t)
#
#
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
#
# plt.figure("2subplot")
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#
# plt.subplot(212)
# plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
# plt.show()
