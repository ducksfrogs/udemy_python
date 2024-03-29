#2x**2 -5x +3 =0
#root is 1.5, 1.0


x1 = 1.1
x2 = 1.9

y1 = 2*x1**2 -5*x1 +3
y2 = 2*x2**2 -5*x2 +3

if y1 *y2 > 0:
    print('The root is not with the given interval')
    exit

for bisection in range(1, 101):
    xh = (x1 + x2) /2
    yh = 2*xh**2 -5*xh +3

    y1 = 2*x1**2 -5*x1 +3

    if abs(y1) < 1.0E-6:
        break

    elif y1 * yh < 0:
        x2 = xh

    else:
        x1 = xh

print('Bisections : %d: ' % bisection)
print('The root :  %0.5f' % x1)

