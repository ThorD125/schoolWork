"""
# Highest frequency
Write a program that asks for numerical input (integers)

between 0 and 99 (both bounds inclusive).

When the users inputs a number outside this interval
the program stops asking input.
"""

user_input_number = int(input("user input number??"))

if 0 <= user_input_number and user_input_number <= 99:
    input_list = [0] * 100
    while 0 <= user_input_number and user_input_number <= 99:
        input_list[user_input_number] += 1
        user_input_number = int(input("user input number??"))

    """
    Finally, print the number that was entered the most.
    You can print -1 if there was no valid input.
    If multiple numbers apply, print the smallest.
    """

    i = 0
    most_frequent = input_list[0]
    while i < len(input_list):
        if most_frequent < input_list[i]:
            most_frequent = input_list[i]
        i += 1

    i = 0
    frequentie_list = []
    while i < len(input_list):
        if most_frequent == input_list[i]:
            frequentie_list.append(i)
        i += 1

    print(frequentie_list[0])
else:
    print("-1")

"""
# Hint 1: you can make use of the size of the interval
# Hint 2: you can make a list a priory instead of on the fly

## Example
    > 3
    > 2
    > 1
    > 3
    > 5
    > 3
    > 1
    > -10
    3

    > 1
    > 3
    > 2
    > 1
    > 3
    > 5
    > 3
    > 1
    > 678
    1

    > 123
    -1
"""
