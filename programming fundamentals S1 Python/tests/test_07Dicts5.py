from unittest import TestCase

from exercises.topic07_dicts.assignment05 import *


class Tester07Dictionary2(TestCase):

    def testCombine(self):
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

        self.assertEqual(ab, dict_combine(a, b))
        self.assertEqual(a, dict_combine(a, a))
        self.assertEqual(b, dict_combine(b, b))
        self.assertEqual(a, dict_combine(a, {}))
        self.assertEqual(b, dict_combine({}, b))
        self.assertEqual(ac, dict_combine(a, c))

    def testZip(self):
        abc123 = {
            "a": 1,
            "b": 2,
            "c": 3
        }

        self.assertEqual(abc123, dict_zip(["a", "b", "c"], [1, 2, 3]))
        self.assertIsNone(dict_zip(["a", "b", "c"], [1, 2]))
