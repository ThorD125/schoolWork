"""
# Split and Count
In the following three assignments, we will be working with (lists of) people.
One person is represented as a dictionary containing a `name` and an `age`:
```Python
{"name": "Alice",  "age": 30}
```

Write the function `split_by_age(people, age)` which partitions a list
into three list:
- the people younger than age;
- the people older than age; and
- the people who are exactly 'age' years old.

That is why the function `split_by_age` should  return a dictionary
with these three lists. Check the tests, to figure out what the keys
of this dictionary are.

Second, write a function `count_by_age(people, age)` which counts the
number of people of the given age. Try to write as few lines of code
as possible (reuse).
"""
# # TODO
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


def split_by_age(people, age):
    lo = []
    mid = []
    hi = []
    for x in people:
        if x["age"] < age:
            lo.append(x)
        elif x["age"] > age:
            hi.append(x)
        else:
            mid.append(x)

    return {"lo": lo, "mid": mid, "hi": hi}


def count_by_age(people, age):
    return len(split_by_age(people, age)["mid"])
