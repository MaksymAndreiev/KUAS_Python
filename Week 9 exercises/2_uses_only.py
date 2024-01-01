def uses_only(word, letters):
    return all([letter in letters for letter in word])


def uses_all(word, letters):
    return uses_only(letters, word)


print(uses_only('appeal', 'aple'))
print(uses_only('apple', 'aple'))
print(uses_only('apples', 'aple'))
print(uses_only('lapel', 'aple'))
print(uses_only('palpable', 'aple'))
print(uses_only('palpable', 'abple'))

using_letters = 'acefhlo'

with open('words.txt') as f:
    strings = f.readlines()
    for s in strings:
        s = s.strip('\n')
        if uses_only(s, using_letters):
            print(s)

print('-' * 30)
using_letters = 'aeiou'
using_letters = 'aeiouy'

counter = 0
with open('words.txt') as f:
    strings = f.readlines()
    for s in strings:
        s = s.strip('\n')
        if uses_all(s, using_letters):
            counter += 1

print(counter)
