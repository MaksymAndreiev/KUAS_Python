import random


def file_words(file_name):
    all_words = []
    file = open(file_name)
    for line in file:
        all_words.extend([c for c in line.split() if c.isalpha()])
    return all_words


words = file_words('text4.txt')

markov = {}
for i in range(len(words) - 2):
    prefix = tuple(words[i:i + 2])
    suffix = words[i + 2]
    markov.get(prefix, [])
    markov[prefix] = markov.get(prefix, []) + [suffix]

key = random.choice(list(markov.keys()))
while not key[0][0].isupper():
    key = random.choice(list(markov.keys()))

print(' '.join(key), end=" ")

while True:
    suffixes = markov.get(key, [])
    if suffixes:
        next_word = random.choice(suffixes)
        print(next_word, end=" ")
        if next_word.endswith('.'):
            break
        key = key[1:] + (next_word,)
    else:
        break
