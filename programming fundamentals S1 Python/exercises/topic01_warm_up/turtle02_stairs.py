"""
Program the turtle to draw a stairs with 4 steps.
 each step is 10 high and has a width of 50.
You can stop at 4 steps.
"""

import turtle


count_stair = 4
height_stair = 10
width_stair = 50

i = 0
while i < count_stair:
    turtle.forward(width_stair)
    turtle.right(90)
    turtle.forward(height_stair)
    turtle.left(90)
    i += 1


turtle.exitonclick()
