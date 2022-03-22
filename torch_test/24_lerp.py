import torch

start = torch.arange(1., 5.)
end = torch.empty(4).fill_(10)


a=torch.lerp(start, end, 0.5)

print(a)
print(start.lerp(end,0.5))