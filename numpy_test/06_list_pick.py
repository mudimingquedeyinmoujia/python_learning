import numpy as np
# 在索引的时候可以对某一个维度实行list操作
a=np.arange(15)
print(a)
b=a[[1,3,5,3,2,1,6]]
print(b)

print("higher slice")
# 总之明确这几点：
# 中括号里面逗号分隔维度
# 对于每一个维度,如果是数字,那么最终结果就是只有一个;如果是n个元素的数组,那么最终结果就是n个,并且不同维度的数组shape必须相同
x = np.array([[1,  2],  [3,  4],  [5,  6]])
print(x)
y = x[[0,1,2],  [0,1,0]]
print (y)
print("---")
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print('这个数组的四个角元素是：')
print(y)
# 相同的取法
print(x[[0,0,3,3],[0,2,0,2]].reshape(2,2))
