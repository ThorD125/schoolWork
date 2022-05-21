"""
# Full Digit Swap Extra
Take one integer as input.
Output the number with the digits reversed but keep the sign.
Leading zeros are not allowed.

## Examples:
    > 1234
    4321

    > -4321
    -1234

    > -700
    -7
"""

number_input = int(input("input number"))


if number_input == 0:
    print(0)
else:
    result = 0
    x = 0
    while 10 ** x < abs(number_input):
        number = abs(number_input) // (10 ** x)
        remainder = number % 10
        result = result * 10 + remainder
        x += 1

    if number_input < 0:
        print(result * -1)
    else:
        print(result)
