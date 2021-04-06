import numpy as np
import control
import matplotlib.pyplot as plt

plt.style.use('seaborn')

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

    # sysp = control.tf(4, [500, 2]) #proceso
    # sysv = control.tf(2, [1,10,1]) #valvula = actuador
    # syst = control.tf(2,1) #sensor

def assignment(Kc=np.linspace(1., 10., 4), Ki=0.005):
	sysgp = control.tf(4, [500,2]) #Process
	sysgv = control.tf(2, [1,10,1]) #Valve
	sysgt = 2
	syspi_list = []
	for i in Kc:
		syspi = control.tf([i, i*Ki],[1,0])
		syspi_list.append(syspi)
	plt.figure()
	for i in range(len(syspi_list)):
		syslc = control.feedback(syspi_list[i]*sysgv*sysgp,sysgt)
		consig = 1/sysgt
		t, y = control.step_response(syslc,200)
		error = -(y - consig)
		plt.plot(t, y, label=f'Kc= {Kc[i]:.2f}')
		# plt.plot(t, error, label=f'Error para Kc={Kc[i]:.2f}')
		plt.title(f'Ki= {Ki:.4f}')
	
	plt.legend()
	plt.xlabel('Time (s)')
	plt.ylabel('Value')
	plt.show()
	return syspi_list


def plot_varying_Ki(Ki_list=np.linspace(0., 0.005, 10)):
	for i in range(len(Ki_list)):
		assignment(Ki=Ki_list[i])
	pass


plot_varying_Ki()




















