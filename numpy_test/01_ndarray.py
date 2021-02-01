import numpy as np

# 注意 ndarray 和 list 的区别在于前者没有逗号作为分隔
# ndarray的元素根据初始化的不同为int32、float64
list_pre_int=[1,2,3,4,5]
list_pre_float=[1.,2,3,4,5]
ndarray_a=np.array(list_pre_int)
ndarray_b=np.array(list_pre_float)
print(list_pre_int)
print(ndarray_a,ndarray_a.dtype)
print(ndarray_b,ndarray_b.dtype)

# 关于shape,相当于是一个属性，返回的是元组，不是函数
# reshape(n,m)方法相当于新建了一个矩阵,不会对原矩阵造成变化
ndarray_c=np.arange(10)
print(ndarray_c)
ndarray_d=ndarray_c.reshape(2,5)
print(ndarray_c)
print(ndarray_d)
print(ndarray_d.shape)

# 初始化,empty()/zeros()/ones()
# 默认是float64
ndarray_emp=np.empty([2,3])
ndarray_zer=np.zeros([2,3])
ndarray_one=np.ones([2,3])
print(ndarray_emp,'\n',ndarray_zer,'\n',ndarray_one)
print(ndarray_emp.dtype,ndarray_zer.dtype,ndarray_one.dtype)