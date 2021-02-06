import torch
import torch.nn as nn

net = nn.Sequential(nn.Linear(4, 3), nn.ReLU(), nn.Linear(3, 1))

print(net)

x = torch.rand(2, 4)
y = net(x).sum()

# 访问网络的所有参数
for name, param in net.named_parameters():
    print(name, " and ", param, " and ", type(param))

for name, param in net[0].named_parameters():
    print(name, " and ", param, " and ", type(param))


# torch.nn.parameter.Parameter 这个类是tensor的子类，如果是Parameter这个类才会被添加到模型的参数列表，否则不会出现，比如说：
class MyModule(nn.Module):
    def __init__(self):
        super(MyModule, self).__init__()
        self.weight1 = nn.Parameter(torch.rand(2, 4))
        self.weight2 = torch.rand(2, 4)

    def forward(self, x):
        x = torch.mm(self.weight1, x)
        y = torch.mm(self.weight2, x)
        return y

nt=MyModule()
for name, param in nt.named_parameters():
    print(name,param)

# 使用tensor.data/Parame.data来访问具体的参数数值
# 使用.grad访问梯度值
for name,param in net.named_parameters():
    print(param.data,param.grad)

# 记住一点！！！自定义层无非就是存储一些参数！！！