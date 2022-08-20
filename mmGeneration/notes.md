# styleGAN2 modules

- EqualLinearActModule
  - 相当于扩展了EqualizedLRLinearModule（它相当于W 来自PGGAN）
  - 将输入X展平成一维，然后选择WX,WX+b,O(WX+b),O(WX),fused_bias
  - 用于z到w的映射
  - 相当于MLP
- ConstantInput 
  - 就是nn.Parameter(), [N,C,4,4]
- ModulatedStyleConv
  - 把ModulatedConv2d、noise、激活合在一起了
  - ModulatedConv2d: 
    - 保证kernel size为奇数
    - 可以使用blur进行模糊操作,尺寸+-1pix
    - style由512维度经过一个MLP变为input维度，也就是等于3D卷积核厚度，每个3D卷积核共享相同的style，
      然后每个input\*k\*k的3D卷积核均乘以相同的style，也就是说style对所有特征图的作用是相同的，不同
      之处在于各个3D卷积核自身的参数不同，之后每个3D卷积核自身再进行归一化（demod）
    - 上采样时，反卷积之后进行blur操作
    - 下采样时，blur之后进行卷积
  - NoiseInjection:
    - 就是简单叠加noise，初始化时分配noise权重，前项传播时添加noise
  - 先卷积，再添加noise，再激活
- ModulatedToRGB
  - 只有上采样，也由ModulatedConv2d组成
  - 先卷积，再bias，不激活，然后上采样
  - ModulatedConv2d:
    - out通道固定为3
    - 卷积核尺寸固定为1
    - 不使用demodulate
- ConvDownLayer
- ModMBStddevLayer
- ResBlock