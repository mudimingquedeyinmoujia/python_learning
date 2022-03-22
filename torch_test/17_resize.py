import torch



z_test=torch.FloatTensor(3,5)
print(z_test)
z_test.data.resize_(3, 5).normal_(0.0, 1.0)
print(z_test)

a=list(range(0,100,5))
print(a)