def avoids(word, letters):
    return not any([letter in word for letter in letters])


print(avoids('cat', 'ct'))
print(avoids('dog', 'ct'))
print(avoids('elephant', 'ct'))
print(avoids('chimanze', 'ct'))
print(avoids('mongoose', 'ct'))

forbidden_letters = input('Forbidden letters: ')
counter = 0

with open('words.txt') as f:
    strings = f.readlines()
    for s in strings:
        s = s.strip('\n')
        if avoids(s, forbidden_letters):
            counter += 1


print(counter)
