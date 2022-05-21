"""
# Sieve of Eratosthenes
Write a program that expects a positive integer as input.
This input is the upper bound.
Then, the program prints all prime-numbers below that upper bound.

**Hint 1:** Look up "Sieve of Eratosthenes" and implement this algorithm.
**Hint 2:** Skip this exercise if you have other exercises left to make.

    > 14
    2
    3
    5
    7
    11
    13
"""

user_input_number = int(input("user input number??"))

list_of_primes = [0] * (user_input_number + 1)

i = 2
while i < len(list_of_primes):
    if 0 == list_of_primes[i]:
        x = 0
        while i * x <= user_input_number:
            list_of_primes[i*x] = 1
            x += 1
        print(i)
    i += 1
