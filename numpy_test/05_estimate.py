import numpy as np

a=np.arange(15).reshape(3,5)
print(a)
print(np.amax(a))
print(np.amax(a,0))
print(np.amax(a,1))
print(np.ptp(a))
print(np.ptp(a,0))
print(np.ptp(a,1))
