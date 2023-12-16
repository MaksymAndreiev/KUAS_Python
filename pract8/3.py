import numpy as np

input_numbers = []
while True:
    s = input('n: ')
    if s == 'stop':
        break
    n = int(s)
    input_numbers.append(n)
    print(n * 2)
    print(f'total : {sum(input_numbers)}')
    print(f'average : {np.average(input_numbers)}')
