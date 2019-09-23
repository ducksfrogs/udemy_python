#2x**2 -5x +3 =0
#root is 1.5, 1.0


y = lambda x: 2*x**2 -5*x +3
x1 = float(input('Enter the value of X1: '))
x2 = float(input('Enter the value of X2: '))

y1 = y(x1)
y2 = y(x2)

if y1 *y2 > 0:
    print('The root is not with the given interval')
    exit

for bisection in range(1, 101):
    xh = (x1 + x2) /2
    yh = y(xh)

    y1 = y(x1)

    if abs(y1) < 1.0E-6:
        break

    elif y1 * yh < 0:
        x2 = xh

    else:
        x1 = xh

print('Bisections : %d: ' % bisection)
print('The root :  %0.5f' % x1)

