"""
# Maximise the Difference

Find in a list of people the age for which the *Average Differences* (of the
younger and older people) is largest (maximised). If more than one age fits
this criterion, you should pick the age that occurred first in the list
(tiebreaker). Realise this computation by implementing the
`biggest_difference(people)` function.

**Watch out:** In the example the list seems to be in some logical order.
This is **ONLY** to facilitate the design of your algorithm. In general,
you should not count of the fact that the the input will be sorted always.
Hence, your solution should word on non-sorted data as well (see tests).
"""
# TODO
import math

friends = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 40},
    {"name": "Carol", "age": 30},
    {"name": "David", "age": 20},
    {"name": "Eve", "age": 40},
    {"name": "Freddy", "age": 20}
]

friends2 = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 30},
    {"name": "Carol", "age": 20},
    {"name": "David", "age": 20},
    {"name": "Eve", "age": 30},
    {"name": "Freddy", "age": 20}
]

friends3 = [
    {"name": "Alice", "age": 9},
    {"name": "Bob", "age": 10},
    {"name": "Carol", "age": 11},
    {"name": "David", "age": 15},
    {"name": "Eve", "age": 19},
    {"name": "Freddy", "age": 20},
    {"name": "Eve", "age": 21}
]


def biggest_difference(people):
    small = 1000
    big = 0
    for x in people:
        if x["age"] < small:
            small = x["age"]
        if x["age"] > big:
            big = x["age"]
    return (big + small)//2
