import numpy as np
import control
import matplotlib.pyplot as plt


# Sistema de la diapo 100 tema 3

R = 2
Tg = 4
Tch = 15
M = 100
D = 1


sysgov = control.tf(1, [Tg, 1])
sysmov = control.tf(1, [Tch, 1])
syseng = control.tf(1, [M, D])
sysR = control.tf(1,R)


sys_total = control.append(control.tf2ss(sysgov), control.tf2ss(sysmov), control.tf2ss(syseng), control.tf2ss(sysR))

# FDT en lazo cerrado con 2 entradas y una salida:

Q = np.array([[1,-4], [2,1], [3,2], [4,3]])

#Entradas:

inp = np.array([1, 3])
out = np.array([3])

syslc = control.connect(sys_total, Q, inp, out)


print(syslc)