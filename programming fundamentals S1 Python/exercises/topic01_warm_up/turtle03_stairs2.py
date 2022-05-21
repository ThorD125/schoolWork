"""
Program the turtle to draw a stairs with 4 steps.
The height and width of these steps should be provided by the user.
"""

import turtle


count_stair = 4
height_stair = int(input("Input height of stair"))
width_stair = int(input("Input height of stair"))

i = 0
while i < count_stair:
    turtle.forward(width_stair)
    turtle.left(270)
    turtle.forward(height_stair)
    turtle.left(90)
    i += 1


turtle.exitonclick()
