"""
# Symptoms (exam 2020-2021)
This whole assignment is about log books of patients, in which
one can see whether or not the patient showed symptoms on any give date.

`{"date": "2021/12/31", "symptoms": False}` implies that the patient
did not show any symptoms on the thirty-first of December.

`{"date": "2021/12/31", "symptoms": True}` implies that the patient
did show symptoms on the thirty-first of December.

One such piece of information is what we call an entry
(pl.: entries) in this assignment.

You can assume that the entries in these log books are **always sorted
by date** and that the log books are complete. Here, complete means
that you will find one entry for every day between the start date
and the and date. In other words, the dates in these entries do not
show any holes or jumps.

Using such a log book with the history of symptoms, we can partition
the entries in three periods: incubation, sickness, and recovered.
If you do not understand, we can show you an example table that
visualizes this exactly.

===

Write the function `had_symptoms(patient_logbook, date)`
which checks whether a patient was showing symptoms on a given date.
*Do this using the most efficient technique you know (minimise the
number of steps in your search)*.

Note that there are only 10 entries in this example but that this could be
many many more in a real case. The entries are sorted by date however.

Note that dates are represented by `strings` in this assignment
(e.g. `"2021/01/02"`).
By using this somewhat odd representation (first year, then month, then day),
we can use simple string comparisons to compare dates.

This means  `<`, `==`, `>` can be used to determine order.
(just like for numbers)

`d1 < d2` is (only) true when `d1` happens before `d2`.

`d1 == d2` is true when `d1` and `d2` represent the exact same date.

`d1 > d2` is (only) true when `d1` happens after `d2`.
"""
# TODO


def had_symptoms(x=None, y=None, z=None):
    return x


# for entry in my_test_data_1:
#    print(entry["symptoms"], had_symptoms(my_test_data_1, entry["date"]))

# print(False, had_symptoms(my_test_data_1, "2020/12"))
# print(False, had_symptoms(my_test_data_1, "2021/11"))
