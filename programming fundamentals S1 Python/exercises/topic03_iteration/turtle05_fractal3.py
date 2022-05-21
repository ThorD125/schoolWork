"""
Program the turtle to draw the Hilbert Curve.
**Hint:** Lookup the Lindenmayer system and
use this to rewrite a string with "commando's".
"""

import turtle

# turtle.exitonclick()
# TODO


string = "A"
x = 0
while x < 6:
    new_string = ""
    for i in string:
        if i == "A":
            new_string += "AB"
        elif i == "B":
            new_string += "A"

    x += 1
    string = new_string
print(string)
