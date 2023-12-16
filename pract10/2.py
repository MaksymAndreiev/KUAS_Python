from random import randint


def randlist(n, i, j):
    return [randint(i, j) for k in range(n)]


print(randlist(10, 1, 5))


def has_duplicates(l):
    return any(l[i] in l[i + 1:] for i in range(len(l)))


print(has_duplicates([1, 2, 3]))  # False
print(has_duplicates([1, 1, 2, 3]))  # True
print(has_duplicates([1, 2, 2, 3]))  # True
print(has_duplicates([1, 2, 3, 3]))  # True
print(has_duplicates([1, 2, 3, 1]))  # True


def stats(n):
    c = 0
    for i in range(100000):
        l = randlist(n, 1, 365)
        if has_duplicates(l):
            c += 1
    return c/1000


print(stats(23))
print(stats(41))
