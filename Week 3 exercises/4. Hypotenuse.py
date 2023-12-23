import math

a = int(input('a:'))
b = int(input('b:'))
c = math.sqrt(a ** 2 + b ** 2)
p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f'hypotenuse {c} area {S}')
