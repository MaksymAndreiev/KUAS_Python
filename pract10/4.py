def includes(sequence, target):
    first = 0
    last = len(sequence) - 1
    while first <= last:
        mid = (first + last) // 2
        if target == sequence[mid]:
            return True
        elif target < sequence[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


with open("words.txt", "r") as file:
    words = [word.strip() for word in file]

interlock_pairs_2 = []
interlock_pairs_3 = []

for word in words:
    if len(word) > 5:
        a = word[::2]
        b = word[1::2]
        if includes(words, a) and includes(words, b):
            interlock_pairs_2.append((a, b))
    if len(word) > 8:
        a = word[::3]
        b = word[1::3]
        c = word[2::3]
        if includes(words, a) and includes(words, b) and includes(words, c):
            interlock_pairs_3.append((a, b, c))

for pair in interlock_pairs_2:
    print(pair)
print(len(interlock_pairs_2))
for pair in interlock_pairs_3:
    print(pair)
print(len(interlock_pairs_3))
