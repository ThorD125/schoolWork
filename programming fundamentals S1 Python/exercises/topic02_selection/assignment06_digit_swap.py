"""
# Digit Swap
Read one number (`int`) as input.

If the number has exactly two digits, the program swaps both digits.
Otherwise the number is printed as is.
The sign of the number is **always** preserved.

**Hint 1:** The input is a number, do not try to convert is to a string.
**Hint 2:** Do not use the internet: the first solution(s) you will find
are wrong !

## Examples:
    > 1234
    1234

    > -1234
    -1234

    > -4
    -4

    > 6
    6

    > 34
    43

    > -12
    -21

    > -70
    -7
"""

number_input = int(input("input number"))


if (9 < number_input and number_input < 100):
    number_one = number_input % 10
    number_two = number_input // 10
    result = number_one * 10 + number_two
    print(result)

elif (-100 < number_input and number_input < -9):
    number_one = abs(number_input) % 10
    number_two = abs(number_input) // 10

    result = number_one * -10 - number_two
    print(result)

else:
    print(int(number_input))
