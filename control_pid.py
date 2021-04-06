import numpy as np
import control
from  matplotlib import pyplot as plt
# definir las fdt
sysgp=control.tf(10,[1,1])
[numd,dend]=control.pade(0.01,3)
sysd=control.tf(numd,dend)
sysgpd=sysgp*sysd
#sysga=control.tf(1,[1/10,1])
sysga=control.tf(1,[1/10, 1])
sysgt=control.tf(1,1)
Kp=0.1
Ti=10 #Ki=1/Ti
#Ki=0
Td=0
N=1000
sysp=control.tf(Kp,1)
sysi=control.tf(1,[Ti,0])
sysd=control.tf([Td, 0],[1/N, 1])
syspid=sysp+sysi+sysd
#obtener la fdt en lazo cerrado mediante feedback
syslc=control.feedback(syspid*sysga*sysgpd,sysgt)
#t=np.arange(0,0.1,100)
[t,y1]=control.step_response(4*syslc,100)
# %%
plt.figure(1)
plt.plot(t,y1)
plt.grid()
plt.show()
