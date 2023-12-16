def decorator(func):
    def inner(n):
        if isinstance(n, int):
            if n >= 0:
                res = func(n)
                return res
            else:
                print('n is < 0')
                return None
        else:
            print('n is not int')
            return None

    return inner


@decorator
def factorial(n):
    print(f'factorial {n}')
    if n == 0:
        print('returning 1')
        return 1
    print(f'returning {n * factorial(n - 1)}')
    return n * factorial(n - 1)


print(factorial(5))
print(factorial(-5))
print(factorial('5'))
