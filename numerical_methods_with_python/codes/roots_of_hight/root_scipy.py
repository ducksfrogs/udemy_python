from scipy.optimize import newton, bisect, fsolve, root

f = lambda x: 2*x**2 -5*x +3

print(newton(f, 0))
print(newton(f,2))

print(bisect(f, 0, 1.2))
print(bisect(f, 1.1, 1.8))

print(fsolve(f, 0))

x0 = [-1, 0, 1, 2,3,4]
print(fsolve(f, x0))


print(root(f, 0).x)
print(root(f, x0).x)

