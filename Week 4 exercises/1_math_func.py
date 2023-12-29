from math import pi, sqrt


def circle_area(r):
    return pi * r ** 2


def sphere_volume(r):
    return 4 / 3 * pi * r ** 3


def triangle_area(a, b):
    return 1 / 2 * a * b


def hypotenuse(a, b):
    return sqrt(a ** 2 + b ** 2)


def point_distance(x1, y1, x2, y2):
    return hypotenuse(x1-x2, y1-y2)
    # return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


print('Circle area')
print(circle_area(1))
print(circle_area(2))
print(circle_area(3))

print('Sphere vol')
print(sphere_volume(1))
print(sphere_volume(2))
print(sphere_volume(3))

print('Triangle area')
print(triangle_area(1, 1))
print(triangle_area(2, 2))
print(triangle_area(3, 4))

print('Hypotenuse')
print(hypotenuse(1, 1))
print(hypotenuse(3, 4))
print(hypotenuse(5, 12))

print('Point dist')
print(point_distance(0, 0, 1, 1))
print(point_distance(3, 4, 6, 8))
print(point_distance(8, 6, 4, 3))
