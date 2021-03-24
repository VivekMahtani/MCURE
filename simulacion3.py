import numpy as np
import control
import matplotlib.pyplot as plt

sysgp = control.tf(1, [4.56, 0.8])
[t,y] = control.step_response(-0.01*sysgp)

plt.figure(1)
plt.plot(t,y)
plt.grid()
plt.show()
