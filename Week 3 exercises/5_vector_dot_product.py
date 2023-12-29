import numpy as np

a = input('vector A: ')
A = eval(a)
b = input('vector B: ')
B = eval(b)
print(a + ' x ' + b + ' = ' + str(np.inner(A, B)))
