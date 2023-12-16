# def even_odd(n):
#     if n % 2:
#         return 'odd'
#     else:
#         return 'even'


def is_divisible_by(n, m):
    if n % m == 0:
        return True
    else:
        return False


def even_odd(n):
    if is_divisible_by(n, 2):
        return 'even'
    else:
        return 'odd'


def age_group(age):
    if age < 0:
        return None
    elif age < 6:
        return 'baby'
    elif age < 18:
        return 'school'
    elif age < 22:
        return 'student'
    elif age < 65:
        return 'employed'
    else:
        return 'retired'


for i in range(10):
    print(i, even_odd(i))

for i in range(101):
    if is_divisible_by(i, 7):
        print(i)

print(age_group(4))
print(age_group(14))
print(age_group(20))
print(age_group(34))
print(age_group(70))
