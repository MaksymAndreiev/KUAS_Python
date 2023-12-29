def double(n=1):
    return 2 * n


def pad(n: str or int, width=8, *kwargs: str):
    character = kwargs[0]
    if isinstance(n, str):
        return character * (width - len(n)) + n
    elif isinstance(n, int):
        return character * (width - len(str(f'{n:02d}'))) + f'{n:02d}'


def twice(f, *args):
    f(*args)
    f(*args)


print(double('2'))
print(double(2))
print(double())

print(pad('hello', 10, ' '))
print(pad('', 2, '0'))
print(pad(4, 2, '0'))
print(pad(42, 2, '0'))
print(pad('', 8, '-'))
print(pad(123, 8, '.'))
print(pad(456789, 8, '0'))

twice(twice, print, 'hello')
