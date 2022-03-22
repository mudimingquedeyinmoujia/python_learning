import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

x = np.array([-1, 0, -1, 0])
y = np.array([1, 1, 0, 0])
z = np.array([-1, -1, -1, -1])

x1 = np.array([0, -0.7, 0, -0.7])
y1= np.array([-1.41, -0.7, -1.4, -0.7])
z1 = np.array([1, 1, 0, 0])

ax = plt.subplot(projection = '3d')  # 创建一个三维的绘图工程
ax.set_title('3d')  # 设置本图名称
ax.scatter(x, y, z, c = 'r')   # 绘制数据点 c: 'r'红色，'y'黄色，等颜色
ax.scatter(x1,y1,z1,c='b')
ax.set_xlabel('X')  # 设置x坐标轴
ax.set_ylabel('Y')  # 设置y坐标轴
ax.set_zlabel('Z')  # 设置z坐标轴

plt.show()