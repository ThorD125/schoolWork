"""
# The Swap Trick
Write a program that reads two inputs into the two variables ``a`` and ``b``.
Make sure that the contents of ``a`` and ``b`` are swapped before printing.

You can update this Python program, but are not allowed to change it!
**Hint:** You can introduce a third variable.
"""

a = input()  # do not remove this line
b = input()  # do not remove this line

# Write your program here:

a_initial = a
b_initial = b

a = b_initial
b = a_initial

print(a, b)  # do not remove this line
