# def print_num(n):
#     s = str(n)
#     print(s[-1])
#     print(s[:-1])


# def print_num(n):
#     s = str(n)
#     print(s[-1])
#     if len(s) > 1:
#         return print_num(int(s[:-1]))
#     else:
#         return


# def print_num(n):
#     s = str(n)
#     print(s[0])
#     if len(s) > 1:
#         return print_num(int(s[1:]))
#     else:
#         return


# def print_num(n):
#     s = str(n)
#     print(s[0], end='')
#     if len(s) > 1:
#         return print_num(int(s[1:]))
#     else:
#         return


# def print_num(n, base):
#     # print(np.base_repr(n, base))
#     if n == 0:
#         return [0]
#     digits = []
#     while n:
#         digits.append(int(n % base))
#         n //= base
#     print(''.join([str(digit) for digit in digits[::-1]]))
#     return digits[::-1]

# def print_num(n, base, w):
#     # print(np.base_repr(n, base))
#     if n == 0:
#         return [0]
#     digits = []
#     while n:
#         digits.append(int(n % base))
#         n //= base
#     digits_string = ''.join([str(digit) for digit in digits[::-1]])
#     leading_zero = f'%0{w}d'
#     print(leading_zero % (int(digits_string)))
#     return digits[::-1]


# def print_num(n, base, w, p):
#     if n == 0:
#         return [0]
#     digits = []
#     while n:
#         digits.append(int(n % base))
#         n //= base
#     digits_string = ''.join([str(digit) for digit in digits[::-1]])
#     print(p * (w - len(digits_string)) + digits_string)
#     return digits[::-1]

def print_num(n, base=10, w=1, p=' '):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    digits_string = ''.join([str(digit) for digit in digits[::-1]])
    print(p * (w - len(digits_string)) + digits_string)
    return digits[::-1]


# print_num(3210)

# print_num(3210, 10)
# print_num(255, 8)
# print_num(42, 2)

# print_num(3210, 10, 0)
# print_num(255, 8, 3)
# print_num(255, 8, 4)
# print_num(42, 2, 8)

print_num(3210, 10, 8, '.')
print_num(255, 8, 8, ' ')
print_num(42, 2, 8, '0')

# print_num(3210)
