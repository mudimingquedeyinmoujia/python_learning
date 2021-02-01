import numpy as np

ndarray_pre = np.arange(0, 15)
ndarray_pre_shape = ndarray_pre.reshape(3, 5)
print(ndarray_pre_shape)

# 反转全部行
ndarray_rev_row = ndarray_pre_shape[::-1, ]
print("reverse all row")
print(ndarray_rev_row)
# 反转全部列
print("reverse all col")
ndarray_pre_col = ndarray_pre_shape[:, ::-1]
print(ndarray_pre_col)
# 几行几列
print("mytest")
ndarray_test=ndarray_pre_shape[1:,2:]
print(ndarray_test)

# 高级索引
print("higher slice")
x = np.array([[1,  2],  [3,  4],  [5,  6]])
print(x)
y = x[[0,1,2],  [0,1,0]]
print (y)

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print('这个数组的四个角元素是：')
print(y)
