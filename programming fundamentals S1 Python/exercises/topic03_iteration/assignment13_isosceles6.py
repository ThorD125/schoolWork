"""
# Isosceles 6
Write a program similar to "Isosceles 5".
This time the triangle is centered and has its top at the bottom.

# Example
    > -3
    > 0
    > 5
    *****
     ***
      *

    > -3
    > 0
    > 4
    ****
     **
"""


user_input_number = int(input("user input number ??"))
# user_input_number = 5
# user_input_number = 8

while user_input_number <= 0:
    user_input_number = int(input("user input number ??"))


stars = ""
x = 0
whites = ""

while x < user_input_number:

    y = 0
    while y < user_input_number - x:
        # print(user_input_number - x)
        stars += "*"

        y += 1

    y = 0

    while y < x // 2:
        whites += " "
        y += 1

    print(whites + stars)
    whites = ""
    stars = ""
    x += 2
