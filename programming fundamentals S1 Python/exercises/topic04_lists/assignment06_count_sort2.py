"""
# Count sort
Write a program that asks for numerical input (integers) between 0 and 99.
When the users inputs a number outside this interval
the program stops asking input.
"""


user_input_number = int(input("user input number??"))
input_list = []


while 0 <= user_input_number and user_input_number <= 99:
    input_list.append(user_input_number)
    user_input_number = int(input("user input number??"))


if len(input_list) == 0:
    print("-1")
else:
    input_list.sort()
    print(input_list)


"""
Finally, print all the number that where entered from small to large.
Numbers that were entered multiple times are thus printed multiple times.


## Example
    > 3
    > 2
    > 1
    > 3
    > 5
    > 3
    > 1
    > -10
    [1, 1, 2, 3, 3, 3, 5]
"""
