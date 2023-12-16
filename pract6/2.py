def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def sum_of_count(n):
    if n > 0:
        return n + sum_of_count(n - 1)
    else:
        return 0


def fibonacci(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        return fibonacci(m - 1) + fibonacci(m - 2)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print('-' * 5 + 'Factorial' + '-' * 5)
print(factorial(0))
print(factorial(3))
print(factorial(6))

print('-' * 5 + 'Sum' + '-' * 5)
for i in range(10):
    print(sum_of_count(i))

print('-' * 5 + 'Fibonacci' + '-' * 5)
print(fibonacci(7))

print('-' * 5 + 'GCD' + '-' * 5)
print(gcd(24, 42))
