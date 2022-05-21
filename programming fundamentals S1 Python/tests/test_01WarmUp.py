import math

from tests.IOTestCase import IOTestCase


class Tester01WarmUp(IOTestCase):

    def package_name(self):
        return "exercises.topic01_warm_up"

    def test01_hello_world(self):
        assert_ = self.create_io_tester("assignment01_hello_world")
        assert_([], "Hello, World!\n")

    def test02_echo(self):
        assert_ = self.create_io_tester("assignment02_echo")
        assert_([123], "123\n")
        assert_(["azerty"], "azerty\n")
        assert_([1.4], "1.4\n")

    def test03_3x4_stars(self):
        assert_ = self.create_io_tester("assignment03_3x4_stars")
        assert_([],
                "****\n****\n****\n")

    def test04_swap(self):
        assert_ = self.create_io_tester("assignment04_swap")
        self.assertOutputEqual("assignment04_swap", [1, 2], "2 1\n")

    def test05_swap2(self):
        assert_ = self.create_io_tester("assignment05_swap2")
        assert_([1, 2], "2 1\n")
        assert_([-1, -2], "-2 -1\n")
        assert_([1, -2], "-2 1\n")
        assert_([-1, 2], "2 -1\n")

    def test06_circle_surface(self):
        assert_ = self.create_io_tester("assignment06_circle_surface")
        assert_([10.5],
                format(10.5 * 10.5 * math.pi, '.3f') + "\n")

    def test07_reverse_sequence(self):
        assert_ = self.create_io_tester("assignment07_reverse_sequence")
        assert_([1, 2, 3, 4, 5],
                "5\n4\n3\n2\n1\n")
