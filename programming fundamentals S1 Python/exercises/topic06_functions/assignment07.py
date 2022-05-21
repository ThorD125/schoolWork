"""
Write the functions
`line`,
`rectangle`,
`parallelogram`, and
`triangle` such that all tests succeed.

*If the functionality you need already exists in
(a) Python (library), try to implement it yourself.
The exercise here is to write code, not to borrow it.*

The focus in this exercise is to work with default parameters.
All functions expect the `size` as first parameters (1 or 2).
These are compulsive.

After the size you can decide to create a filled shape or an *hollow shape*.
The default is filled.
        ****             ****
        ****             *  *
Filled: ****     Hollow: ****

Then, you can optionally supply how far from the left margin the drawing
should be placed (indentation).
By default the drawing should be placed as close to the margin as possible.

Finally, it should be possible to change the default drawing char
from '*' to anything else.

For `parallelogram` you can also decide the slope
(integer, positive or negative).

For triangle we suggest the following signature:
triangle(width, fill=True, indentation=0, char='*',
         align_right=False, from_top_to_bottom=True)
"""

import os


def read_shape(fn):
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, "06Functions7_shapes", fn), 'r') as file:
        return file.read()


# TODO


def line(stars, filled=True, shift=0, first_sign="*"):
    line = ""
    for i in range(shift):
        line += " "

    for i in range(stars):
        if i == 0 or i == stars - 1:
            line += first_sign
        elif filled:
            line += first_sign
        else:
            line += " "

    return line


def rectangle(length, height, filled=True, indent=0, char="*"):
    rectangle = ""
    for x in range(height):
        if x == 0:
            rectangle += line(length, True, indent, char) + "\n"
        elif x == height - 1:
            rectangle += line(length, True, indent, char)
        else:
            rectangle += line(length, filled, indent, char) + "\n"
    return rectangle


def square(width, filled=True, indent=0, char="*"):
    square = rectangle(width, width, filled, indent, char)
    return square


def parallelogram(length, height, filled=True, indent=0, char="*", slope=0):
    parallelogram = ""
    for x in range(height):
        for i in range(slope):
            parallelogram += " "
        slope -= 1
        for i in range(height - x-1):
            parallelogram += " "
        if x == 0 or x == height - 1:
            parallelogram += line(length, True, indent, char)
        else:
            parallelogram += line(length, filled, indent, char)
        if x != height - 1:
            parallelogram += "\n"

    return parallelogram


# print(read_shape("parallelogram_43_swap"))
# print(parallelogram(4, 3, True, 0, '*', -1))
# print(read_shape("parallelogram_43_shift2_swap"))
# print(parallelogram(4, 3, True, 0, '*', -2))


def triangle(base, filled=True, indent=0, char="*", align_right=False):
    triangle = ""
    i = 1
    while i <= base:
        if i == base:
            triangle += line(i, True, indent, char)
        else:
            triangle += line(i, filled, indent, char)

        if i < base:
            triangle += "\n"
        i += 1
    return triangle


# print(read_shape("triangle_5_right"))
# print(triangle(5, True, 0, '*', False))
# print(read_shape("triangle_5_bottom_up"))
# print(triangle(5, True, 0, '*', True, False))
# print(read_shape("triangle_5_bottom_up_right"))
# print(triangle(5, True, 0, '*', False, False))
