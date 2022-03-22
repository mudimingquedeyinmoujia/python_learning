import numpy as np

# a=np.arange(60)
# aa=a.reshape(3,4,5)
# print(aa)
#
# print(np.max(aa))
# print(np.min(aa))
# print(np.max(aa[:,:,0]))
# print(np.max(aa[:,:,1]))
# print(np.max(aa[:,:,2]))
# print(np.max(aa[0,:,:]))
# print(np.max(aa[1,:,:]))
# print(np.max(aa[2,:,:]))

label=np.arange(30).reshape(10,3)

print(label)
max_x,min_x=np.max(label[:,0]),np.min(label[:,0])
max_y,min_y=np.max(label[:,1]),np.min(label[:,1])
max_z,min_z=np.max(label[:,2]),np.min(label[:,2])
print(max_x,max_y,max_z,min_x,min_y,min_z)
