"""
# Factorial
Ask for a positive number (``int``) as input and output its factorial.

The factorial of a number n is n! with n! = n * (n-1) * ... * 3 * 2 * 1

For negative numbers the factorial is not defined. In this case you can
simply return 1.
"""


user_input_number = int(input("User input number??"))


if user_input_number > 0:
    i = 0

    user_input_number_original = user_input_number - 1

    while user_input_number_original > 0:
        user_input_number *= user_input_number_original
        user_input_number_original -= 1

    print(user_input_number)
else:
    print("1")
