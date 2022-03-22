import numpy as np
import torch
import torch.nn as nn


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

        max_freq = self.kwargs['max_freq_log2']  # nerf:9/3 num_freqs-1,
        N_freqs = self.kwargs['num_freqs']  # nerf:10/4 位置编码的数量

        if self.kwargs['log_sampling']:  # true
            freq_bands = 2. ** torch.linspace(0., max_freq, steps=N_freqs)  # [2^0,2^1,...,2^max_freq] 位置编码数量
        else:  # 如果不按照log采样那就是均匀采样
            freq_bands = torch.linspace(2. ** 0., 2. ** max_freq, steps=N_freqs)

        for freq in freq_bands:
            for p_fn in self.kwargs['periodic_fns']:
                embed_fns.append(lambda x, p_fn=p_fn, freq=freq: p_fn(x * freq))
                out_dim += d

        self.embed_fns = embed_fns  # sin(2^0 x) cos(2^0 x) sin(2^1 x) cos(2^1 x) ...
        self.out_dim = out_dim

    def embed(self, inputs):
        return torch.cat([fn(inputs) for fn in self.embed_fns], -1)  # 按照最后一维拼接，拼接后维度不变


def get_embedder(multires, i=0):
    """
    获取位置编码函数与位置编码后的维度,没有使用pi
    :param multires: 位置编码频率，从0开始计算，依次是2^0,2^1,...,2^(multires-1) 共 multires 个
    :param i: 0代表默认位置编码，-1代表不进行位置编码
    :return: example: x,y,z --> x,y,z,sin(x),sin(y),sin(z),cos(x),cos(y),cos(z),sin(2^1x),sin(2^1y),sin(2^1z),cos(2^1x),
    cos(2^1y),cos(x^1z),... ///  输出的对于每个batch的维度
    """
    if i == -1:
        return nn.Identity(), 2

    embed_kwargs = {
        'include_input': True,  # 输出的编码是否包含输入的特征本身
        'input_dims': 2,  # 最好每个batch维度是一维，默认一维有三个分量
        'max_freq_log2': multires - 1,  # 最大的位置编码频率
        'num_freqs': multires,  # 位置编码频率数量
        'log_sampling': True,  # 默认按照2^0,2^1...2^n采样,否则在[0,2^n]均匀采样
        'periodic_fns': [torch.sin, torch.cos],
    }

    embedder_obj = Embedder(**embed_kwargs)
    embed = lambda x, eo=embedder_obj: eo.embed(x)
    return embed, embedder_obj.out_dim


if __name__ == '__main__':
    features = np.arange(10).reshape(5, 2)
    features_ten = torch.Tensor(features)
    emb_fn, out_dims = get_embedder(2, -1)
    print(emb_fn(features_ten), out_dims)
