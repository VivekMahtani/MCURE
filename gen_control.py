'''
Se trata de simular el lazo de control de generación del sistema formado por 
gobernador, turbina y generación. La señal de reliamentació nse toma de la salida
de frecuencia del generador se ultiplica por el factor 1/R (speed droop)

Los parámetros se dan un unidades pu.
Se considera una variacion de carga en el instante t=10s con valor 0.01pu
Obsérvese que dependiendo del valor que le demos a R, el sistema será capaz de 
contribuir en mayor o menor medida a corredir la variación de frecuencia
'''

import control as ctr
from matplotlib import pyplot as plt
import numpy as np

#%% Parameters
Tg=0.3
Tch=0.5
M=4.0
D=0.8
R=1/0.1
#R=1e10
DPlv=0.01 #   Load variation (pu)

#%% Transfer functions
s_gov=ctr.tf(1,[ Tg, 1])
s_pmov=ctr.tf(1,[Tch, 1])
s_gen=ctr.tf(1,[M, D])
s_droop=ctr.tf(1,[R])
s_aux=ctr.tf(1,1)
s_aux1=ctr.tf(1,1)
#s_cont=ctr.tf(1,[Tg, 1])


#%% Block diagram reduction

syst=ctr.append(ctr.tf2ss(s_gov),ctr.tf2ss(s_pmov),ctr.tf2ss(s_gen),ctr.tf2ss(s_droop), ctr.tf2ss(s_aux),ctr.tf2ss(s_aux1))
q=[[1,-4, 0],
   [2, 1, 0],
   [3, 6, 0],
   [4, 3, 0],
   [5, 0, 0],
   [6, 2, -5]
   ]
inp=[1,5]
out=[3,2,6]
syslc=ctr.connect(syst,q,inp,out)
#%% Simulation
t=np.arange(0,40,0.05)
Lr= np.zeros(t.size,)    # Load reference
DPl= DPlv*np.ones(t.size,)  # Load variations
#DPl= np.zeros(t.size,)  # Load variations
DPl[0:int(20/2/0.05)]=0
u=[Lr,DPl]
t,[Dw,DPmec,DP],xout=ctr.forced_response(syslc,t,u)
Dw=Dw*50

#%% Graphical Representation
plt.figure(1)
plt.plot(t,50+Dw)
plt.ylabel('Frec (Hz.)')
plt.xlabel('Tiempo (s.)')
plt.ylim(49.0,50)
plt.grid()

plt.figure(2)
plt.plot(t,DPmec)
plt.ylabel('DPmec (pu)')
plt.xlabel('Tiempo (s.)')
plt.grid()

plt.figure(3)
plt.plot(t,DP)
plt.ylabel('DP (pu)')
plt.xlabel('Tiempo (s.)')
plt.grid()

plt.show()
