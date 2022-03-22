# myfunction=lambda x:x+44
# print(myfunction(3))

# embedding
import torch
import torch.nn as nn
import numpy as np

# max_freq=9
# N_freqs=10
# freq_bands = 2.**torch.linspace(0., max_freq, steps=N_freqs)
# freq_bands2 = torch.linspace(2.**0., 2.**max_freq, steps=N_freqs)
# print(freq_bands)
# print(freq_bands2)

class Embedder:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.create_embedding_fn()

    def create_embedding_fn(self):
        embed_fns = []
        d = self.kwargs['input_dims']
        out_dim = 0
        if self.kwargs['include_input']:  # true
            embed_fns.append(lambda x: x)
            out_dim += d

        max_freq = self.kwargs['max_freq_log2']  # 9/3
        N_freqs = self.kwargs['num_freqs']  # 10/4

        if self.kwargs['log_sampling']:  # true
            freq_bands = 2. ** torch.linspace(0., max_freq, steps=N_freqs)
        else:  # 如果不按照log采样那就是均匀采样
            freq_bands = torch.linspace(2. ** 0., 2. ** max_freq, steps=N_freqs)

        for freq in freq_bands:
            for p_fn in self.kwargs['periodic_fns']:
                embed_fns.append(lambda x, p_fn=p_fn, freq=freq: p_fn(x * freq))
                out_dim += d

        self.embed_fns = embed_fns
        self.out_dim = out_dim

    def embed(self, inputs):
        return torch.cat([fn(inputs) for fn in self.embed_fns], -1)


def get_embedder(multires, i=0):
    if i == -1:
        return nn.Identity(), 3

    embed_kwargs = {
        'include_input': True,
        'input_dims': 3,
        'max_freq_log2': multires - 1,  # 9/3
        'num_freqs': multires,  # 10/4
        'log_sampling': True,
        'periodic_fns': [torch.sin, torch.cos],
    }

    embedder_obj = Embedder(**embed_kwargs)
    embed = lambda x, eo=embedder_obj: eo.embed(x)
    return embed, embedder_obj.out_dim

embed_fun,out_dim=get_embedder(10)
x=torch.tensor(np.array([0,0,7]))
rx=embed_fun(x)
print(rx)
print(out_dim)