import math
import turtle

sc = turtle.Screen()
sc.setworldcoordinates(0, -2, 3600, 2)

t = turtle.Turtle()
t.speed(100)


def sin_draw():
    t.pendown()
    for x in range(3600):
        y = math.sin(math.radians(x))
        t.goto(x, y)


sin_draw()

t.hideturtle()

turtle.done()
