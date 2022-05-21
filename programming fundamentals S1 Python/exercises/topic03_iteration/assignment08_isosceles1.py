"""
# Isosceles 1
Write a program that asks for the height of an isosceles right triangle.
This is a right triangle with the two legs
(and their corresponding angles) equal.

Print such a triangle on screen using ``*``.
The triangle is left aligned and has its top on top.

Negative or zero heights are not accepted.
Keep on asking for a correct
height until a positive number is entered.

## Example
    > -3
    > 0
    > 5
    *
    **
    ***
    ****
    *****
"""

user_input_number = int(input("User input number??"))

while user_input_number <= 0:
    user_input_number = int(input("User input number??"))

i = 1
stars = "*"
x = 1

while i <= user_input_number:
    while x < i:
        stars += "*"
        x += 1
    print(stars)
    stars = "*"
    x = 1
    i += 1
