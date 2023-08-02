from scipy.signal import lti
import numpy as np
import matplotlib.pyplot as plt
import control as co
num = [2]
den = [2, 1]
sys = lti(num, den)
print("sys: ", sys)
t, y = sys.step()
plt.plot(t, y)
plt.plot(0,t[-1],[1]*2,label="referencia")
plt.show()


plt.rcParams['figure.figsize'] = [23, 10]
plt.rcParams['font.size'] = 24
G1 = co.tf([1, 0.5], [1, 2, 3])
G2 = co.tf(np.poly((1, 0.5)), np.poly([1, 2]))
Gn = ((np.poly([1, 2])) * (np.poly([1, 5])))
print(G1)
print(G2)
print("Gn=", Gn)
G3 = co.minreal(G2)
print(G3)
G4 = G1 + G2
print(G4)
G5 = G1 * G2
print(G5)
G6 = G1 / G2
print(G6)

print()
G7 = co.feedback(G1, G2)
print()
print()
print("FeedBack", G1, G7)


print()
G8 = G1_ss = co.tf2ss(G1)
print()
print()
print("TF to State Space", G1, G8)

print()
G9 = G2_ss = co.tf2ss(G2)
print()
print()
print("TF to State Space", G2, G9)

A = [[0, 1, 0], [0, 0, 1], [-1, -2, -3]]
B = [[0], [0], [1]]
C = [1, 0, 0]
D = 0
sys7 = co.ss(A, B, C, D)
print()
print()
print("State Space Model", sys7)
sys7_tf = co.ss2tf(sys7)
print()
print()
print("State Space Model", sys7_tf)

t = np.linspace(0, 10, 1000)
t1, y1 = co.impulse_response(G1, t)

plt.plot(t1, y1)
plt.xlabel("time(s)")
plt.ylabel("amplitud(s)")
plt.grid()
