from scipy.signal import lti
#import conda as con
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import control as co
G00 = co.tf([1, 6, 10, -0.5], [1, 7, 10, 0])
print("G00: ", G00)
G1 = co.tf([1, 0.5], [1, 7, 10])
print(G1)
G0 = co.tf([3], [1, 2, 3])
# print(G2)
G3 = co.tf([1], [0, 1, 0])
# print(G3)
G2 = co.feedback(G1, 1)
# print(NegFB)
G4 = G1 - G00
#print("G00 ", G00)



plt.figure(figsize=(10, 7), facecolor="cadetblue")
t = np.linspace(0.1, 10, 5000)
t0, y0 = co.step_response(1, t)
t1, y1 = co.step_response(G1, t)
#t2, y2 = co.step_response(G2, t)
t3, y3 = co.impulse_response(G4, t)

plt.plot(t1, y1, label="Lazo Cerrado")
plt.plot(t3, y3, label="Error Estado Estacionario")
plt.plot(t0, y0, label="Escalón")
plt.title('Función de Transferencia / Respuesta a un Escalon')
plt.legend()
plt.xlabel("tiempo(s)")
plt.ylabel("amplitud")
plt.grid()
plt.show()


sys2 = signal.lti([1, 0.5], [1, 7, 10])  # H(s) = (s - 0.5) / (s ** 2 + 7 * s + 10)
w, H = signal.freqresp(sys2)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6), facecolor="cadetblue")
ax1.plot(H.real, H.imag)
ax1.plot(H.real, -H.imag)
ax2.plot(sys2.zeros.real, sys2.zeros.imag, 'o')
ax2.plot(sys2.poles.real, sys2.poles.imag, 'x')
plt.title('Función de Transferencia / Respuesta a un Escalon')
plt.legend()
plt.xlabel("tiempo(s)")
plt.ylabel("amplitud")
plt.grid()
plt.show()

m = 1  # kg
b = 2  # Ns / m
sys_car = signal.lti(-0.5, [m, b])
t, y = signal.step2(sys_car)  # Respuesta a escalón unitario
plt.plot(t, 2250 * y)  # Equivalente a una entrada de altura 2250
plt.legend()
plt.xlabel("tiempo(s)")
plt.ylabel("amplitud")
plt.grid()
plt.show()

num = [1, 0.5]
den = [1, 7, 10]
sys_ol = co.tf(num,den) #Lazo abierto
sys_cl = co.feedback(sys_ol,1)
print(sys_ol)
print(sys_cl)

plt.figure(figsize=(10, 7), facecolor="red")
plt.title('Función G(s) / Respuesta a un Escalon')
plt.legend()
plt.xlabel("tiempo(s)")
plt.ylabel("amplitud")
plt.grid()

t,yol = co.step_response(sys_ol)
plt.plot(t, yol)

t,ycl = co.step_response(sys_cl)
plt.plot(t, ycl)

plt.plot(t, yol, label="Lazo Abierto")
plt.plot(t, ycl, label="Lazo Cerrado")

plt.show()
# t3, y3 = co.step_response(G1, t)
# plt.plot(t3, y3)

# t4, y4 = co.step_response(G2, t)
# plt.plot(t4, y4)


