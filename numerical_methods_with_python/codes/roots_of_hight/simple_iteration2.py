from math import sqrt
x = 2

for iteration in range(1, 101):
    xnew = sqrt((5*x-3)/2)
    if abs(xnew - x) < 0.000001:
        break
    else:
        x = xnew
print(iteration, xnew)
print("The root: %0.5f" % xnew)
print("Number of iteration: %d" % iteration)
