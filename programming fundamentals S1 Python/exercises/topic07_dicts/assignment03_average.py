"""
# Average Differences
Write the function `average_differences(people, age)`.
This function should compute
- the average age of the people younger than the given age, and
- the average age of the people older than the given age.
The function `average_differences` should return the positive
difference between the two.

**Hint 1:** Do not write the same code twice if you have written
some parts for this program already.
**Hint 2:** Copy-paste is NOT what I mean, try an import?

"""
import math

# friends = [
#     {"name": "Alice", "age": 30},
#     {"name": "Bob", "age": 40},
#     {"name": "Carol", "age": 30},
#     {"name": "David", "age": 20},
#     {"name": "Eve", "age": 40},
#     {"name": "Freddy", "age": 20}
# ]

# friends2 = [
#     {"name": "Alice", "age": 30},
#     {"name": "Bob", "age": 30},
#     {"name": "Carol", "age": 20},
#     {"name": "David", "age": 20},
#     {"name": "Eve", "age": 30},
#     {"name": "Freddy", "age": 20}
# ]

# friends3 = [
#     {"name": "Alice", "age": 9},
#     {"name": "Bob", "age": 10},
#     {"name": "Carol", "age": 11},
#     {"name": "David", "age": 15},
#     {"name": "Eve", "age": 19},
#     {"name": "Freddy", "age": 20},
#     {"name": "Eve", "age": 21}
# ]

# TODO


def average_differences(people, age):
    high, low, low_ages, high_ages = [], [], 0, 0

    for x in people:
        if x["age"] < age:
            low.append(x)
        elif x["age"] > age:
            high.append(x)
    for x in low:
        low_ages += x["age"]
    for x in high:
        high_ages += x["age"]

    return math.nan if len(low) == 0 or len(high) == 0 else (high_ages/len(high) - low_ages/len(low))
