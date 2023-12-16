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

# while not prefix[0]

prefix = random.choice(list(markov.keys()))

print(' '.join(prefix), end=" ")

for i in range(20):
    suffixes = markov.get(prefix, [])
    if suffixes:
        next_word = random.choice(suffixes)

        print(next_word, end=" ")

        prefix = prefix[1:] + (next_word,)
    else:
        break
