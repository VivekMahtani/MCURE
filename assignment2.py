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
# (kc*s + kc*ki)/s


# You have to write the Python script file to simulate this system and 
# to perform several simulations to study the effect of each control 
# action (P action and Integral action).

# You have to upload the python script with the code of the program and a 
# pdf file explaining the results obtained.

Kc = 4
Ki = 1

### Transfer functions

sysgp = control.tf(4, [500,2])
sysgv = control.tf(2, [1,10,1])
sysgt = control.tf(2,1)
syspi = control.tf([Kc, Kc*Ki], [1,0])

syslc = control.feedback(sysgp*sysgv*sysgt,syspi)
#t = np.arange(0,0.1,100)
[t,y1] = control.step_response(syslc, 50)
#El 4 es el valor de Yr

# plt.figure(1)
# plt.plot(t,y1)
# plt.grid()
# plt.show()


def plot_figures(Kc, Ki=0.7):
	sysgp = control.tf(4, [500,2])
	sysgv = control.tf(2, [1,10,1])
	sysgt = control.tf(2,1)
	syspi_list = []
	for Kc in Kc:
		syspi = control.tf([Kc, Kc*Ki], [1,0])
		syspi_list.append(syspi)
	plt.figure(1)
	for pi in syspi_list:
		syslc = control.feedback(sysgp*sysgv*sysgt,pi)
		t, y = control.step_response(syslc, 50)
		plt.plot(t, y, label=f'syspi: {pi}')
	plt.grid()
	plt.legend()
	plt.show()
	return syspi_list

plot_figures(Kc=[2,4,6,8,10])























