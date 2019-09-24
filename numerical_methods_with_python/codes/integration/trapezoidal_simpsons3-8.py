import numpy as np

f = lambda x: x*np.sin(x)

a = 0
b = np.pi/2
n = 6

h = (b-a)/n

S = (f(a) + f(b))

for i in range(1, n, 3):
    S += 3*f(a + i*h) + f(a + (i+1)*h)

for i in range(3, n, 3):
    S += 2*f(a + i*h)

Integral = h/3 * S

print("Integral: %f" % Integral)