import numpy as np
import matplotlib.pyplot as plt

x=np.arange(18)+1
y_loss=[0.5805,0.3598, 0.3232,0.2892,0.2598,
        0.2409,0.2271,0.2147,0.1707,0.1171,
        0.1059,0.1001,0.0957,0.0923,0.0898,
        0.0879,0.0861,0.0848]
y_metric=[0.2281,0.1397, 0.1253,0.1118,0.1004,
          0.0931,0.0878, 0.0831,0.0650,0.0425,
          0.0382,0.0360,0.0345, 0.0333,0.0324,
          0.0317,0.0311, 0.0306]
y_val=[0.2555,0.1814,0.1460,0.1331,0.1228,
       0.1186,0.1120, 0.1028, 0.0585,0.0527,
       0.0504, 0.0523,0.0524, 0.0543,0.0543,
       0.0524,0.0467,0.0531]
y1=np.array(y_loss)
y2=np.array(y_metric)
y3=np.array(y_val)
plt.xticks(x)
plt.yticks(np.array([i/10 for i in range(8)]))
plt.grid(True,linewidth=0.2)
plt.xlabel('epoch')
plt.ylabel('loss/nme loss')
plt.title('training')
plt.plot(x,y1,'ro-',x,y2,'bo--',x,y3,'go--')
plt.show()