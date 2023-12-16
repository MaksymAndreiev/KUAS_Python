def rotate(word, n):
    new_word = []
    for c in word:
        if 'a' <= c <= 'z':
            pos = n + ord(c) - ord('a')
            pos %= 26
            new_c = chr(pos + 97)
            new_word.append(new_c)
        elif 'A' <= c <= 'Z':
            pos = n + ord(c) - ord('A')
            pos %= 26
            new_c = chr(pos + 65)
            new_word.append(new_c)
        else:
            new_word.append(c)
    return ''.join(new_word)


print(rotate('This is a message that has been encoded.', 13))
print(rotate(rotate('This is a message that has been encoded.', 13), -13))
