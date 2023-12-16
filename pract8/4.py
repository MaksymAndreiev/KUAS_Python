def newton(n, eps):
    s = n / 2
    while abs(s * s - n) >= eps:
        s = (s + n / s) / 2
    return s


print(newton(100, 0.1))
print(newton(1, 0.01))
print(newton(2, 0.00001))
print(newton(10, 0.00001))
