f = lambda x: 0.1 * x ** 5 - 0.2 * x ** 3 + 0.1 * x - 0.2
h = 0.05
x = 0.1

# Forword deffence appromiaton
dff1 = (f(x + h) - f(x)) / h
dff2 = (f(x + 2 * h) - 2 * f(x + h) + f(x)) / h ** 2

print('f\(%f) = %f' % (x, dff1))
print('f\(%f) = %f' % (x, dff2))

# Central Forword deffence appromiaton
dfc1 = (f(x + h) - f(x - h)) / 2 * h
dfc2 = (f(x + h) - 2 * f(x) + f(x - h)) / h ** 2

print('f\`(%f) = %f' % (x, dfc1))
print('f\`\`(%f) = %f' % (x, dfc2))

# Forword deffence appromiaton
dff1 = (f(x + h) - f(x)) / h
dff2 = (f(x + 2 * h) - 2 * f(x + h) + f(x)) / h ** 2

print('f\(%f) = %f' % (x, dff1))
print('f\(%f) = %f' % (x, dff2))
