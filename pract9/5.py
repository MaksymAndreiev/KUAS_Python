with open('text.txt') as f:
    strings = f.readlines()
    i = 1
    for s in strings:
        s = s.strip('\n')
        print(f'Line {i}: {len(s.split())}')
        i += 1

with open('text.txt') as f:
    strings = f.readlines()
    print(f'Number of lines: {len(strings)}')
    all_words = []
    all_characters = []
    for s in strings:
        s = s.strip('\n')
        all_words.extend(s.split())
    for word in all_words:
        all_characters.extend([letter for letter in word])
    print(f'Number of words: {len(all_words)}')
    print(f'Number of characters: {len(all_characters)}')

