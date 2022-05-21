from unittest import TestCase

from exercises.topic06_functions.assignment06 import *


class Tester06Functions5(TestCase):

    def testExtreme(self):
        self.assertEqual(-7, extreme([-2, 1, 0, -3, -7]))
        self.assertEqual(7, extreme([1, 7, 0, -3, -7], False))

    def testShiftToPositive(self):
        array = [-2, 1, 0, -3, -7]
        self.assertEqual([5, 8, 7, 4, 0], shift_to_positive(array))
        self.assertEqual([-2, 1, 0, -3, -7], array)
        self.assertEqual([1, 2, 3, 4], shift_to_positive([1, 2, 3, 4]))

    def testShiftToPositiveInPlace(self):
        array = [-2, 1, 0, -3, -7]
        self.assertEqual([5, 8, 7, 4, 0], shift_to_positive_in_place(array))
        self.assertEqual([5, 8, 7, 4, 0], array)
        self.assertEqual([1, 2, 3, 4],
                         shift_to_positive_in_place([1, 2, 3, 4]))

    def testSort(self):
        array = [9, 1, 5, 7, 3, 8, 4, 6, 2, 0]
        sort(array)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], array)

    def testSortCopy(self):
        array = [9, 1, 5, 7, 3, 8, 4, 6, 2, 0]
        hard_copy = [9, 1, 5, 7, 3, 8, 4, 6, 2, 0]
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], sort_copy(array))
        self.assertEqual(hard_copy, array)
        self.assertEqual([-10, 0, 100], sort_copy([100, -10, 0]))
