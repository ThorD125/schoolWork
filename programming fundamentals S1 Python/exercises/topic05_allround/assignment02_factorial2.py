"""
# Factorial (II)
Ask for a number (`int`) as input and output its factorial.

The factorial of a number n is n! with n! = n * (n-1) * ... * 3 * 2 * 1
Your program should print `undefined` when a negative number is entered.
"""

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
else:
    print("undefined")
