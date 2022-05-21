"""
# Star Rectangle
Write a program that asks for two numerical inputs (``int``): the height and
the width of a rectangle. Print such a rectangle on screen using ``*``.

The program has no output if either the height or the width is negative (or 0).

## Example:
    > 4
    > 3
    ***
    ***
    ***
    ***
"""

user_input_number_height = int(input("User input height number??"))
user_input_number_width = int(input("User input width number??"))

stars = ""
i = 0
x = 0

if user_input_number_height != 0 and user_input_number_width != 0:
    while i < user_input_number_height:
        while x < user_input_number_width:
            stars += "*"
            x += 1
        print(stars)
        i += 1
