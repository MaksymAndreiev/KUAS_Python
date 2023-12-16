import random
import turtle
from math import pow, sqrt

turtle.setup(500, 500)
turtle.tracer(0, 0)
turtle.hideturtle()
turtle.up()
n = 2000
i = 0
tally = 0
s = 0
inside = False
while i < n:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print()
    if sqrt(pow(x, 2) + pow(y, 2)) < 1:
        inside = True
        tally += 1
    else:
        inside = False
    turtle.goto(x * 200, y * 200)
    turtle.dot(10, "black" if inside else "red")
    turtle.update()
    turtle.goto(-200 + s, 225)
    turtle.dot(5, "green")
    s += 0.2
    i += 1

print(tally / n * 4)
