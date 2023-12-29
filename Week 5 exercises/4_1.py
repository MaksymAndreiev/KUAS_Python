import math
import turtle

import numpy as np

t = turtle.Turtle()
t.speed(10)


def triangle(length, angle, full, left):
    # angle_sin = math.radians(angle)
    diagonal = np.linalg.norm([length, length / 2])

    # base_half_length = diagonal * math.sin(angle_sin / 2)
    base_half_length = length / 2

    t.pendown()
    t.left(90)
    if full:
        t.left(angle)
        t.forward(length)
        t.left(90 + angle)
        t.forward(diagonal)
    elif left:
        t.forward(length)
        t.right(90)
        t.forward(base_half_length)
        t.right(90+angle)
        t.forward(diagonal)
    else:
        t.right(180+angle)
        t.forward(base_half_length)
        t.right(90)
        t.forward(length)


def figure(length):
    angle = math.degrees(math.atan(1/2))
    triangle(length, angle, False, True)
    triangle(length, angle, True, None)
    triangle(length, angle, False, False)


figure(200)

t.hideturtle()

turtle.done()
