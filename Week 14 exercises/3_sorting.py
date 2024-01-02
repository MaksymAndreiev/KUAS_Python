import random


def random_list(n):
    return [random.randint(0, 10) for _ in range(n)]


def sort_list(l):
    for i in range(len(l) - 1):
        s = i
        for j in range(i+1, len(l)):
            if l[j] < l[s]:
                s = j
        t = l[i]
        l[i] = l[s]
        l[s] = t
    return l


num_lists = 10

for _ in range(20):
    l = random_list(num_lists)
    print(l, end="\t")
    sort_list(l)
    print(l)
    assert(l == sorted(l))