import numpy as np

# 可以使用索引改变数组元素
a = np.arange(0, 10)
print(a)
a[4] = 9
print(a)

# 可以使用索引改变数组中的某行某列
b = a.reshape(2, 5)
print(b)
b[1, 3:] = 100, 999
print(b)
c=b[0,3]
print(c)
c=44
print(b)
