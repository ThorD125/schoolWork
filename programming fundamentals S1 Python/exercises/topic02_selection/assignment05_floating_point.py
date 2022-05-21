"""
# Oh-point-three
Write a program that takes two numbers (`float`) as input.
The program outputs `equal` if the sum of both numbers equals 0.3 or
`not equal` in the other case.

**Hint:** reflect on how a computer stores decimal numbers when
your program behaves unexpectedly.

## Examples:
    > 0.5
    > -0.2
    equal

    > 0.3
    > 0
    equal

    > 0.4
    > -0.2
    not equal
"""

input_number_1 = float(input("input number 1"))
input_number_2 = float(input("input number 2"))

precision = 0.005
end_number = 0.3

result = input_number_1 + input_number_2

if end_number + precision > result and result > end_number - precision:
    print("equal")
else:
    print("not equal")
