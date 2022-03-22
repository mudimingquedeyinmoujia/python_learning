import random

base=[i*2 for i in range(20)]
print(base)
ind=random.sample(range(0,20),10)
print(ind)
samp=[base[i] for i in ind]
print(samp)