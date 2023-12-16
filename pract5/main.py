import turtle


def squareCircles(length, radius):
    turtle.forward(length / 2)
    turtle.right(90)

    for _ in range(4):
        turtle.left(45)
        turtle.circle(radius)
        turtle.right(45)
        turtle.forward(length)
        turtle.right(90)

    turtle.done()


my_turtle = turtle.Turtle()

my_turtle.speed(20)

squareCircles(200, 50)

my_turtle.hideturtle()

turtle.exitonclick()
