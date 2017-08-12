# -*- coding:utf-8 -*-
import os
import sys
import glob
sys.path.append(os.pardir + '\\ProcessData\\src')
import RefineData
import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas as pd
import JapaneseHoliday


class DataToJson:
    data_index = ["date", "code", "market", "name", "category", "start", "end", "min", "max", "volume", "sales"]

    def __init__(self):
        self.rd = RefineData.RefineData()
        pass

    def show_date_data(self, _db_dir, _db_file, _date):
        return self.rd.get_date_data(_db_dir, _db_file, _date)

if __name__ == '__main__':
    import os
    import datetime
    average_day = [5, 25, 75]
    span_day = 30
    # 暫定で50足す
    data_span_day = 30 + max(average_day) + 50
    code = "4324-T"
    if int(datetime.datetime.today().hour) <= 19:
        today = datetime.datetime.today() - datetime.timedelta(days=1)
    else:
        today = datetime.datetime.today()

    day_count = 0
    view_day = today
    while day_count < 10:
        if view_day.weekday() == 5 or view_day.weekday() == 6:
            view_day = view_day - datetime.timedelta(days=day_count)
        else:
            holiday_name = JapaneseHoliday.holiday_name(date=today.date())
            if holiday_name is not None:
                view_day = view_day - datetime.timedelta(days=day_count)
            else:
                break
        day_count += 1

    start_day = view_day - datetime.timedelta(days=data_span_day)
    file_list = []
    for i in range(data_span_day + 1):
        tmp_day = start_day + datetime.timedelta(days=i)
        if int(tmp_day.day) < 16:
            half = "01"
        else:
            half = "02"
        year_month = tmp_day.strftime("%Y-%m")
        if (year_month + "_" + half) not in file_list:
            file_list.append(year_month + "_" + half)
    db_dir = os.path.split(os.path.split(os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0])[0])[0] + '\\data\\kdb\\stocks\\db\\'
    shd = DataToJson()

    if int(view_day.day) < 16:
        half = "01"
    else:
        half = "02"
    db_file = view_day.strftime("%Y-%m") + "_" + half + "_stocks.db"
    ret = shd.show_date_data(db_dir, db_file, view_day)
    ret = ret