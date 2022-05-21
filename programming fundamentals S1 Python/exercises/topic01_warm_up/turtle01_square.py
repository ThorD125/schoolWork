"""
Program the turtle to draw a square of 100 by 100.
"""

import turtle

i = 0

while i < 4:
    turtle.forward(100)
    turtle.right(90)
    i += 1

turtle.exitonclick()
