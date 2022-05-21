"""
# Basic text functions
Write the functions
"""

"""
All these functions should be written such that the tests succeed.
The goal of this exercise is to create a lot of
small helper functions and to re-use them.

If the functionality you need already exists in
(a) Python(library), try to implement it yourself.
The exercise here is to write code, not to borrow it.
You can make use of `ord()` and `chr()`
that respectively turn a chracter into an integer, and vice versa.
Hence, it is not necessary to implement `ord()` and `chr()` yourself.

First play with these two functions until you understand how they work.
Then try to write a function `is_between` this function can be used
to make extreme simple implementations of ``is_digit` and `is_alpha`.
"""
# TODO


def is_whitespace(ch):  # given
    return ch == ' ' or ch == '\t' or ch == '\r' or ch == '\n'


"""
`is_between`,
"""


def is_between(number, first, last):
    return True if ord(first) <= ord(number) and ord(number) <= ord(last) else False


"""
`is_digit`,
"""


def is_digit(number):
    return is_between(number, '0', '9')


"""
`to_upper`,
"""


def to_upper(string):
    new_string = ''
    for i in range(len(string)):
        if is_between(string[i], 'a', 'z'):
            new_string += chr(ord(string[i]) - 32)
        else:
            new_string += string[i]
    return new_string


"""
`to_lower`,
"""


def to_lower(string):
    new_string = ''
    for i in range(len(string)):
        if is_between(string[i], 'A', 'Z'):
            new_string += chr(ord(string[i]) + 32)
        else:
            new_string += string[i]
    return new_string


"""
`is_alpha`,
# """


def is_alpha(string):
    return is_between(string, 'a', 'z') or is_between(string, 'A', 'Z')


"""
`is_int`, and
"""


def is_int(number):
    answer = True
    for i in number.replace('  ', ''):
        if ord(i) == 46:
            answer = False
            break
        elif not ((47 < ord(i) and ord(i) < 58) or ord(i) == 45 or ord(i) == 43):
            answer = False

    return answer


"""
`trim`.
"""


def trim(string):
    return string.strip()
# TODO: strip
