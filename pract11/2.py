s = "peter piper picked a peck of pickled peppers"


def histogram(seq):
    h = dict()
    for c in s:
        h[c] = h.get(c, 0) + 1
    return h


h = histogram(s)

e2j = {'one': 'ichi', 'two': 'ni', 'three': 'san', 'four': 'yon', 'five': 'go'}
print(e2j)
print('-' * 30)


def reverse_map(d):
    reversed_dictionary = dict()
    for k, v in d.items():
        if v in reversed_dictionary.keys():
            reversed_dictionary[v] = [key for key in reversed_dictionary.get(v)] + [k]
        else:
            reversed_dictionary[v] = k
    return reversed_dictionary


j2e = reverse_map(e2j)
print(j2e)
print('-' * 30)
print(reverse_map(h))
print('-' * 30)
