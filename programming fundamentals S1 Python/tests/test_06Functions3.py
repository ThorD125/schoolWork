from unittest import TestCase

from exercises.topic06_functions.assignment03 import *


class Tester06Functions3(TestCase):

    def testReverse(self):
        self.assertEqual('', reverse(''))
        self.assertEqual('lab', reverse('bal'))

    def testIsPalindrome(self):
        self.assertTrue(is_palindrome('aibohphobia'))
        self.assertFalse(is_palindrome('test'))
        self.assertTrue(is_palindrome(''))

    def testSubString(self):
        self.assertEqual('', sub_str('voetbalveld', 0, 0))
        self.assertEqual('', sub_str('voetbalveld', 11, 1))
        self.assertEqual('voet', sub_str('voetbalveld', 0, 4))
        self.assertEqual('bal', sub_str('voetbalveld', 4, 3))
        self.assertEqual('veld', sub_str('voetbalveld', 7, 4))

    def testSubStringWithNegativeValues(self):
        self.assertEqual('voet', sub_str('voetbalveld', -11, 4))
        self.assertEqual('bal', sub_str('voetbalveld', -7, 3))

        self.assertEqual('bal', sub_str('voetbalveld', 7, -3))
        self.assertEqual('', sub_str('voetbalveld', 0, -1))
        self.assertEqual('veld', sub_str('voetbalveld', 11, -4))

        self.assertEqual('', sub_str('voetbalveld', -11, -1))
        self.assertEqual('', sub_str('voetbalveld', -15, -1))
        self.assertEqual('bal', sub_str('voetbalveld', -4, -3))

    def testFind(self):
        self.assertEqual(4, find('bal', 'voetbalbal'))
        self.assertEqual(4, find('bal', 'voetbalbal', 4))
        self.assertEqual(7, find('bal', 'voetbalbal', 5))
        self.assertEqual(0, find('haha', 'hahaha'))
        self.assertEqual(2, find('haha', 'hahaha', 1))
        self.assertEqual(-1, find('haha', 'hahaha', 3))
        self.assertEqual(-1, find('haha', 'ha'))

    def testFindAll(self):
        self.assertEqual([0, 2, 4], find_all('ha', 'hahaha'))
        self.assertEqual([0, 2], find_all('haha', 'hahaha'))
        self.assertEqual([0, 6, 8], find_all('haha', 'hahahihahahahihiha'))

    def testFindAllWithoutOverlap(self):
        self.assertEqual([0], find_all('haha', 'hahaha', False))
        self.assertEqual([0, 6], find_all('haha', 'hahahihahahahihiha', False))

    def testReplace(self):
        self.assertEqual('voetloblob', replace('bal', 'lob', 'voetbalbal'))
        self.assertEqual('voet', replace('bal', '', 'voetbalbal'))
        self.assertEqual('balbal', replace('voet', '', 'voetbalbal'))
        self.assertEqual('voetbalbal', replace('sok', 'lob', 'voetbalbal'))
        self.assertEqual('hohoha', replace('haha', 'hoho', 'hahaha'))

    def testDecompose(self):
        self.assertEqual([1, 0, 2, 0, 3], decompose(30201))
