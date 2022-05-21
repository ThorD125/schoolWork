"""
# Isosceles 2
Write a program similar to "Isosceles 1".
This time the triangle is left aligned and has its top at the bottom.

## Example
    > -3
    > 0
    > 5
    *****
    ****
    ***
    **
    *
"""


user_input_number = int(input("User input number??"))

while user_input_number <= 0:
    user_input_number = int(input("User input number??"))


i = user_input_number
stars = "*"
x = 1

while i > 0:
    while x < i:
        stars += "*"
        x += 1
    print(stars)
    stars = "*"
    x = 1
    i -= 1
