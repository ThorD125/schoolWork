"""
# Sentinel Extreme Pro
Keep on asking for input (`int`) until a zero is
entered or when 10 numbers have been entered.
Finally, print both the smallest and the largest
number that was entered (zero does not count).

If no numbers were entered (only zero), you should print two zeros.
"""


user_input_number = int(input('user input number??'))

if user_input_number == 0:
    print("0 0")
else:
    user_list = []

    while user_input_number != 0 and len(user_list) < 10:
        user_list.append(user_input_number)
        user_input_number = int(input('user input number??'))

    user_list.sort()
    print(user_list[0], user_list[-1])
