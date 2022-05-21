"""
# Euclid
Write a program that reads two positive integers (no need to check the input).
Print out the largest divisor that both numbers have in common
(greatest common divisor, GCD or "grootste gemene deler")

**Hint:** use Euclid's algorithm:
    https://en.wikipedia.org/wiki/Euclidean_algorithm
    https://nl.wikipedia.org/wiki/Algoritme_van_Euclides#Het_algoritme
"""

user_input_number_1 = int(input("User input number1??"))
user_input_number_2 = int(input("User input number2??"))

if user_input_number_1 < user_input_number_2:
    biggest_number, smallest_number = user_input_number_2, user_input_number_1
else:
    biggest_number, smallest_number = user_input_number_1, user_input_number_2

if biggest_number % smallest_number == 0:
    endresult = smallest_number
else:
    while biggest_number % smallest_number != 0:
        endresult = biggest_number % smallest_number
        biggest_number = biggest_number % smallest_number
        biggest_number, smallest_number = smallest_number, biggest_number

print(endresult)
