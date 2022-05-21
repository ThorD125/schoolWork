"""
Implement the functions
`extreme`,
`shift_to_positive`,
`shift_to_positive_in_place`,
`sort`, and
`sort_copy` such that all tests succeed.

`extreme` searches the smallest or largest element in a list.
The second (optional) argument decides whether to pick the smallest (default).

`shift_values_to_positive` creates a list with the same elements as the input
list, but ensures that all elements are positive by shifting them all with
the smallest possible number (if needed).

`shift_to_positive_in_place` does the exact same thing *in place* , the
original list is updated.

Take a look at the tests to see how we verify both functions.


`sort`, and `sort_copy` both take a list with numbers as input and  returns a
list with the same numbers from low to high (sorted). The difference is that
`sort` is *in-place*, i.e., the original list is updated and that `sort_copy`
creates a new list.

**Hint:** Take a look at this algorithm ans try to translate the English
text into Python code. The algorithm is not part of this courses material.
https://en.wikipedia.org/wiki/Insertion_sort

If the functionality you need already exists in
(a) Python (library), try to implement it yourself.
The exercise here is to write code, not to borrow it.
"""
# TODO


def extreme(list, negative=True):
    number = list[0]
    for i in list:
        if i < number and negative:
            number = i
        elif i > number and not negative:
            number = i
    return number


def shift_to_positive(list):
    result = []
    extremeNum = extreme(list)
    if extremeNum == 1:
        return list
    for i in list:
        result.append(i - extremeNum)
    return result


def shift_to_positive_in_place(list):
    # print(extreme(list), extreme(list, False))
    return shift_to_positive(list)


array = [-2, 1, 0, -3, -7]
print([5, 8, 7, 4, 0], shift_to_positive_in_place(array))
print([5, 8, 7, 4, 0], array)
print([1, 2, 3, 4], shift_to_positive_in_place([1, 2, 3, 4]))


def sort(list):
    for x in list:
        i = 0
        while i < len(list) - 1:
            if list[i+1] < list[i]:
                list[i], list[i+1] = list[i+1], list[i]
            i += 1

    return list


def sort_copy(list):
    newlist = []
    for x in list:
        newlist.append(x)
    return sort(newlist)
