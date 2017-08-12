# -*- coding:utf-8 -*-
import os
import sys
import datetime

sys.path.append(os.pardir + "\\" + os.pardir + '\\ProcessData\\src')
import DatabaseManager
import JapaneseHoliday

class GetData:
    def __init__(self):
        self.dbm = DatabaseManager.DatabaseManager()
        pass

    def connect(self, _db_dir, _db_file):
        _db_path = _db_dir + _db_file
        return self.dbm.connect(_db_path)

    def disconnect(self, _conn):
        self.dbm.disconnect(_conn)
        pass

    def get_from_date_code(self, _conn, _date, _code):
        ret = None
        if self.dbm.check_existence(_conn, _date, _code).fetchone() is not None:
            ret = self.dbm.get_from_date_code(_conn, _date, _code)
        return ret

    def get_from_date(self, _conn, _date):
        return self.dbm.get_from_date(_conn, _date)

    def get_from_code(self, _conn, _code):
        return self.dbm.get_from_code(_conn, _code)

    def get_from_name(self, _conn, _name):
        return self.dbm.get_from_name(_conn, _name)

    def get_from_market(self, _conn, _market):
        return self.dbm.get_from_market(_conn, _market)

    def get_from_category(self, _conn, _category):
        return self.dbm.get_from_category(_conn, _category)

    # def get_today_code_list(self, _conn, _date):
    # 	self.dbm.get_from_date(_conn, _date)
    # 	return code_list

    def get_db_file_name(self, _date):

        date, space_day = GetData.get_work_date(_date)

        filename = self.dbm.get_db_name(date)
        return filename, date

    def get_db_dir(self):
        return self.dbm.get_db_dir()

    @staticmethod
    def get_work_date(_date):
        day_count = 0
        while day_count < 10:
            if _date.weekday() != 5 and _date.weekday() != 6:
                holiday_name = JapaneseHoliday.holiday_name(date=_date.date())
                if holiday_name is None:
                    break
            _date -= datetime.timedelta(days=1)
            day_count += 1
        return _date, day_count

