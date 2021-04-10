import numpy as np
import control
import matplotlib.pyplot as plt

plt.style.use('seaborn')

# In this assignment you have to simulate a closed-loop control system 
# using Octave. 
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

Kc = np.linspace(1, 5., 4)
Ki = 0.005

def assignment2(Kc=Kc, Ki=Ki): #Kc has to be a list; Ki has to be a float

	# Defining the transfer functions
	sysgp = control.tf(4, [500,2]) #Process
	sysgv = control.tf(2, [1,10,1]) #Valve
	sysgt = 2 # Sensor

	syspi_list = []
	# Loop to iterate among the different values of Kc
	for i in Kc:
		syspi = control.tf([i, i*Ki],[1,0])
		syspi_list.append(syspi)

	# Plotting the figures with the different values of Kc
	plt.figure()
	for i in range(len(syspi_list)):
		#Defining the closed loop
		syslc = control.feedback(syspi_list[i]*sysgv*sysgp,sysgt)
		consig = 1/sysgt # The setpoint is 0.5, because the sensor
						# transfer function is equal to 2
		t, y = control.step_response(syslc,200)
		error = np.abs(y - consig) # The error while achieving the setpoint
		plt.plot(t, y, label=f'Kc= {Kc[i]:.2f}')
		# plt.plot(t, error, label=f'Error para Kc={Kc[i]:.2f}')
		plt.title(f'Ki= {Ki:.4f}')
	
	plt.legend()
	plt.xlabel('Time (s)')
	plt.ylabel('Value')
	plt.show()
	return syspi_list

assignment2()

Ki_list = np.linspace(0., 0.005, 10)
# Funtion for different values of Ki
def plot_varying_Ki(Kc=Kc, Ki_list=Ki_list): #Now Kc AND Ki are lists.
	for i in range(len(Ki_list)):
		assignment2(Kc=Kc, Ki=Ki_list[i])
	pass

plot_varying_Ki()


Kc = [2]
Ki_list = np.linspace(0.001, .20, 10)
plot_varying_Ki(Kc=Kc, Ki_list=Ki_list)



