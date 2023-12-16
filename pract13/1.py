import random

playing = True
while playing:
    count = 0
    number = random.randint(1, 100)
    while True:
        guess = int(input('Input number: '))
        count += 1
        if guess < number:
            print('too low')
            continue
        elif guess > number:
            print('too high')
            continue
        else:
            print(f'correct: {number}')
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
