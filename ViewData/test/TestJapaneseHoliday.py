# -*- coding:utf-8 -*-
import os
import sys
import unittest

sys.path.append(os.pardir + '\\Data\\src')

import datetime
import calendar
import JapaneseHoliday


class TestJapaneseHoliday(unittest.TestCase):
    def test_holiday_name_2014(self):
        holiday = [[2014, 1, 1, '元日'],
                        [2014, 1, 2, '正月'],
                        [2014, 1, 3, '正月'],
                        [2014, 1, 13, '成人の日'],
                        [2014, 2, 11, '建国記念の日'],
                        [2014, 3, 21, '春分の日'],
                        [2014, 4, 29, '昭和の日'],
                        [2014, 5, 3, '憲法記念日'],
                        [2014, 5, 4, 'みどりの日'],
                        [2014, 5, 5, 'こどもの日'],
                        [2014, 5, 6, '振替休日'],
                        [2014, 7, 21, '海の日'],
                        [2014, 9, 15, '敬老の日'],
                        [2014, 9, 23, '秋分の日'],
                        [2014, 10, 13, '体育の日'],
                        [2014, 11, 3, '文化の日'],
                        [2014, 11, 23, '勤労感謝の日'],
                        [2014, 11, 24, '振替休日'],
                        [2014, 12, 23, '天皇誕生日'],
                        [2014, 12, 31, '大晦日']]
        holiday_count = 0
        year = 2014
        for month in range(1, 13):
            for day in range(1, calendar.monthrange(year, month)[1]):
                date = datetime.date(year, month, day)
                if year == holiday[holiday_count][0] and month == holiday[holiday_count][1] and day == holiday[holiday_count][2]:
                    self.assertEquals(holiday[holiday_count][3], JapaneseHoliday.holiday_name(date=date))
                    self.assertEquals(holiday[holiday_count][3], JapaneseHoliday.holiday_name(year=year, month=month, day=day))
                    if holiday_count < len(holiday) - 1:
                        holiday_count += 1
                else:
                    self.assertIsNone(JapaneseHoliday.holiday_name(date=date))
                    self.assertIsNone(JapaneseHoliday.holiday_name(year=year, month=month, day=day))

    def test_holiday_name_2015(self):
        holiday = [[2015, 1, 1, '元日'],
                        [2015, 1, 2, '正月'],
                        [2015, 1, 3, '正月'],
                        [2015, 1, 12, '成人の日'],
                        [2015, 2, 11, '建国記念の日'],
                        [2015, 3, 21, '春分の日'],
                        [2015, 4, 29, '昭和の日'],
                        [2015, 5, 3, '憲法記念日'],
                        [2015, 5, 4, 'みどりの日'],
                        [2015, 5, 5, 'こどもの日'],
                        [2015, 5, 6, '振替休日'],
                        [2015, 7, 20, '海の日'],
                        [2015, 9, 21, '敬老の日'],
                        [2015, 9, 22, '国民の休日'],
                        [2015, 9, 23, '秋分の日'],
                        [2015, 10, 12, '体育の日'],
                        [2015, 11, 3, '文化の日'],
                        [2015, 11, 23, '勤労感謝の日'],
                        [2015, 12, 23, '天皇誕生日'],
                        [2015, 12, 31, '大晦日']]
        holiday_count = 0
        year = 2015
        for month in range(1, 13):
            for day in range(1, calendar.monthrange(year, month)[1]):
                date = datetime.date(year, month, day)
                print(date)
                if year == holiday[holiday_count][0] and month == holiday[holiday_count][1] and day == holiday[holiday_count][2]:
                    self.assertEquals(holiday[holiday_count][3], JapaneseHoliday.holiday_name(date=date))
                    self.assertEquals(holiday[holiday_count][3], JapaneseHoliday.holiday_name(year=year, month=month, day=day))
                    if holiday_count < len(holiday) - 1:
                        holiday_count += 1
                else:
                    self.assertIsNone(JapaneseHoliday.holiday_name(date=date))
                    self.assertIsNone(JapaneseHoliday.holiday_name(year=year, month=month, day=day))
