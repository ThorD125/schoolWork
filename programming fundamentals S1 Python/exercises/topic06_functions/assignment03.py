"""
Write the functions
"reverse"
"is_palindrome"
"sub_str"
"find"
"find_all"
"replace" and
`decompose`
such that all tests succeed.

The key of this exercise is to start small: make your
function work for simple and small inputs. Just like in
the previous exercise the key is to reuse existing functions.

*If the functionality you need already exists in
(a) Python (library), try to implement it yourself.
The exercise here is to write code, not to borrow it.*
"""
# TODO


"""
"reverse"
"""


def reverse(string):
    result = ""
    for i in range(len(string)):
        result += string[len(string) - i - 1]

    return result


"""
"is_palindrome"
"""


def is_palindrome(string):
    if string == reverse(string):
        return True
    else:
        return False


"""
"sub_str"
"""


# def sub_str(string, start, end):
#     result = ""
#     if start > end:
#         start, end = end, start
#     end += start
#     while start < end:
#         result += string[start]
#         start += 1
#     return result


# print('voet', sub_str('voetbalveld', -11, 4))
# print('bal', sub_str('voetbalveld', -7, 3))

# print('bal', sub_str('voetbalveld', 7, -3))
# print('', sub_str('voetbalveld', 0, -1))
# print('veld', sub_str('voetbalveld', 11, -4))

# print('', sub_str('voetbalveld', -11, -1))
# print('', sub_str('voetbalveld', -15, -1))
# print('bal', sub_str('voetbalveld', -4, -3))


"""
"find"
"""


def find(substring, string, y=0):
    list = []
    while y < len(string)-len(substring) + 1:
        result = ""
        for x in range(0, len(substring)):
            result += string[x + y]

        if result == substring:
            list.append(y)
        # if not repeat:
        #     y += len(substring)
        y += 1
    if len(list) == 0:
        list.append(-1)
    return list[0]


"""
"find_all"
"""


# def find_all(substring, string, repeat=True):
#     list = []
#     y = 0
#     while y < len(string)-len(substring) + 1:
#         result = ""
#         for x in range(0, len(substring)):
#             result += string[x + y]

#         if result == substring:
#             list.append(y)
#         # if not repeat:
#         #     y += len(substring)
#         y += 1
#     if len(list) == 0:
#         list.append(-1)
#     return list[0]


# print([0, 2, 4], find_all('ha', 'hahaha'))
# print([0, 2], find_all('haha', 'hahaha'))
# print([0, 6, 8], find_all('haha', 'hahahihahahahihiha'))

# print([0], find_all('haha', 'hahaha', False))
# print([0, 6], find_all('haha', 'hahahihahahahihiha', False))

"""
"replace"
"""


# def replace():
#     return "result"


# print('voetloblob', replace('bal', 'lob', 'voetbalbal'))
# print('voet', replace('bal', '', 'voetbalbal'))
# print('balbal', replace('voet', '', 'voetbalbal'))
# print('voetbalbal', replace('sok', 'lob', 'voetbalbal'))
# print('hohoha', replace('haha', 'hoho', 'hahaha'))

"""
`decompose`
"""


def decompose(string):
    result = []
    for i in reverse(str(string)):
        result.append(int(i))
    return result
