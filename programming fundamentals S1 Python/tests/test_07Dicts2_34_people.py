import math
from unittest import TestCase

from exercises.topic07_dicts.assignment02_split_and_count import (
    split_by_age, count_by_age
)
from exercises.topic07_dicts.assignment03_average import average_differences
from exercises.topic07_dicts.assignment04_maximise import biggest_difference

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


class TesterLocal(TestCase):

    def test_split_by_age_20(self):
        res = split_by_age(friends, 20)
        self.assertEqual([], res["lo"])
        self.assertEqual([friends[3], friends[5]], res["mid"])

        older = [friends[0], friends[1], friends[2], friends[4]]
        self.assertEqual(older, res["hi"])

    def test_split_by_age_30(self):
        res = split_by_age(friends, 30)
        self.assertEqual([friends[3], friends[5]], res["lo"])
        self.assertEqual([friends[0], friends[2]], res["mid"])
        self.assertEqual([friends[1], friends[4]], res["hi"])

    def test_split_by_age_35(self):
        res = split_by_age(friends, 35)
        younger = [friends[0], friends[2], friends[3], friends[5]]
        self.assertEqual(younger, res["lo"])
        self.assertEqual([], res["mid"])
        self.assertEqual([friends[1], friends[4]], res["hi"])

    def test_split_by_age_40(self):
        res = split_by_age(friends, 40)
        younger = [friends[0], friends[2], friends[3], friends[5]]
        self.assertEqual(younger, res["lo"])
        self.assertEqual([friends[1], friends[4]], res["mid"])
        self.assertEqual([], res["hi"])

    def test_count_by_age(self):
        self.assertEqual(0, count_by_age(friends, 0))
        self.assertEqual(2, count_by_age(friends, 20))
        self.assertEqual(0, count_by_age(friends, 25))
        self.assertEqual(2, count_by_age(friends, 30))
        self.assertEqual(0, count_by_age(friends, 35))
        self.assertEqual(2, count_by_age(friends, 40))
        self.assertEqual(0, count_by_age(friends, 45))

        self.assertEqual(0, count_by_age(friends2, 0))
        self.assertEqual(3, count_by_age(friends2, 20))
        self.assertEqual(0, count_by_age(friends2, 25))
        self.assertEqual(3, count_by_age(friends2, 30))
        self.assertEqual(0, count_by_age(friends2, 35))
        self.assertEqual(0, count_by_age(friends2, 40))
        self.assertEqual(0, count_by_age(friends2, 45))

    def test_average_differences(self):
        self.assertTrue(math.isnan(average_differences(friends3, 9)))
        self.assertEqual(8.2, average_differences(friends3, 10))
        self.assertEqual(9.25, average_differences(friends3, 11))
        self.assertEqual(10.0, average_differences(friends3, 15))
        self.assertEqual(9.25, average_differences(friends3, 19))
        self.assertEqual(8.2, average_differences(friends3, 20))
        self.assertTrue(math.isnan(average_differences(friends3, 21)))

    def test_biggest_difference(self):
        self.assertEqual(15, biggest_difference(friends3))
