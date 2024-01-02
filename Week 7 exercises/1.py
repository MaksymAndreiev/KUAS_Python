def print_each(num):
    i = 0
    while i < num:
        print(i)
        i += 1


def print_each1(string):
    i = 0
    while i < len(string):
        print(string[i])
        i += 1


def print_each2(x, n):
    i = n
    while i < len(x):
        print(x[i])
        i += 1


def print_each3(x, n=0):
    print_each2(x, n)


print_each(10)
print('-'*30)
print_each1('hello')
print('-'*30)
print_each2('goodbye', 4)
print('-'*30)
print_each3('goodbye')
