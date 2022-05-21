"""
# Isosceles 5
Write a program similar to "Isosceles 2".
This time triangle is centered and has its top on top.
Watch out, not all triangle have a top with 1 star. Some have two stars.

## Example
    > -3
    > 0
    > 5
      *
     ***
    *****

    > -3
    > 0
    > 4
     **
    ****
"""


user_input_number = int(input("user input number ??"))
# user_input_number = 5
# user_input_number = 8

while user_input_number <= 0:
    user_input_number = int(input("user input number ??"))

white_space = " "
stars = "*"

if user_input_number % 2:
    white_space_count = int((user_input_number - 1) / 2)
    stars_count = 1
else:
    white_space_count = int((user_input_number - 2) / 2)
    stars_count = 2


while stars_count <= user_input_number:
    x = 0
    # white_spaces = white_space_count * white_space
    white_spaces = ""

    while x < white_space_count:
        white_spaces += " "
        x += 1

    # stars_result = stars_count * stars
    stars_result = ""
    y = 0
    while y < stars_count:
        stars_result += "*"
        y += 1

    print(white_spaces + stars_result)
    stars_count += 2
    white_space_count -= 1
