def print_ascending(d):
    for k, v in sorted(d.items()):
        print(f'{k} {v}')


def is_letter(c: str):
    return c.isalpha() or c.isspace()


print(is_letter('a'))  # True
print(is_letter('B'))  # True
print(is_letter(''))  # True
print(is_letter(','))  # False
print(is_letter('.'))  # False
print('-' * 30)


def depunctuate(word):
    return ''.join(filter(is_letter, word))


with open('text2.txt') as f:
    strings = f.readlines()
    for s in strings:
        print(depunctuate(s))

print('-' * 30)
with open('text2.txt') as f:
    word_freq = {}
    strings = f.readlines()
    for s in strings:
        s = depunctuate(s)
        words = s.split()
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
    print_ascending(word_freq)

