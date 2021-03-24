import matplotlib.pyplot as plt
import numpy as np

def show(event):
    print(event)
    print(type(event))

x=np.arange(10)
y=np.sin(x)
ax1=plt.subplot(221)
plt.plot(x,y,'b')
buttonaxe = plt.axes([0.7, 0.5, 0.1, 0.1])
button1 = plt.Button(buttonaxe, 'p2',color='khaki', hovercolor='yellow')
button1.on_clicked(show)
plt.show()
