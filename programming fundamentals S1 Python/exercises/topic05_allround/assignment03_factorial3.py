"""
# Factorial (II)
Ask for a number (`int`) as input and output its factorial.
Your program should keep on asking for input until a
positive number is entered.


## Example:
    > -6
    > -3
    > 4
    24
"""

user_input_number = int(input("User input number??"))

while user_input_number < 0:
    user_input_number = int(input("User input number??"))

if user_input_number > 0:
    i = 0

    user_input_number_original = user_input_number - 1

    while user_input_number_original > 0:
        user_input_number *= user_input_number_original
        user_input_number_original -= 1

    print(user_input_number)
elif user_input_number == 0:
    print("1")
