import numpy as np
import control
import matplotlib.pyplot as plt

# sysgp = control.tf(10, [1,1,0])
# sysga = control.tf(1,[1/10, 1])
# sysgt = control.tf(1,1)


# In this assignment you have to simulate a closed-loop control system using Octave. 
# The system to be controlled is the heat exchanger studied in class. 
# The elements in the closed-loop are:

# Gp(s)=T(s)/Fv(s)=4/(500s+2)  (tranfer function of the process)

# Gv(s)=Fv(s)/U(s)=2/(s^2+10s+1)  (valve tranfer function) 

# Gt(s)=Tm(s)/T(s)=2  (sensor transfer function)

# Gc(s)=U(s)/E(s)=kc*(1+ki/s) (PI controller transfer function)



