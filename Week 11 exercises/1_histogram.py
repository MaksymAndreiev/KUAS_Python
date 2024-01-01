s = "peter piper picked a peck of pickled peppers"


def histogram(seq):
    h = dict()
    for c in s:
        # if not c in h:
        #     h[c] = 0
        # h[c] = h[c] + 1
        h[c] = h.get(c, 0) + 1
    return h
    # for c in h:
    #     print(c, '*' * h[c])


h = histogram(s)
print(h)
print('-' * 30)


def print_ascending(d):
    for k, v in sorted(d.items()):
        print(f'{k} {v}')


print_ascending({"b": 1, "c": 2, "a": 3})
print('-' * 30)


def print_histogram(d):
    for k, v in sorted(d.items()):
        print(k, '*' * v)


print_histogram({"b": 1, "c": 2, "a": 3})
print('-' * 30)
print_histogram(h)
print('-' * 30)
