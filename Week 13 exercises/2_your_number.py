playing = True
while playing:
    count = 0
    lo = 1
    hi = 100
    while True:
        f = False
        number = (lo + hi) // 2
        print(f'Guess is: {number}')
        guess = input('Am I HIGH, LOW, or CORRECT: ')
        while not f:
            if guess == 'c':
                f = True
            elif guess == 'h':
                hi = number - 1
                f = True
                break
            elif guess == 'l':
                lo = number + 1
                f = True
                break
            else:
                print('Enter h, l or c')
        else:
            break

    correct = False
    while not correct:
        answer = input('Wanna play more? (yes/no)')
        answer = answer.lower()
        if 'yes'.startswith(answer):
            correct = True
        elif 'no'.startswith(answer):
            correct = True
            playing = False
            break
        else:
            print("I don't understand you; please type YES or NO.")
