import numpy as np

x = np.arange(6)
y = np.array([2, 8, 14, 28, 39, 62])

m = len(x)
n = 2

A = np.zeros((n+1, n+1))
B = np.zeros(n+1)
a = np.zeros(n+1)

for row in range(n+1):
    for col in range(n+1):
        if row == 0 and col == 0:
            A[row, col] = m
            continue
        A[row, col] = np.sum(x**(row+col))

    B[row] = np.sum(x**row * y)

a = np.linalg.solve(A, B)

print('The polynomial :')
print('f(x) = \t %f \t' %a[0])

for i in range(1, n+1):
    print('\t %+f x^%d' % (a[i], i))