# Information Processing 1 — Week 5 exercises

## 1 Drawing geometric shapes

During the class we created a function called `circle(radius)`. Use that to write another function
called `squareCircles(length, radius)` that draws a square with sides of the given `length` and four circles of the given
radius that just touch
the corners of the square as shown in the figure.

Hint: Develop your function by incrementally. While drawing a square, draw a circle at the end of each edge. Then figure
out how to orient the circles correctly. Alternatively, start by drawing just the first circle and the first line. When
they look correct, repeat the code four times to draw the entire figure.

![image](https://github.com/MaksymAndreiev/KUAS_Python/assets/29687267/06883638-d12d-4ee6-b668-4468dfba28d3)

## 2 Drawing ﬂowers

During the class we created a function called `arc(radius, angle)`.

**Part 1** Use the `arc(radius, angle)` function to write another function called `petal(radius, angle)` that draws a
single flower ‘petal’.

Hint: Ensure that the final position and final heading of the pen, after drawing the petal, are the same as the starting
position and heading. In other words, if you call petal twice it should overwrite itself.

![image](https://github.com/MaksymAndreiev/KUAS_Python/assets/29687267/8cf73195-d94c-4eed-9762-c601321f26bf)


**Part 2** Write a function called `flower(radius, angle, npetals)` that draws a flower with `npetals` petals each of
which
has the given radius and `angle`.

![image](https://github.com/MaksymAndreiev/KUAS_Python/assets/29687267/a3c7f053-a856-4dc5-abd7-a6e1decb7d57)


## 3 Drawing pizzas

**Part 1** Write a function `triangle(length, angle)` that
draws an *isosceles* triangle whose equal sides are the given length and separated by the given angle.

Hints: The problem is easier to solve if you think of the triangle as two right-angled triangles back-to-back, both
having a hypotenuse of the given length. You can then use `length` \* `math.sin(angle / 2)` to calculate half the length
of
the base of the triangle. Don’t forget that `angle` must be converted to radians (not shown here) before you use it in
the
`sin()` function.

![image](https://github.com/MaksymAndreiev/KUAS_Python/assets/29687267/b56b2819-4141-4219-a631-62c225418c42)

**Part 2** Write a function `pizza(length, number)` that
draws number copies of an isosceles triangle, whose equal edges are the given length, whose apexes all touch in the
centre of the drawing, and whose bases form a 360 degree polygon.

Hints: Use `triangle()` to draw each segment. Calculate the angle based on the number of segments. Rotated each triangle
from the previous by angle degrees to form the pattern shown here.

![image](https://github.com/MaksymAndreiev/KUAS_Python/assets/29687267/56f7d004-6214-4177-b957-37a7589c595e)

## 4 Challenges

## 4.1 Precisely explaining a pattern — to Python

In Week 1 you practised describing how to draw this
pattern, very precisely, to your partner using a common native language.

This week describe precisely how to draw this pattern to your computer using the Python language. Create a function to
perform the drawing. Parameterize the function with the length of the sides of the square.

Hint: One way to do this is to calculate the length of the triangle’s sides and then re-use your `triangle()` function
from earlier.

![image](https://github.com/MaksymAndreiev/KUAS_Python/assets/29687267/c052ac3d-d9ea-4dcd-b13a-015e33c38eca)


## 4.2 Moving the ‘pen’ with goto

Write a function that uses `goto(x, y)` to plot two cycles
of a sine wave (angles in the range 2*π* to 2*π*) along the X axis (from *x* = 200 to *x* = 200). Multiply the value of
the sine function by 100 to scale it nicely. Hint: use `up()` and `down()` to turn drawing off and on.

![image](https://github.com/MaksymAndreiev/KUAS_Python/assets/29687267/7e5722f6-9d82-497a-9072-e632afa9cb6b)


## 4.3 Plotting an arbitrary function

Instead of plotting the sine function, modify your program to plot an arbitrary function `f(angle)`. Test your program
first with `f(angle)` equal to `sin(angle)`, which should produce the same result as the previous question.

Set $f(a) = \sin(a) + \frac{1}{3}\sin(3a)$ and plot the result.

Set $f(a) = \sin(a) + \frac{1}{3}\sin(3a) + \frac{1}{5}\sin(5a)$ and plot the result.

Use a `for` loop to extend this series so that

$$f(a) = \sin(a) + \frac{1}{3}\sin(3a) + \frac{1}{5}\sin(5a) + \ldots + \frac{1}{97}\sin(97a) + \frac{1}{99}\sin(99a)$$

and plot the result.

