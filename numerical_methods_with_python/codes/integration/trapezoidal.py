import numpy as np

f = lambda x: x*np.sin(x)

a = 0
b = np.pi/2
n = 5

h = (b-a)/n

S = 0.5*(f(a) + f(b))

for i in range(1, n):
    S += f(a + i*h)

Integral = h * S

print("Integral: %f" % Integral)