from unittest import TestCase

from exercises.topic06_functions.assignment04 import *


class Tester06Functions4(TestCase):

    def testInDutchBelow10(self):
        self.assertEqual('nul', to_dutch(0))
        self.assertEqual('negen', to_dutch(9))

    def testInDutchBelow100(self):
        self.assertEqual('achttien', to_dutch(18))
        self.assertEqual('zevenenvijftig', to_dutch(57))
        self.assertEqual('tweeëntwintig', to_dutch(22))

    def testInDutchBelow1000(self):
        self.assertEqual('honderdtien', to_dutch(110))  # !!!
        self.assertEqual('driehonderdvijftien', to_dutch(315))
        self.assertEqual('driehonderddrieëndertig', to_dutch(333))
        self.assertEqual('driehonderd', to_dutch(300))
        self.assertEqual('driehonderdenzeven', to_dutch(307))

    def testInDutch(self):
        self.assertEqual('zevenhonderdeenentachtig miljoen '
                         'vierhonderdtweeënvijftigduizend '
                         'driehonderdeenentwintig',
                         to_dutch(781452321))
        self.assertEqual('min '
                         'zevenhonderdeenentachtig miljoen '
                         'vierhonderdtweeënvijftigduizend '
                         'driehonderdeenentwintig',
                         to_dutch(-781452321))
