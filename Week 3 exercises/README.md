# Information Processing 1 — Week 3 exercises

## 1 Using Python like a calculator

Python has the following mathematical operators:

| Code     | Result    | Notes                                            |
|----------|-----------|--------------------------------------------------|
| `a + b`  | `a + b`   |                                                  |
| `a - b`  | `a - b`   |                                                  |
| `a * b`  | `a × b`   |                                                  |
| `a / b`  | `a ÷ b`   | Result is always a float                         |
| `a // b` | `a ÷ b`   | Result is rounded down towards −∞                |
| `a % b`  | `a mod b` | The remainder from a // b                        |
| `a ** b` | `a^b`     | If a and b are both ints, then the result is int |

Using these operators, write Python expressions to calculate the answers to the following problems.
Evaluate the expressions in the interactive IDLE window, or write a short script that calculates and prints
out all four of the answers.

1. How many seconds are there in 42 minutes 42 seconds?
2. Given $c = 2 \pi r$ what is the circumference of a circle of radius 5?
3. Given $a = \pi r^2$ what is the area of a circle with radius 5?
4. Given $v = \frac{4}{3} \pi r^3$ what is the volume of a sphere with radius 5?\
   Hint: after executing this statement\
   `from math import pi`\
   the variable ‘pi’ will contain the value of π.

## 2 Algorithms and programs

**Part 1**. The following algorithm converts a temperature from Celsius to Fahrenheit, where:f=^95 c+ 32

```
1. start
2. input integer temperature c
3. let f = c ∗ 1.8
4. let f = f + 32
5. output f
6. stop
```

Here are the lines of a Python program that implements this algorithm.

```
f = f + 32
print(f)
f = c * 1.
c = int(input("c: "))
```

The lines are not in the correct order. Copy and paste the lines into a Python script, in the correct order.
Run the script to make sure it works. (Test cases: 0C = 32F, 50C = 122F, and 100C = 212F)

**Part 2**. The following algorithm converts from Fahrenheit to Celsius, where:c=^59 (f− 32 )

```
1. start
2. input integer temperature f
3. let c = f − 32
4. let c = c ∗ 5
5. let c = c / 9
6. output c
7. stop
```

Implement the algorithm as a Python script. Test the script using the same test cases as above.

## 3 Flowcharts and programs

![image](https://github.com/MaksymAndreiev/KUAS_Python/assets/29687267/a4f3f6ae-cb53-4cd8-a4da-2261a9064b1d)

Write a program that inputs the total length of a movie in minutes and then
outputs the length of the movie in hours and minutes. The flowchart is
shown on the right.
To make this work you will need to find the _floor_ of a floating-point number
(the closest integer that is no larger than the floating-point number). There
are several ways to do this, for example, by converting the float into an
int or by using the ‘//’ operator which performs integer division even if
one or both of its operands are floats.

Test your program on several movie lengths in minutes that have obviously
correct answers when expressed as hours plus minutes, like this (where the
text that you type as input is shown in red):

```
minutes: 215
3 hours 35 minutes
```

## 4 Multiple inputs and outputs

Write a program that:

1. inputs the length of the two shorter sides of a right triangle, then
2. outputs the length of the hypotenuse and the area of the triangle.
   Test it with several obvious cases, for example:

```
a: 3
b: 4
hypotenuse 5.0 area 6.
```

## 5 Vector dot product

Python understands several other types, some of which can be used to represent vectors. Try typing
these expressions into the interactive IDLE window:

```
(3, 4)

(3, 4)[0]

(3, 4)[1]
```

The input() function returns the text of what you type ‘verbatim’, as a string, without trying to interpret
it as any kind of value. To interpret the text as a program value you can pass it to the ‘eval(s)’ function,
where s is a string and the result is the value you would obtain if you typed the contents of the string as
part of a program. Try this in the interactive IDLE window or in a script:

```
s = input("vector: ")
v = eval(s)
print(v[0])
print(v[1])
```
and type the input “(3, 4)” (without the quotes).


You now know enough to write a program that prompts for two vectors,AandB, and then prints their
dot (‘inner’) product A·B, where: $A \cdot B = A_x B_x + A_y B_y$.\
Your program should behave like this:

```
vector A: (3,1)

vector B: (3,-1)

(3, 1). (3, -1) = 8
```

## 6 Challenges

In case you found the first five questions too easy, here are some more challenging
exercises. If you finish all of the challenges before the end of the class then you will
earn 1 bonus point towards your final score.

### 6.1 Simple ‘while’ loops

![image](https://github.com/MaksymAndreiev/KUAS_Python/assets/29687267/2643d9fb-7125-4a90-985f-37e403308d83)

This Python program prints the first ten integers, from 10 down to 1.

```
N = 10
while (N > 0):
print(N)
N = N - 1
print("done")
```
Note how indentation is used to indicate which statements are inside the ‘body’ of
the loop, just like we have been doing for pseudo-code.

The flowchart on the right shows a variation on this program that calculates the
sum of the first _N_ counting numbers. Modify the program so that it implements
the flowchart. Verify that the sum of the first ten counting numbers is 55 :
```
N: 10
55
```

### 6.2 Factorial function

Make a copy of your previous program. Modify it trivially to calculate the factorial ofN,N!, where:

$$N! =
\begin{cases}
    1 & \text{if } N = 0 \\
    N \times (N-1)! & \text{if } N > 0
\end{cases}
$$

(Assume the input will never be < 1.) Verify the program using an easy input value, e.g:
```
N: 5
120
```
### 6.3 Fibonacci function

Make a copy of your previous program. Modify the program so that it prints the $N^\text{th} $ Fibonacci number,
$F_N $, where: $F_0 = 0 , F_1 = 1, and F_N = F_{N-1} + F_{N-2}$. The sequence of Fibonacci numbers is therefore:

````
0 1 1 2 3 5 8 13 21 34 55 89 144 ...
````

Test your program by printing the 13thFibonacci number,F 13 , which should be 233.

### 6.4 Limit of the ratio of successive Fibonacci numbers

As the Fibonacci numbers become larger the ratio between them $\frac{F_n}{F_{n-1}}$ rapidly tends towards a constant.
Use your program to find the value of that constant to a reasonable accuracy.
