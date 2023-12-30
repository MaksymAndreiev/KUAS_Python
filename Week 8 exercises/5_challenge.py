import math


def newton(n, eps):
    s = n / 2
    while abs(s * s - n) > eps:
        s = (s + n / s) / 2
    return s


print('n ' + 'newton(n)' + ' ' * 10 + 'math.sqrt(n)' + ' ' * 7 + 'diff')
print('_ ' + '_________' + ' ' * 10 + '____________' + ' ' * 7 + '____')
for n in range(1, 10):
    n_ = newton(n, 0.00001)
    s = math.sqrt(n)
    print(f'{n} ' + ' ' * (18 - len(str(n_))) + f'{n_} ' + ' ' * (
            18 - len(str(s))) + f'{s} ' + ' ' * (18 - len(str(abs(n_ - s)))) + f'{abs(n_ - s)}')
