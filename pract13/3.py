import math
from turtle import *

function_name = ['sin(x)', 'cos(x)']
minimum = [-2 * math.pi, -math.pi]
maximum = [2 * math.pi, math.pi]

f_index = 0
min_index = 0
max_index = 0


def function(x):
    return math.sin(x) if f_index in (0, -2) else math.cos(x)


def menu(i1, i2, i3):
    return f'1) change function: {function_name[i1]}\n' \
           f'2) change minimum: {minimum[i2]}\n' \
           f'3) change maximum: {maximum[i3]}\n' \
           f'4) plot function\n' \
           f'5) exit'


setup(500, 500)  # create a 500 x 500 window for plotting

while True:
    print(menu(f_index, min_index, max_index))
    choice = int(input('choice: '))
    if choice == 1:
        if -2 < f_index < 2:
            f_index -= 1
        else:
            f_index += 1
        print(f'new function: {function_name[f_index]}')
    elif choice == 2:
        min_index -= 1
        print(f'new minimum: {minimum[min_index]}')
    elif choice == 3:
        max_index -= 1
        print(f'new maximum: {maximum[max_index]}')
    elif choice == 4:
        xmin = minimum[min_index]
        xmax = maximum[max_index]
        ymin = function(xmin)  # output value at first point
        ymax = ymin

        # calculate the actual range of output values ymin to ymax
        xscale = (xmax - xmin) / 400  # scale input range to 400 pixels wide

        for wx in range(401):  # window coordinates
            x = xmin + wx * xscale  # function coordinates
            y = function(x)  # function coordinates
            ymin = min(ymin, y)  # minimum y seen so far
            ymax = max(ymax, y)  # maximum y seen so far

        if ymin == ymax:  # y is constant
            ymin = ymin - 1  # avoid divide by zero below

        yscale = 400 / (ymax - ymin)  # scale output range to 400 pixels high

        up()  # do not draw a line to the first point

        for wx in range(401):  # window coordinates
            x = xmin + wx * xscale  # function coordinates
            y = function(x)  # function coordinates
            wy = (y - ymin) * yscale  # window coordinates
            goto(-200 + wx, -200 + wy)  # draw line to next function point
            down()
            # draw lines starting from first point
        up()
        goto(0, 0)  # park the turtle back at the origin

        # mainloop()
    elif choice == 5:
        exit(1)
    else:
        print('Enter 1-5')
