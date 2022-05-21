"""
# Average
Keep on asking for input (``float``) until a zero is entered.
Print the average of these (non-zero) inputs with 3 digits after
the decimal point.
Your program should print ``no data`` if the first input was a zero.

You can display 3 numbers after the decimal point by using
`format(math.pi, '.3f')`.

## Examples:

    > 1.4
    > -2.1
    > 3.0
    > -4
    > 0
    -0.425

    > 0
    no data

"""


user_input_number = format(float(input("Input a number???")), '.3f')

count = float(0)


count_non_zero = 0


if user_input_number == format(0, '.3f'):
    print("no data")
else:
    while user_input_number != format(0, '.3f'):
        count_non_zero += 1
        count = float(count) + float(user_input_number)
        user_input_number = format(float(input("Input a number???")), '.3f')
    print(format(count/count_non_zero, '.3f'))
