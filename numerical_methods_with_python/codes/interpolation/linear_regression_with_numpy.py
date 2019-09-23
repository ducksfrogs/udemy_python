import numpy as np

x = np.array([3, 4, 5, 6, 7, 8])
y = np.array([0, 7, 17, 26, 35, 45])
n = len(x)
a = (np.mean(y)*np.sum(x**2) - np.mean)
sumx = sumxy = sumx2 = sumy = 0

sumx = np.sum(x)
sumy = np.sum(y)
sumx2
sumxy

xm = sumx / n
ym = sumy / n

a = (ym*sumx2 - xm*sumxy)/(sumx2 - n*xm**2)
b = (sumxy - xm*sumy)/(sumx2 - n*xm**2)

print('The straight line equation')
print('y = (%.3f) + (%.3f)x' % (a,b))
