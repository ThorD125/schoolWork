"""
# What if it cannot be found?

Write a simple function to find the index of an element (first argument)
in a list or string (second argument).
For once, you can do some copy-pasting in your solution because we want
this function four times.

The goal of this exercise is to learn and read unit tests and figure out
what the expected outcome of a function should be. Each version has its
value, depending on the language one is preferred over the other.

"""
# TODO

import math


def find_index_v1(letter_to_find, string_to_search):
    index = 0
    while index < len(string_to_search):
        if string_to_search[index] == letter_to_find:
            return index
        index += 1
    return None


def find_index_v2(letter_to_find, string_to_search):
    index = 0
    while index < len(string_to_search):
        if string_to_search[index] == letter_to_find:
            return index
        index += 1
    return False


def find_index_v3(letter_to_find, string_to_search):
    index = 0
    while index < len(string_to_search):
        if string_to_search[index] == letter_to_find:
            return index
        index += 1
    return math.nan


def find_index_v4(letter_to_find, string_to_search):
    index = 0
    while index < len(string_to_search):
        if string_to_search[index] == letter_to_find:
            return index
        index += 1
    return -1
