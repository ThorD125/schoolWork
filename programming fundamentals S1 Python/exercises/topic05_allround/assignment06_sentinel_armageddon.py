"""
# Sentinel Extreme Pro
Keep on asking for input (`int`) until a zero is entered
or when 10 numbers have been entered.

Finally, print *the index* of both the smallest
and the largest number that was entered (zero does not count).
The index of the first number is 1, the index of the second is 2, ...

Try not to use a list.

If no numbers were entered (only zero), you should print two zeros.
"""

number = int(input())
index_counter = 0

smallest_number = number
biggest_number = number

smallest_index = 0
biggest_index = 0

while number != 0 and index_counter < 10:
    index_counter = index_counter + 1
    if number <= smallest_number:
        smallest_number = number
        smallest_index = index_counter
    if number >= biggest_number:
        biggest_number = number
        biggest_index = index_counter
    number = int(input())

print(smallest_index, biggest_index)
