import numpy as np

x = np.array([3, 4, 5, 6, 7, 8])
y = np.array([0, 7, 17, 26, 35, 45])
n = len(x)
a = (np.mean(y)*np.sum(x**2) - np.mean(x)* np.sum(x*y))/(np.sum(x**2)-n*np.mean(x)**2)
b = (np.sum(x*y) - np.mean(x)* np.sum(y))/(sum(x**2)-n*np.mean(x)**2)

print('The straight line equation')
print('y = (%.3f) + (%.3f)x' % (a,b))
