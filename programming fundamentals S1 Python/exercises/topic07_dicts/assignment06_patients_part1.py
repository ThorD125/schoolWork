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

# Find Indexes
Write (two) functions `index_of_first_symptomatic_day(patient_logbook)` and
`index_of_last_symptomatic_day(patient_logbook)`
which look for the **index** on which the first symptom ever presented
itself and the **index** in which the last symptom
ever presented itself, respectively.

Make use of the tests to figure out how your functions should behave in
edge cases.

# Find Dates
Now, also write the two functions `first_symptomatic_day(patient_logbook)` and
`last_symptomatic_day(patient_logbook)` which return dates instead of indexes.

*Write as little new code as possible.*
"""
# TODO
import math


def index_of_first_symptomatic_day(patient_logbook):
    x = 0
    while x < len(patient_logbook):
        if patient_logbook[x]["symptoms"]:
            return x
        x += 1
    return math.nan


def first_symptomatic_day(patient_logbook):
    for x in patient_logbook:
        if x["symptoms"]:
            return x["date"]
    return math.nan


def index_of_last_symptomatic_day(patient_logbook):
    x = len(patient_logbook) - 1
    while x > 0:
        if patient_logbook[x]["symptoms"]:
            return x
        x -= 1
    return math.nan


def last_symptomatic_day(patient_logbook):
    return first_symptomatic_day(reversed(patient_logbook))
