import matplotlib.pyplot as plt
import numpy as np

def loss_curve(epochs,loss_list):
    epochs_list=np.arange(epochs)+1

    plt.plot(epochs_list, loss_list, label="loss")
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.legend(loc=0, ncol=1)  # 参数：loc设置显示的位置，0是自适应；ncol设置显示的列数

    plt.show()

loss_list=[np.e**(1-i/100) for i in range(100)]
epochs=100

loss_curve(epochs,loss_list)
