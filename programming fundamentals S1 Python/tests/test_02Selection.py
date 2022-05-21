import math

from tests.IOTestCase import IOTestCase


class Tester02Selection(IOTestCase):

    def package_name(self):
        return "exercises.topic02_selection"

    def test01_check_sign(self):
        assert_ = self.create_io_tester("assignment01_check_sign")
        assert_([1], "+\n")
        assert_([0], "+\n")
        assert_([-1], "-\n")
        assert_([100], "+\n")
        assert_([-100], "-\n")

    def test02_check_sign2(self):
        assert_ = self.create_io_tester("assignment02_check_sign2")
        assert_([1], "+\n")
        assert_([0], "0\n")
        assert_([-1], "-\n")
        assert_([100], "+\n")
        assert_([-100], "-\n")

    def test03_circle_surface2(self):
        assert_ = self.create_io_tester("assignment03_circle_surface2")
        assert_([10.5],
                format(10.5 * 10.5 * math.pi, '.3f') + "\n")
        assert_([-1], "?\n")

    def test04_odd(self):
        assert_ = self.create_io_tester("assignment04_odd")
        assert_([3], "odd\n")
        assert_([2], "even\n")
        assert_([1], "odd\n")
        assert_([0], "even\n")

        assert_([-3], "odd\n")
        assert_([-2], "even\n")
        assert_([-1], "odd\n")

        assert_([123], "odd\n")
        assert_([-123], "odd\n")
        assert_([246], "even\n")
        assert_([-246], "even\n")

    def test05_floating_point(self):
        assert_ = self.create_io_tester("assignment05_floating_point")

        eq = "equal\n"
        not_eq = "not equal\n"

        assert_([0.5, -0.2], eq)
        assert_([0.3, 0.0], eq)
        assert_([0.3, -0.0], eq)
        assert_([0.1, 0.2], eq)
        assert_([0.4, 0.2], not_eq)

    def test06_digit_swap(self):
        assert_ = self.create_io_tester("assignment06_digit_swap")
        assert_([1234], "1234\n")
        assert_([-1234], "-1234\n")

        assert_([-4], "-4\n")
        assert_([4], "4\n")

        assert_([34], "43\n")
        assert_([-34], "-43\n")

        assert_([70], "7\n")
        assert_([-70], "-7\n")
