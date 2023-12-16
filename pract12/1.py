import random


def file_words(file_name):
    all_words = []
    for line in open(file_name):
        all_words.extend([c for c in line.split() if c.isalpha()])
    return all_words


words = file_words('text3.txt')

for i in range(20):
    print(f'{i + 1}. {random.choice(words)}')
