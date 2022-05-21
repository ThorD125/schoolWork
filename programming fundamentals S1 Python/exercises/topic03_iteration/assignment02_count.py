"""
# Sentinel
Keep on asking for input (``int``) until a zero is entered.
Count and print how many non-zero inputs you received.

## Example:

    > 1
    > -2
    > 3
    > -4
    > 0
    4

"""


count_non_zero = 0

user_input_number = int(input("Input number"))

while user_input_number != 0:
    count_non_zero += 1
    user_input_number = int(input("Input number"))

print(count_non_zero)
