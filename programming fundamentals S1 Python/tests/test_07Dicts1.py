from unittest import TestCase

from exercises.topic07_dicts.assignment01 import *


class Tester07Dictionary1(TestCase):
    friends = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 40},
        {"name": "Carol", "age": 20}
    ]

    friends_rep = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 40},
        {"name": "Carol", "age": 40}
    ]

    def testFind(self):
        self.assertEqual(self.friends[0], find_by_name(self.friends, "Alice"))
        self.assertEqual(self.friends[1], find_by_name(self.friends, "Bob"))
        self.assertEqual(self.friends[2], find_by_name(self.friends, "Carol"))
        self.assertIsNone(find_by_name(self.friends, "Zeno"))

    def testAge(self):
        self.assertEqual(30, get_age(self.friends, "Alice"))
        self.assertEqual(40, get_age(self.friends, "Bob"))
        self.assertEqual(20, get_age(self.friends, "Carol"))
        self.assertTrue(math.isnan(get_age(self.friends, "Zeno")))

    def testOld(self):
        f1 = self.friends_rep[1]
        f2 = self.friends_rep[2]
        self.assertEqual([f1], get_oldest(self.friends))
        self.assertEqual([f1, f2], get_oldest(self.friends_rep))
