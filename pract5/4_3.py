import math
import turtle


def plot_function(f):
    turtle.up()
    turtle.goto(-200, 100 * f(-2 * math.pi))
    turtle.down()

    for x in range(-200, 201):
        angle = x / 100 * 2 * math.pi
        y = 100 * f(angle)
        turtle.goto(x, y)

    turtle.up()
    turtle.goto(-200, 100 * f(-2 * math.pi))
    turtle.down()

    for x in range(-200, 201):
        angle = x / 100 * 2 * math.pi
        y = 100 * f(angle)
        turtle.goto(x, y)


def f(angle):
    return math.sin(angle) + 1 / 3 * math.sin(3 * angle)


turtle.speed(1)  # Adjust the speed if needed
plot_function(f)
turtle.done()