for length in range(1, 26):
    words = open("words.txt")
    count = 0
    for line in words:
        word = line.strip()
        if len(word) == length:
            count += 1
    if count > 0:
        # ensure at least one'*'is printed
        count = count + 1000
        print(length, "*" * (count // 1000))
