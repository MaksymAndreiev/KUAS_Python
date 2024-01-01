def is_monotonic(word):
    return word == ''.join(sorted(word))


def is_double(word, pos):
    return word[pos] == word[pos + 1]


print(is_monotonic('beefily'))
print(is_monotonic('beefiness'))

counter = 0

with open('words.txt') as f:
    strings = f.readlines()
    for s in strings:
        s = s.strip('\n')
        if is_monotonic(s):
            counter += 1

print(counter)

with open('words.txt') as f:
    strings = f.readlines()
    for s in strings:
        s = s.strip('\n')
        for i in range(len(s) - 6):
            if is_double(s, i) and is_double(s, i + 2) and is_double(s, i + 4):
                print(s)
