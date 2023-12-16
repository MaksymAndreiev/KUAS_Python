def palindrome(string):
    for i in range(int(len(string) / 2)):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True


def palindrome1(string):
    return string == string[::-1]


print(palindrome('reviver'))
print(palindrome('level'))
print(palindrome('deed'))
print(palindrome('asd'))
print('-' * 10)
print(palindrome1('reviver'))
print(palindrome1('level'))
print(palindrome1('deed'))
print(palindrome1('asd'))

