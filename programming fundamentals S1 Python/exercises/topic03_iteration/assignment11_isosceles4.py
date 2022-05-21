"""
# Isosceles 4
Write a program similar to "Isosceles 1".
This time triangle is right aligned and has its top on top.

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
whitespaces = ""
x = 1
y = 1

while i <= user_input_number:
    if user_input_number - i != 0:
        while y <= user_input_number - i:
            whitespaces += " "
            y += 1

    while x < i:
        stars += "*"
        x += 1

    print(whitespaces + stars)

    y = 1
    x = 1
    stars = "*"
    whitespaces = ""
    i += 1
