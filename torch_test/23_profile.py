import torch

x = torch.randn((1, 1), requires_grad=True)
with torch.autograd.profiler.profile() as prof:
     for _ in range(100):  # any normal python code, really!
         y = x ** 2
         y.backward()
# NOTE: some columns were removed for brevity
print(prof.key_averages().table(sort_by="self_cpu_time_total"))