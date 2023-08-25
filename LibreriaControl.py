import numpy as np
import control as co

G1 = co.tf([5, 7, 9], [1, 8, 6, 2])
G2 = 5*co.tf(np.poly([-2, -5]), np.poly([-4, -5, -9]))
print(G1)
print (G2)