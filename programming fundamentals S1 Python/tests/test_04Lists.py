from tests.IOTestCase import IOTestCase


class Tester04Lists(IOTestCase):

    def package_name(self):
        return "exercises.topic04_lists"

    def test01_reverse_sequence_hell(self):
        assert_ = self.create_io_tester("assignment01_reverse_sequence")
        r = range(0, 100)
        assert_(r, "\n".join(map(str, reversed(r))) + "\n")

    def test02_highest_frequency(self):
        assert_ = self.create_io_tester("assignment02_highest_frequency")
        assert_([1, 3, 2, 1, 3, 5, 3, 1, 678], "1\n")
        assert_([50, 3, 2, 50, 3, 5, 3, 50, 678], "3\n")
        assert_([50, 3, 2, 50, 3, 5, 3, 50, 50, 678], "50\n")
        assert_([99, 3, 2, 99, 3, 5, 3, 99, 678], "3\n")
        assert_([99, 3, 2, 99, 3, 5, 99, 3, 99, 678], "99\n")

        assert_([-1], "-1\n")
        assert_([123], "-1\n")

    def test03_highest_frequency2(self):
        assert_ = self.create_io_tester("assignment03_highest_frequency2")
        assert_([1, 3, 2, 1, 3, 5, 3, 1, 678], "3\n")
        assert_([50, 3, 2, 50, 3, 5, 3, 50, 678], "50\n")
        assert_([50, 3, 2, 50, 3, 5, 3, 50, 50, 678], "50\n")
        assert_([99, 3, 2, 99, 3, 5, 3, 99, 678], "99\n")
        assert_([99, 3, 2, 99, 3, 5, 99, 3, 99, 678], "99\n")

        assert_([-1], "-1\n")
        assert_([123], "-1\n")

    def test04_highest_frequency3(self):
        assert_ = self.create_io_tester("assignment04_highest_frequency3")
        assert_([1, 3, 2, 1, 3, 5, 3, 1, 678], "1\n3\n")
        assert_([50, 3, 2, 50, 3, 5, 3, 50, 678], "3\n50\n")
        assert_([50, 3, 2, 50, 3, 5, 3, 50, 50, 678], "50\n")
        assert_([99, 3, 2, 99, 3, 5, 3, 99, 678], "3\n99\n")
        assert_([99, 3, 2, 99, 3, 5, 99, 3, 99, 678], "99\n")

        assert_([99, 3, 2, 99, 3, 5, 3, 99, 12, 12, 12, 678],
                "3\n12\n99\n")

        assert_([-1], "-1\n")
        assert_([123], "-1\n")

    def test05_count_sort(self):
        assert_ = self.create_io_tester("assignment05_count_sort")
        assert_([3, 2, 1, 3, 5, 3, 1, -10], "[1, 2, 3, 5]\n")

    def test06_count_sort2(self):
        assert_ = self.create_io_tester("assignment06_count_sort2")
        assert_([3, 2, 1, 5, -10], "[1, 2, 3, 5]\n")
        assert_([3, 2, 1, 3, 5, 3, 1, -10], "[1, 1, 2, 3, 3, 3, 5]\n")

    def test07_sieve_of_eratosthenes(self):
        assert_ = self.create_io_tester("assignment07_eratosthenes")
        assert_([14], "2\n3\n5\n7\n11\n13\n")

    def test07_battleship(self):
        assert_ = self.create_io_tester("assignment08_battleship")
        damage = "Damage: 0.50"
        efficiency = "Efficiency: 0.50"
        assert_([], damage + "\n" + efficiency + "\n")
