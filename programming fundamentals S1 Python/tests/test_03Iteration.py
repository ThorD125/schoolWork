import os

from tests.IOTestCase import IOTestCase


def format_(nr):
    return format(nr, '.3f') + "\n"


def read_shape(fn):
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, "03Iteration_shapes", fn), 'r') as file:
        return file.read()


class Tester03Iteration(IOTestCase):

    def package_name(self):
        return "exercises.topic03_iteration"

    def test01_sum(self):
        assert_ = self.create_io_tester("assignment01_sum")
        assert_([1.4, -2.1, 3.0, -4, 0],
                format_(1.4 + -2.1 + 3.0 + -4))
        assert_([0], format_(0.0))

    def test02_count(self):
        assert_ = self.create_io_tester("assignment02_count")
        assert_([1, -2, 3, -4, 0], "4\n")

    def test03_average(self):
        assert_ = self.create_io_tester("assignment03_average")
        assert_([1.4, -2.1, 3.0, -4, 0],
                format_((1.4 + -2.1 + 3.0 + -4) / 4))
        assert_([0], "no data\n")

    def test04_all_ex(self):
        assert_ = self.create_io_tester("assignment04_all_ex")
        assert_([3], "0\n1\n2\n")

    def test05_all_in(self):
        assert_ = self.create_io_tester("assignment05_all_in")
        assert_([3], "0\n1\n2\n3\n")

    def test06_factorial(self):
        assert_ = self.create_io_tester("assignment06_factorial")
        assert_([5], "120\n")
        assert_([1], "1\n")
        assert_([0], "1\n")
        assert_([-1], "1\n")
        assert_([-5], "1\n")

    def test07_star_square(self):
        assert_ = self.create_io_tester("assignment07_star_rectangle")
        assert_([3, 4], read_shape("rectangle_34"))
        assert_([4, 3], read_shape("rectangle_43"))
        assert_([4, 0], "")
        assert_([0, 3], "")
        assert_([0, 0], "")

    def test08_isosceles1(self):
        assert_ = self.create_io_tester("assignment08_isosceles1")
        assert_([3], read_shape("isosceles1_3"))
        assert_([-1, -2, 0, 3], read_shape("isosceles1_3"))

    def test09_isosceles2(self):
        assert_ = self.create_io_tester("assignment09_isosceles2")
        assert_([3], read_shape("isosceles2_3"))
        assert_([-1, -2, 0, 3], read_shape("isosceles2_3"))

    def test10_isosceles3(self):
        assert_ = self.create_io_tester("assignment10_isosceles3")
        assert_([3], read_shape("isosceles3_3"))
        assert_([-1, -2, 0, 3], read_shape("isosceles3_3"))

    def test11_isosceles4(self):
        assert_ = self.create_io_tester("assignment11_isosceles4")
        assert_([3], read_shape("isosceles4_3"))
        assert_([-1, -2, 0, 3], read_shape("isosceles4_3"))

    def test12_isosceles5(self):
        assert_ = self.create_io_tester("assignment12_isosceles5")
        assert_([5], read_shape("isosceles5_5"))
        assert_([-1, -2, 0, 5], read_shape("isosceles5_5"))

        assert_([6], read_shape("isosceles5_6"))
        assert_([-1, -2, 0, 6], read_shape("isosceles5_6"))

    def test13_isosceles6(self):
        assert_ = self.create_io_tester("assignment13_isosceles6")
        assert_([5], read_shape("isosceles6_5"))
        assert_([-1, -2, 0, 5], read_shape("isosceles6_5"))

        assert_([6], read_shape("isosceles6_6"))
        assert_([-1, -2, 0, 6], read_shape("isosceles6_6"))

    def test14_euclid(self):
        assert_ = self.create_io_tester("assignment14_euclid")
        assert_([225, 15], "15\n")
        assert_([15, 12], "3\n")
        assert_([15, 225], "15\n")
        assert_([12, 15], "3\n")

    def test15_digit_swap2(self):
        assert_ = self.create_io_tester("assignment15_digit_swap2")
        assert_([1234], "4321\n")
        assert_([-1234], "-4321\n")
        assert_([0], "0\n")
        assert_([6], "6\n")
        assert_([-6], "-6\n")
        assert_([700], "7\n")
        assert_([-700], "-7\n")

    def test16_centered_square(self):
        assert_ = self.create_io_tester("assignment16_centered_square")
        assert_([3], read_shape("centered_square_3"))
        assert_([5], read_shape("centered_square_5"))
        assert_([7], read_shape("centered_square_7"))

        assert_([0, 2, 3], read_shape("centered_square_3"))
        assert_([0, 1, 2, 3], read_shape("centered_square_3"))
        assert_([-1, 0, 1, 2, 3], read_shape("centered_square_3"))

    def test17_square_of_numbers(self):
        assert_ = self.create_io_tester("assignment17_square_of_numbers")
        assert_([-1], "No Output\n")
        assert_([0], "No Output\n")
        assert_([1], "No Output\n")
        assert_([10], "No Output\n")
        assert_([9], read_shape("square_of_numbers"))
