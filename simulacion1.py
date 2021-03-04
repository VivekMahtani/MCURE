import numpy as np
import matplotlib.pyplot as plt
import control

sysg = control.tf(4,[1,5])
print(sysg)

[t,y] = control.step_response(2*sysg) #Multiplicamos por 2 por la amplitud

# plt.figure()
# plt.plot(t,y)
# plt.grid()
# plt.show()

# G(s) = 100 / (s^2 + s + 10)
# U(t) = 5

den = [1,1,10]
pp = np.roots(den)
print(pp)
tau = 1/pp[0].real
print(abs(tau))





# Definir F, G, llamar feedback y luego step response.
# Glc = Y/R = G1F/(1+G1F)

F = control.tf(2,1)
G = sysg

syslc = control.feedback(F*G)
# La consigna es 3
[t,ylc] = control.step_response(3*syslc)
plt.figure()
plt.plot(t,ylc)
plt.xlabel('Tiempo')
plt.ylabel('Salida')
plt.grid()
plt.show()


