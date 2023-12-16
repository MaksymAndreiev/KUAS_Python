def find_letter(word, letter):
    i = 0
    while i < len(word):
        if word[i] == letter:
            return i
        i += 1
    else:
        return None


word = 'abcdef'
print(find_letter(word, 'a'))
print(find_letter(word, 'f'))
print(find_letter(word, 'z'))


def find_letter1(word, letter):
    for i in range(len(word)):
        if word[i] == letter:
            return i
    else:
        return None


print('-'*30)
print(find_letter1(word, 'a'))
print(find_letter1(word, 'f'))
print(find_letter1(word, 'z'))


def count_letter(word, letter):
    count = 0
    for c in word:
        if c == letter:
            count += 1
    return count


word = 'bananas'

print('-'*30)
print(count_letter(word, 'a'))
print(count_letter(word, 'n'))
print(count_letter(word, 'z'))


def count_letters(word, letters):
    count = 0
    for c in word:
        for l in letters:
            if c == l:
                count += 1
    return count


print('-'*30)
print(count_letters(word, 'a'))
print(count_letters(word, 'ban'))
print(count_letters(word, 'banz'))
print(count_letters(word, 'bans'))