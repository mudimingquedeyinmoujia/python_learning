import numpy as np

a=np.arange(60)
aa=a.reshape(3,4,5)
print(aa)

print(np.max(aa))
print(np.min(aa))
print(np.max(aa[:,:,0]))
print(np.max(aa[:,:,1]))
print(np.max(aa[:,:,2]))
print(np.max(aa[0,:,:]))
print(np.max(aa[1,:,:]))
print(np.max(aa[2,:,:]))
