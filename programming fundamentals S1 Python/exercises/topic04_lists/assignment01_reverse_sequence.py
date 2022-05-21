"""
# Reverse sequence
Write a program that asks for 100 numerical inputs and
outputs them in reverse order.
"""


input_list = []

max = 100

i = 0
while i < max:
    input_list.append(input("user input number"))
    i += 1

i = 1
while i <= max:
    print(input_list[int(len(input_list) - i)])
    i += 1
