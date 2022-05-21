"""
Program the turtle to draw Sierpinski triangle.
**Hint:** Lookup the Lindenmayer system and
use this to rewrite a string with "commando's".
"""

import turtle


turtle.speed(10000)

forward = 500

angel = 120
x = 1

length = 0


def triangle(forward, angel, x=1):
    while x <= 3:
        turtle.forward(forward)
        turtle.left(angel)
        x += 1


triangle(forward, angel)
forward /= 2
turtle.forward(forward)
turtle.left(angel/2)

triangle(forward, angel)


turtle.exitonclick()
