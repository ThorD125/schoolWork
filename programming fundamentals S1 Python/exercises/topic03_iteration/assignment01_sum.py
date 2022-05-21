"""
# Sum
Keep on asking for input (`float`) until a zero is entered.
Print the sum of these (non-zero) inputs with 3 digits after the decimal point.

You can display 3 numbers after the decimal point by using
`format(math.pi, '.3f')`.

## Examples:

    > 1.4
    > -2.1
    > 3.0
    > -4
    > 0
    -1.700
"""
user_input_number = format(float(input("Input a number???")), '.3f')

count = float(0)


while user_input_number != format(0, '.3f'):
    count = float(count) + float(user_input_number)
    user_input_number = format(float(input("Input a number???")), '.3f')

print(format(count, '.3f'))
