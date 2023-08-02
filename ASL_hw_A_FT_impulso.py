import control as co
import matplotlib.pyplot as plt
import numpy as np
from math import *

G00 = co.tf([1, 6, 10, -0.5], [1, 7, 10, 0])
print("G00: ", G00)
G1 = co.tf([1, 0.5], [1, 7, 10])
#print(G1)
G0 = co.tf([3], [1, 2, 3])
#print(G2)
G3 = co.tf([1], [0, 1, 0])
#print(G3)
G2 = co.feedback(G1, 1)
#print(NegFB)

G4 = G1 - G00
print("G04 ", G4)

plt.figure(figsize=(10, 7), facecolor="goldenrod")
t = np.linspace(0, 6, 5000)
t0, y0 = co.step_response(1, t)
t1, y1 = co.impulse_response(G1, t)
t2, y2 = co.impulse_response(G2, t)
t3, y3 = co.impulse_response(G00, t)
t4, y4 = co.impulse_response(G4, t)

#for zeta in np.arange(0, 1.0, 0.2):
#    G4 = co.tf([3], [1, 2*zeta, 3])
#    _, y = co.step_response(G4, t)
#    plt.plot(t, y, label=f" źeta = {zeta:.2}")
#fig, ax = plt.subplots(15,10)
#x = np.linspace(0, 8, 1000
#    (figsize=(8, 6), facecolor="goldenrod")
#plt.plot(t0, y0, label="G0")
#plt.plot(t1, y1, label="Lazo Abierto")
plt.plot(t2, y2, label="Lazo Cerrado")
plt.plot(t3, y3, label="Error Estado Estacionario")

plt.grid()
plt.show()

#plt.plot(t4, y4, label="G4")
#plt.errorbar(t4, y4, xerr=0.2, yerr=0.4)






plt.title('Función de Transferencia / Respuesta a un Impulso')
plt.legend()
plt.xlabel("tiempo(s)")
plt.ylabel("amplitud")
plt.grid()
plt.show()

#t3, y3 = co.step_response(G1, t)
#plt.plot(t3, y3)

#t4, y4 = co.step_response(G2, t)
#plt.plot(t4, y4)




