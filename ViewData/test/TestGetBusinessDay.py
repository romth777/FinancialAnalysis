# -*- coding:utf-8 -*-
import os
import sys
import unittest

sys.path.append(os.pardir + '\\Data\\src')

import datetime
import calendar
import GetBusinessDay
import JapaneseHoliday

class TestJapaneseHoliday(unittest.TestCase):
    def test_get_business_day1(self):
        gbd = GetBusinessDay.GetBusinessDay()

        year = 2015
        month = 1
        day = 1
        delta = 365
        date = datetime.date(year, month, day)
        tmp = gbd.get_business_day(date, delta)

        for t in tmp:
            self.assertLess(calendar.weekday(t.year, t.month, t.day), 5)
            self.assertIsNone(JapaneseHoliday.holiday_name(year=t.year, month=t.month, day=t.day))
