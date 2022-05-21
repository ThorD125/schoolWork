"""
Program the turtle to draw Koch's snowflake.
**Hint:** Lookup the Lindenmayer system and
use this to rewrite a string with "commando's".
"""

import turtle


x = 0
i = 0
width_of_side = 200


def side():
    turtle.forward(width_of_side / (3 ** i))
    if width_of_side / (3 ** i) != width_of_side:
        turtle.left(360 / (3 * 2))
        turtle.forward(width_of_side / (3 ** i))
        turtle.right(360 / (3 * 2))
        turtle.right(360 / (3 * 2))
        turtle.forward(width_of_side / (3 ** i))
        turtle.left(360 / (3 * 2))
        turtle.forward(width_of_side / (3 ** i))
    turtle.right(360 / 3)


while i < 2:
    while x < 3:

        side()

        x += 1
    x = 0
    i += 1

turtle.exitonclick()
