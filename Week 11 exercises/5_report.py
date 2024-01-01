with open('text2.txt') as f:
    text = f.read()
    print(text.count('\n'))
    print(len(text.split()))
    print(len(''.join(text)))
