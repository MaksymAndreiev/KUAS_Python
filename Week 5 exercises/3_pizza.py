import math
import turtle

t = turtle.Turtle()
t.speed(30)


def triangle(length, angle):
    angle_sin = math.radians(angle)

    base_half_length = length * math.sin(angle_sin / 2)

    t.pendown()

    t.right(angle / 2)
    t.forward(length)
    t.left(90 + angle / 2)
    t.forward(2 * base_half_length)
    t.left(90 + angle / 2)
    t.forward(length)


# triangle(200, 60)


def pizza(length, number):
    angle = 360 / number
    for i in range(number):
        triangle(length, angle)
        t.right(90+angle)


pizza(200, 30)

t.hideturtle()

turtle.done()
