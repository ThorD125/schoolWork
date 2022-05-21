"""
Implements the functions
`is_leap_year`,
`number_of_days_in_month`,
`number_of_days_in_year`,
`number_of_day` (compute the number of days until this day in a year), and
`date_diff_in_days`
such that all tests succeed.

If the functionality you need already exists in
(a) Python (library), try to implement it yourself.
The exercise here is to write code, not to borrow it.
"""

number_of_days_in_month_data = {
    True: [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],  # leap year
    False: [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # non leap year
}
# TODO


def is_leap_year(year):
    if str(year)[-2:] == "00":
        if year % 400 == 0:
            return True
    elif year % 4 == 0:
        return True
    return False


def number_of_days_in_month(year, month):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month % 2 == 0:
        return 30
    else:
        return 31


def number_of_days_in_year(year):
    if is_leap_year(year):
        return 366
    else:
        return 365


def number_of_day(year, month, day):
    the_day = 0
    for i in range(month-1):
        # print(i+1)
        the_day += number_of_days_in_month(year, i + 1)
    return the_day + day


def date_diff_in_days(year1, month1, day1, year2, month2, day2):
    # print(number_of_day(year1, month1, day1))
    # print(number_of_day(year2, month2, day2))
    negative = False
    if year1 > year2:
        year1, year2 = year2, year1
        month1, month2 = month2, month1
        day1, day2 = day2, day1
        negative = True

    a = number_of_day(year2, month2, day2)
    b = number_of_day(year1, month1, day1)
    # print(a, b)
    totalyears = 0
    for year in range(year1, year2):
        # print(year)
        # print(number_of_days_in_year(year))
        totalyears += number_of_days_in_year(year)

    if negative:
        return -1 * (a - b + totalyears)

    return a - b + totalyears
