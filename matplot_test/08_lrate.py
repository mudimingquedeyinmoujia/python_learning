import matplotlib.pyplot as plt
import numpy as np

lrate=5e-4
lrate_decay=2

global_step=np.arange(1000)
decay_rate = 0.1
decay_steps = lrate_decay * 100
new_lrate = lrate * (decay_rate ** (global_step / decay_steps))

plt.plot(global_step,new_lrate)
plt.show()