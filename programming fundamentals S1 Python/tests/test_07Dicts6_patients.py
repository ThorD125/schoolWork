import math
from unittest import TestCase

from exercises.topic07_dicts.assignment06_patients_part1 import \
    index_of_first_symptomatic_day, \
    index_of_last_symptomatic_day
from exercises.topic07_dicts.assignment06_patients_part1 import \
    first_symptomatic_day, \
    last_symptomatic_day
from exercises.topic07_dicts.assignment06_patients_part2 import \
    get_incubation_days, \
    get_sickness_days, \
    get_recovered_days
from exercises.topic07_dicts.assignment06_patients_part3 import \
    had_symptoms

my_test_data_1 = [
    {"date": "2021/01/01", "symptoms": False},
    {"date": "2021/01/02", "symptoms": False},
    {"date": "2021/01/03", "symptoms": False},
    {"date": "2021/01/04", "symptoms": False},
    {"date": "2021/01/05", "symptoms": True},
    {"date": "2021/01/06", "symptoms": False},
    {"date": "2021/01/07", "symptoms": False},
    {"date": "2021/01/08", "symptoms": True},
    {"date": "2021/01/09", "symptoms": True},
    {"date": "2021/01/10", "symptoms": False}
]

my_test_data_2 = [
    {"date": "2021/01/01", "symptoms": False},
    {"date": "2021/01/02", "symptoms": True},
    {"date": "2021/01/03", "symptoms": True},
    {"date": "2021/01/04", "symptoms": False},
    {"date": "2021/01/05", "symptoms": True},
    {"date": "2021/01/06", "symptoms": False},
    {"date": "2021/01/07", "symptoms": False},
    {"date": "2021/01/08", "symptoms": False},
    {"date": "2021/01/09", "symptoms": False},
    {"date": "2021/01/10", "symptoms": False}
]

my_test_data_3 = [
    {"date": "2021/01/01", "symptoms": False},
    {"date": "2021/01/02", "symptoms": False},
    {"date": "2021/01/03", "symptoms": False},
    {"date": "2021/01/04", "symptoms": False},
    {"date": "2021/01/05", "symptoms": False},
    {"date": "2021/01/06", "symptoms": False},
    {"date": "2021/01/07", "symptoms": False},
    {"date": "2021/01/08", "symptoms": True},
    {"date": "2021/01/09", "symptoms": False},
    {"date": "2021/01/10", "symptoms": True}
]

my_test_data_no_symptoms = [
    {"date": "2021/01/01", "symptoms": False},
    {"date": "2021/01/02", "symptoms": False},
    {"date": "2021/01/03", "symptoms": False},
    {"date": "2021/01/04", "symptoms": False},
    {"date": "2021/01/05", "symptoms": False},
    {"date": "2021/01/06", "symptoms": False},
    {"date": "2021/01/07", "symptoms": False},
    {"date": "2021/01/08", "symptoms": False},
    {"date": "2021/01/09", "symptoms": False},
    {"date": "2021/01/10", "symptoms": False}
]


class TesterLocal(TestCase):

    def test_index_of_first_symptomatic_day(self):
        self.assertEqual(4, index_of_first_symptomatic_day(my_test_data_1))
        self.assertEqual(1, index_of_first_symptomatic_day(my_test_data_2))

        self.assertTrue(math.isnan(
            index_of_first_symptomatic_day(my_test_data_no_symptoms)
        ))

    def test_first_symptomatic_day(self):
        self.assertEqual("2021/01/05",
                         first_symptomatic_day(my_test_data_1))

        self.assertEqual("2021/01/02",
                         first_symptomatic_day(my_test_data_2))

        self.assertTrue(math.isnan(
            index_of_first_symptomatic_day(my_test_data_no_symptoms)
        ))

    def test_index_of_last_symptomatic_day(self):
        self.assertEqual(8, index_of_last_symptomatic_day(my_test_data_1))
        self.assertEqual(4, index_of_last_symptomatic_day(my_test_data_2))

        self.assertTrue(math.isnan(
            index_of_last_symptomatic_day(my_test_data_no_symptoms)
        ))

    def test_last_symptomatic_day(self):
        self.assertEqual("2021/01/09", last_symptomatic_day(my_test_data_1))
        self.assertEqual("2021/01/05", last_symptomatic_day(my_test_data_2))

        self.assertTrue(math.isnan(
            index_of_last_symptomatic_day(my_test_data_no_symptoms)
        ))

    def test_get_incubation_days(self):
        expected = [
            {"date": "2021/01/01", "symptoms": False},
            {"date": "2021/01/02", "symptoms": False},
            {"date": "2021/01/03", "symptoms": False},
            {"date": "2021/01/04", "symptoms": False}
        ]
        self.assertEqual(expected, get_incubation_days(my_test_data_1))
        self.assertEqual([], get_incubation_days(my_test_data_no_symptoms))

    def test_get_sickness_days(self):
        expected = [
            {"date": "2021/01/05", "symptoms": True},
            {"date": "2021/01/06", "symptoms": False},
            {"date": "2021/01/07", "symptoms": False},
            {"date": "2021/01/08", "symptoms": True},
            {"date": "2021/01/09", "symptoms": True}
        ]
        self.assertEqual(expected, get_sickness_days(my_test_data_1))
        self.assertEqual([], get_sickness_days(my_test_data_no_symptoms))

    def test_get_recovered_days(self):
        expected = [
            {"date": "2021/01/10", "symptoms": False}
        ]
        self.assertEqual(expected, get_recovered_days(my_test_data_1))
        self.assertEqual([], get_recovered_days(my_test_data_3))
        self.assertEqual([], get_recovered_days(my_test_data_no_symptoms))

    def test_had_symptoms(self):
        for entry in my_test_data_1:
            self.assertEqual(
                entry["symptoms"],
                had_symptoms(my_test_data_1, entry["date"])
            )

        self.assertFalse(had_symptoms(my_test_data_1, "2020/12"))
        self.assertFalse(had_symptoms(my_test_data_1, "2021/11"))
