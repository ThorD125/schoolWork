from unittest import TestCase

from exercises.topic06_functions.assignment05 import *


class Tester06Functions4(TestCase):

    def testIsLeapYear(self):
        self.assertTrue(is_leap_year(2016))
        self.assertFalse(is_leap_year(2017))
        self.assertFalse(is_leap_year(1997))
        self.assertTrue(is_leap_year(1996))
        self.assertFalse(is_leap_year(1900))
        self.assertTrue(is_leap_year(2000))

    def testNumberOfDaysIn(self):
        self.assertEqual(28, number_of_days_in_month(2017, 2))
        self.assertEqual(29, number_of_days_in_month(2016, 2))
        self.assertEqual(31, number_of_days_in_month(1996, 7))
        self.assertEqual(365, number_of_days_in_year(1997))
        self.assertEqual(366, number_of_days_in_year(1996))

    def testNumberOfDay(self):
        self.assertEqual(365, number_of_day(2017, 12, 31))
        self.assertEqual(366, number_of_day(2016, 12, 31))
        self.assertEqual(1, number_of_day(2016, 1, 1))
        self.assertEqual(90, number_of_day(2017, 3, 31))
        self.assertEqual(91, number_of_day(2016, 3, 31))

    def testDateDiffInDays(self):
        self.assertEqual(0, date_diff_in_days(2017, 1, 1, 2017, 1, 1))
        self.assertEqual(1, date_diff_in_days(2017, 1, 1, 2017, 1, 2))
        self.assertEqual(2, date_diff_in_days(2017, 1, 1, 2017, 1, 3))
        self.assertEqual(730, date_diff_in_days(2015, 4, 1, 2017, 3, 31))
        self.assertEqual(-730, date_diff_in_days(2017, 3, 31, 2015, 4, 1))
        self.assertEqual(89, date_diff_in_days(2017, 1, 1, 2017, 3, 31))
        self.assertEqual(-89, date_diff_in_days(2017, 3, 31, 2017, 1, 1))
        self.assertEqual(90, date_diff_in_days(2016, 1, 1, 2016, 3, 31))
        self.assertEqual(-90, date_diff_in_days(2016, 3, 31, 2016, 1, 1))
