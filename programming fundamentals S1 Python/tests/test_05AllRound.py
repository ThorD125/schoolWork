import time

from tests.IOTestCase import IOTestCase


class Tester05AllRound(IOTestCase):

    def package_name(self):
        return "exercises.topic05_allround"

    def test01_sentinel_extreme(self):
        assert_ = self.create_io_tester("assignment01_sentinel_extreme")
        assert_([0], "0 0\n")
        assert_([1, 0], "1 1\n")
        assert_([-1, 0], "-1 -1\n")
        assert_([-1, 1, 0], "-1 1\n")
        assert_([1, 2, 0], "1 2\n")
        assert_([-1, -2, 0], "-2 -1\n")

    def test02_factorial2(self):
        assert_ = self.create_io_tester("assignment02_factorial2")
        assert_([-1], "undefined\n")
        assert_([0], "1\n")
        assert_([1], "1\n")
        assert_([2], "2\n")
        assert_([3], "6\n")
        assert_([5], "120\n")

    def test03_factorial3(self):
        assert_ = self.create_io_tester("assignment03_factorial3")
        assert_([-1, 0], "1\n")
        assert_([-1, -2, 1], "1\n")
        assert_([-2, -3, -1, 2], "2\n")
        assert_([-1, -2, -3, -4, 3], "6\n")
        assert_([-1, -2, -3, -4, -5, 5], "120\n")

    def test04_variation(self):
        assert_ = self.create_io_tester("assignment04_variation")
        assert_([-1, 0], "undefined\n")
        assert_([0, -1], "undefined\n")
        assert_([5, 5], "120\n")
        assert_([20, 25], "129260083694424883200000\n")

        # Removed timed-multi-threaded execution because OS incompatibility.
        # Now: increment input size and time the execution:
        # should stay below one tenth of a second
        expected = 1
        while expected <= 100000:
            start = time.time()
            assert_([1, expected], str(expected) + "\n")
            end = time.time()
            if (end - start) > 0.1:
                self.fail("took to long !")
            expected *= 10

    def test05_sentinel_extreme_pro(self):
        assert_ = self.create_io_tester("assignment05_sentinel_extreme_pro")
        assert_([0], "0 0\n")
        assert_([1, 0], "1 1\n")
        assert_([-1, 0], "-1 -1\n")
        assert_([-1, 1, 0], "-1 1\n")
        assert_([1, 2, 0], "1 2\n")
        assert_([-1, -2, 0], "-2 -1\n")
        assert_([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "1 10\n")

    def test06_sentinel_armageddon(self):
        assert_ = self.create_io_tester("assignment06_sentinel_armageddon")
        assert_([0], "0 0\n")
        assert_([1, 0], "1 1\n")
        assert_([-1, 0], "1 1\n")
        assert_([-1, 1, 0], "1 2\n")
        assert_([1, 2, 0], "1 2\n")
        assert_([-1, -2, 0], "2 1\n")
        assert_([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "1 10\n")
