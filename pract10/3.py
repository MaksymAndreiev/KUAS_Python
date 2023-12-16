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

reverse_pairs = []

for word in words:
    if includes(words, word[::-1]):
        reverse_pairs.append((word, word[::-1]))

for pair in reverse_pairs:
    print(pair)
