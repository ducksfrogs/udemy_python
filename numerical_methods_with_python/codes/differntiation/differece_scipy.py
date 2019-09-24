import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

f = lambda x: 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
x = np.linspace(0, 1, 11)
h = 0.01
dfc1 = derivative(f, x, h, 1)
dfc2 = derivative(f, x, h, 2)

plt.plot(x, f(x), '-k', x, dfc1, '--b', x, dfc2, '-.r')
plt.grid()
plt.show()

