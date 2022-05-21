"""
# Factorial
Ask for a positive number (``int``) and print
all numbers (line by line) from 0 through the entered number (included)

## Example:
    > 3
    0
    1
    2
    3

"""


user_input_number = int(input("User input number??"))

i = 0

while i <= user_input_number:
    print(i)
    i += 1
