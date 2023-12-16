import sympy as sm

x, y = sm.symbols("x y")
f = (sm.exp(x**3))
res = sm.integrate(f, (x, sm.sqrt(y), 2), (y, 0, 4))
print(res.evalf())
