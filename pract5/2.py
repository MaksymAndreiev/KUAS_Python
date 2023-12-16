import turtle


def arc(radius, angle):
    turtle.circle(radius, angle)


def petal(radius, angle):
    for _ in range(2):
        arc(radius, angle)
        turtle.left(180 - angle)


def flower(radius, angle, npetals):
    angle_increment = 360 / npetals
    for _ in range(npetals):
        petal(radius, angle)
        turtle.left(angle_increment)


turtle.speed(20)
flower(100, 60, 6)

turtle.done()
