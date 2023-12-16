import turtle

t = turtle.Turtle()
# turtle.tracer(100.0)
# turtle.update()
s = turtle.Screen()
s.setup(800, 600)
t.penup()
t.backward(400)
t.pendown()


def koch(x):
    if x > 3:
        for direction in [60, -120, 60, 0]:
            koch(x / 3)
            t.left(direction)
    else:
        t.forward(x)


def snowflake(x):
    for i in range(3):
        koch(x)
        t.right(120)


# koch(729)
t.penup()
t.forward(400)
t.pendown()
snowflake(75)
turtle.done()
