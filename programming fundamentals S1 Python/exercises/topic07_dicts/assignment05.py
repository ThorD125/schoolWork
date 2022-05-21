"""
Write the functions `dict_zip` and `dict_combine`.

`dict_zip` turns a list of keys and a list of values into a new dictionary.
This, of coarse, only works when both lists contain an equal amount of
elements. If is not possible to create a dictionary because the above rule
is not met, you can return nothing (None).

`dict_combine` creates a new dictionary out of two other dictionaries.
The result should have one entry for each of the keys of both dictionaries.
If both input dictionaries have the same key and the same value, only one
entry is created. If both input dictionaries have the same key with a
different value, the value in the resulting dictionary is a list of both
values.
"""
# TODO


def dict_combine(val1, val2):
    dict = {}
    for x in val1:
        if len(val1) == len(val2):
            if x in val2.keys() and val1[x] != val2[x]:
                dict[x] = [val1[x], val2[x]]
            else:
                dict[x] = val1[x]
                # dict[x] = val2[x]

            # else:
            #     dict[x] = val1[x]
            #     dict[x] = val2[x]
                # print(x)
            # dict[x] = [val1[x]]
    return dict


a = {"a": 1}
b = {"b": True}
c = {"a": False}

ab = {
    "b": True,
    "a": 1
}

ac = {
    "a": [1, False]
}

print(ab, dict_combine({"a": 1}, {"b": True}))
print(a, dict_combine({"a": 1}, {"a": 1}))
print(b, dict_combine({"b": True}, {"b": True}))
print(a, dict_combine({"a": 1}, {}))
print(b, dict_combine({}, {"b": True}))
print(ac, dict_combine({"a": 1}, {"a": False}))


# def dict_zip(x=None, y=None, z=None):
#     return x


# abc123 = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }

# print(abc123, dict_zip(["a", "b", "c"], [1, 2, 3]))
# self.assertIsNone(dict_zip(["a", "b", "c"], [1, 2]))
