import numpy as np

a=np.arange(15).reshape(3,5)
print(a)
print(np.amax(a))
print(np.amax(a,0))
print(np.amax(a,1))
print(np.ptp(a))
print(np.ptp(a,0))
print(np.ptp(a,1))

# 关于维数
b=np.arange(15).reshape(5,-1)
print(b)
c=np.reshape(b,[-1])
print(c)
d=b[:,:,np.newaxis]
print(d)
print(d.shape)
print("new test")
dim_3=np.arange(30).reshape(3,5,2)
print(dim_3)

# reshape(-1)
print("----")
shp_ndarray=np.arange(15).reshape(3,-1)
print(shp_ndarray)
shp_ndarray_1=shp_ndarray.reshape(-1)
print(shp_ndarray_1)