"""
# Centered Square
Create a Python program that prints a square.
The edges should be pluses (+') and in the exact center,
there should be an oh (`o`).

Because it is only possible to place the `o` is in the exact center,
the size of the square has to odd. Moreover, the `o` should always
be visible, which makes 3 the smallest input.
Hence, keep asking for input, until it is valid.

These are the three smallest possible squares:
> 3
+++
+o+
+++


> 5
+++++
+   +
+ o +
+   +
+++++


> 7
+++++++
+     +
+     +
+  o  +
+     +
+     +
+++++++

"""

user_input_number = int(input("User input number??"))


while user_input_number < 3 or user_input_number % 2 == 0:
    user_input_number = int(input("User input number??"))


star = "+"
space = " "
mid = "o"

line = ""
x = 0
# print(user_input_number * star)
while x < user_input_number:
    line += "+"
    x += 1
print(line)


how_many_between = int((user_input_number - 3) / 2)
space_count = user_input_number - 2
count = 0
while count < how_many_between:
    x = 0
    spaces = ""
    while x < space_count:
        spaces += " "
        x += 1
    print(star + spaces + star)
    count += 1


space_between = int((user_input_number - 3)/2)
spaces = ""
x = 0
while x < space_between:
    spaces += " "
    x += 1
print(star + spaces + mid + spaces + star)


how_many_between = int((user_input_number - 3) / 2)
space_count = user_input_number - 2
count = 0
while count < how_many_between:
    x = 0
    spaces = ""
    while x < space_count:
        spaces += " "
        x += 1
    print(star + spaces + star)
    count += 1


line = ""
x = 0
while x < user_input_number:
    line += "+"
    x += 1
print(line)
