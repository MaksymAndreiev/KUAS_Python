m = int(input('Length in min: '))
h = m // 60
m = m % (h * 60)
print(f'{h} hours {m} minutes')
