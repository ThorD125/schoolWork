"""
# Rework your old exercises
Write the functions `gcd` (greatest common divisor),
"""
import math


def gcd(smallest_number, biggest_number):
    if smallest_number > biggest_number:
        biggest_number, smallest_number = smallest_number, biggest_number

    while biggest_number % smallest_number > 0:
        biggest_number %= smallest_number
        biggest_number, smallest_number = smallest_number, biggest_number

    return smallest_number


"""
`swap_digits`,
"""


def swap_digits(number_input):
    if number_input == 0:
        return 0
    else:
        result = 0
        x = 0
        while 10 ** x < abs(number_input):
            number = abs(number_input) // (10 ** x)
            remainder = number % 10
            result = result * 10 + remainder
            x += 1

        if number_input < 0:
            return result * -1
        else:
            return result


"""
`factorial`,
"""


def product_range(number):
    number_original = number - 1
    while number_original > 0:
        number *= number_original
        number_original -= 1
    return number


def factorial(number):
    if number > 0:
        # number_original = number - 1

        # while number_original > 0:
        #     number *= number_original
        #     number_original -= 1

        # return number
        smallest_number = 1
        result = 1
        while number > smallest_number:
            result *= number
            number -= 1
        return result

        # return product_range(number)
    else:
        return 1


"""
`variation`,
"""

print(5040)
print(factorial(7))
print(1)
print(factorial(0))

print("lskjfemlkjesmesmslkj")


def variation(n, k):
    check, result = n - k, 1

    while n > check:
        result *= n
        n -= 1

    if not (n < 0 or k < 0):
        return result
    else:
        return 0


print(7)
print(variation(7, 1))
print(5040)
print(variation(7, 6))
print(1500000000)
print(variation(1500000000, 1))
print(0)
print(variation(6, 7))
print(0)
print(variation(-7, -6))
print(0)
print(variation(-7, 6))
print(0)
print(variation(7, -6))
print(1)
print(variation(0, 0))

"""
`avg` (average), and
"""


def avg(numbers):
    if len(numbers) != 0:
        sum = 0
        i = 0
        while i < len(numbers):
            sum += numbers[i]
            i += 1

        res = sum / len(numbers)

        if res > 0:
            return res
        elif res == 0:
            return 0
    else:
        return math.nan


"""
`largest_prime`.
"""


def largest_prime(user_input_number):
    list_of_primes, magic_priem = [0] * (user_input_number + 1), math.nan
    for i in range(2, len(list_of_primes)):
        if 0 == list_of_primes[i]:
            magic_priem = i
            for x in range(2, len(list_of_primes)):
                if x * i < len(list_of_primes):
                    list_of_primes[x * i] += 1
    return(magic_priem)


"""
All these functions should be written suchnt that the tests succeed.
Take a look at your previous programs for the algorithms.
The focus of this exercise, is to decide which parameters to use
and what your function should return.

When working on `variation` keep performance in mind! When the
tests for both `factorial` and `variation` succeed, take a
look at both functions: can you see that they share a big part
of code? Try to extract a function that I would call
`product_range` and use it in both `factorial` and `variation`.
Your tests should still succeed:
 this means your code still works. Changing a program
 (to improve its quality) without changing its solutions or
 outcomes is called *refactoring*.
"""
# TODO
