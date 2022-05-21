import os
from unittest import TestCase

from exercises.topic06_functions.assignment07 import *


def read_shape(fn):
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, "06Functions7_shapes", fn), 'r') as file:
        return file.read()


class Tester06Functions7(TestCase):

    def testLine(self):
        self.assertEqual('****', line(4))
        self.assertEqual('*  *', line(4, False))
        self.assertEqual('   *  *', line(4, False, 3))
        self.assertEqual('+', line(1, True, 0, '+'))
        self.assertEqual(' +- +-', line(3, False, 1, '+-'))
        self.assertEqual('', line(0, False, 0, '+'))

    def testRectangle(self):
        self.assertEqual(read_shape("rectangle_53"), rectangle(5, 3))
        self.assertEqual(read_shape("rectangle_34"), rectangle(3, 4))

        self.assertEqual(read_shape("rectangle_34_not_filled"),
                         rectangle(3, 4, False))
        self.assertEqual(read_shape("rectangle_24_not_filled"),
                         rectangle(2, 4, False))
        self.assertEqual(read_shape("rectangle_34_indent"),
                         rectangle(3, 4, True, 2))
        self.assertEqual(read_shape("rectangle_34_x"),
                         rectangle(3, 4, True, 0, 'x'))

    def testSquare(self):
        self.assertEqual(read_shape("square"), square(5, False, 3, 'o'))

    def testParallelogram(self):
        self.assertEqual(read_shape("parallelogram_43"),
                         parallelogram(4, 3))
        self.assertEqual(read_shape("parallelogram_43_not_filled"),
                         parallelogram(4, 3, False))
        self.assertEqual(read_shape("parallelogram_43_indent"),
                         parallelogram(4, 3, True, 2))
        self.assertEqual(read_shape("parallelogram_43_x"),
                         parallelogram(4, 3, True, 0, 'x'))
        self.assertEqual(read_shape("parallelogram_43_swap"),
                         parallelogram(4, 3, True, 0, '*', -1))
        self.assertEqual(read_shape("parallelogram_43_shift2"),
                         parallelogram(4, 3, True, 0, '*', 2))
        self.assertEqual(read_shape("parallelogram_43_shift2_swap"),
                         parallelogram(4, 3, True, 0, '*', -2))

    def testRightTriangle(self):
        self.assertEqual(read_shape("triangle_3"), triangle(3))
        self.assertEqual(read_shape("triangle_5"), triangle(5))

        self.assertEqual(read_shape("triangle_5_not_filled"),
                         triangle(5, False))
        self.assertEqual(read_shape("triangle_5_indent"),
                         triangle(5, True, 2))
        self.assertEqual(read_shape("triangle_5_x"),
                         triangle(5, True, 0, 'x'))
        self.assertEqual(read_shape("triangle_5_right"),
                         triangle(5, True, 0, '*', False))
        self.assertEqual(read_shape("triangle_5_bottom_up"),
                         triangle(5, True, 0, '*', True, False))
        self.assertEqual(read_shape("triangle_5_bottom_up_right"),
                         triangle(5, True, 0, '*', False, False))
