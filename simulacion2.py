import numpy as np
import control
import matplotlib.pyplot as plt

sysgp = control.tf(10, [1,1,0])
sysga = control.tf(1,[1/10, 1])
sysgt = control.tf(1,1)

Kp = 1
Ti = 1e10
Td = 10
N=1000

sysp = control.tf(Kp,1)
sysi = control.tf(1,[Ti,0])
sysd = control.tf([Td,0], [1/N, 0])

syspid = sysp+sysi+sysd

syslc = control.feedback(syspid*sysga*sysgp*sysgt)
#t = np.arange(0,0.1,100)
[t,y1] = control.step_response(4*syslc, 20)
#El 4 es el valor de Yr

plt.figure(1)
plt.plot(t,y1)
plt.grid()
plt.show()