"""
# Area of a disk (circle)
Write a program that reads the radius of a circle (`float`),
and computes and prints the area up to 3 digits after the decimal point.
When a negative radius is supplied, the program replies with a `?`.

You can display 3 numbers after the decimal point by using
`format(math.pi, '.3f')`.


**Hint:** In Python you can represent π by using `math.pi`.
To use `math.pi`, however, one needs
to import `math` first. (This is done for you in this file)
"""

import math  # do not remove this line

radius = float(input("insert radius of circle"))

if radius >= 0:
    result = format(radius ** 2 * math.pi, '.3f')
    print(result)

else:
    print("?")
