from unittest import TestCase

from exercises.topic06_functions.assignment08 import *


class Tester06Functions8(TestCase):

    def testV1(self):
        self.assertEqual(0, find_index_v1("a", "azerty"))
        self.assertIsNone(find_index_v1("q", "azerty"))

    def testV2(self):
        self.assertEqual(0, find_index_v2("a", "azerty"))
        self.assertFalse(find_index_v2("q", "azerty"))

    def testV3(self):
        self.assertEqual(0, find_index_v3("a", "azerty"))
        self.assertTrue(math.isnan(find_index_v3("q", "azerty")))

    def testV4(self):
        self.assertEqual(0, find_index_v4("a", "azerty"))
        self.assertEqual(-1, find_index_v4("q", "azerty"))
