"""
# Sentinel Extreme
Keep on asking for input (`int`) until a zero is entered.
Finally, print both the smallest and the largest number
that was entered (zero does not count).

If no numbers were entered (only zero), you should print two zeros.

## Example:
    > -1
    > -2
    > 0
    -2 -1
"""
user_input_number = int(input('user input number??'))

if 0 == user_input_number:
    print("0 0")

else:
    user_number_list = []
    while user_input_number != 0:
        user_number_list.append(user_input_number)
        user_input_number = int(input('user input number??'))

    i = 0
    while i < len(user_number_list):
        smallestnumber = user_number_list[0]
        if smallestnumber > user_number_list[i]:
            smallestnumber = user_number_list[i]
        i += 1
    i = 0
    while i < len(user_number_list):
        biggestnumber = user_number_list[0]
        if biggestnumber < user_number_list[i]:
            biggestnumber = user_number_list[i]
        i += 1

    print(smallestnumber, biggestnumber)
