# -*- coding:utf-8 -*-
import os
import sys
sys.path.append(os.pardir + '\\ProcessData\\src')
import GetData
import StockDataTag
from pandas import DataFrame
import datetime
import pandas as pd


class RefineData:
        def __init__(self):
            self.gd = GetData.GetData()
            self.sdt = StockDataTag.StockDataTag()
            self.data_index = ["date", "code", "market", "name", "category", "start", "end", "min", "max", "volume", "sales"]
            pass

        def get_code_data(self, _db_dir, _db_file, _code):
            conn = self.gd.connect(_db_dir, _db_file)
            row = self.gd.get_from_code(conn, _code)
            data_all = row.fetchall()
            s1 = DataFrame(data_all, columns=self.data_index)
            s1 = s1.set_index("date")
            # for i in range(len(data_all)):
            #     tmp = [data_all[i]]
            #     s1 = s1.append(DataFrame(tmp, columns=self.data_index, index=[tmp[0][0]]))
            self.gd.disconnect(conn)
            return s1

        def get_code_data_date_index(self, _db_dir, _db_file, _code):
            conn = self.gd.connect(_db_dir, _db_file)
            row = self.gd.get_from_code(conn, _code)
            data_all = row.fetchall()
            s1 = DataFrame(data_all, columns=self.data_index)
            date_list = []
            for i in range(len(s1)):
                date_list.append(datetime.datetime.strptime(s1.irow(i)["date"], '%Y-%m-%d'))
            s2 = DataFrame(data_all, columns=self.data_index, index=date_list)
            # for i in range(len(data_all)):
            #     tmp = [data_all[i]]
            #     s1 = s1.append(DataFrame(tmp, columns=self.data_index, index=[tmp[0][0]]))
            self.gd.disconnect(conn)
            return s2

        def get_date_data(self, _db_dir, _db_file, _date):
            conn = self.gd.connect(_db_dir, _db_file)
            if isinstance(_date, str):
                row = self.gd.get_from_date(conn, _date)
            elif isinstance(_date, datetime.datetime):
                row = self.gd.get_from_date(conn, _date.strftime('%Y-%m-%d'))
            else:
                return None
            data_all = row.fetchall()
            s1 = DataFrame(data_all, columns=self.data_index)
            s1 = s1.set_index("date")
            # for i in range(len(data_all)):
            #     tmp = [data_all[i]]
            #     s1 = s1.append(DataFrame(tmp, columns=self.data_index, index=[tmp[0][0]]))
            self.gd.disconnect(conn)
            return s1

        def get_ohlc(self, _db_dir, _date, _days, _code=None):
            gd = GetData.GetData()
            if isinstance(_date, str):
                _date = datetime.datetime.strptime(_date, "%Y-%m-%d")

            s1 = DataFrame(columns=self.data_index)

            sum_space_day = 0
            for i_day in range(_days):
                tmp_date, space_day = self.gd.get_work_date(_date - datetime.timedelta(days=i_day + sum_space_day))
                sum_space_day += space_day

                db_file, date = gd.get_db_file_name(tmp_date)
                db_file += "_stocks.db"

                conn = self.gd.connect(_db_dir, db_file)
                if _code is None:
                    row = self.gd.get_from_date(conn, tmp_date.strftime('%Y-%m-%d'))
                elif _code is not None:
                    row = self.gd.get_from_date_code(conn, tmp_date.strftime('%Y-%m-%d'), _code)
                else:
                    return None

                data_all = row.fetchall()
                for i in range(len(data_all)):
                    tmp = [data_all[i]]
                    s1 = s1.append(DataFrame(tmp, columns=self.data_index))
                self.gd.disconnect(conn)

            s1 = s1.set_index("date")

            return s1

        def get_db_dir(self):
            return self.gd.get_db_dir()

        def get_rolling_mean(self, _data, _day):
            _data = _data.sort_index(ascending=True)
            start = pd.rolling_mean(_data["start"], _day)
            end = pd.rolling_mean(_data["end"], _day)
            max = pd.rolling_mean(_data["max"], _day)
            min = pd.rolling_mean(_data["min"], _day)
            volume = pd.rolling_mean(_data["volume"], _day)

            ret = pd.concat([start, end, max, min, volume], axis=1)
            ret = ret.sort_index(ascending=False)

            return ret

        def get_work_date(self, _date):
            return self.gd.get_work_date(_date)

        # date:開始日/span:日数
        def get_last_work_date(self, _date, _span):
            if isinstance(_date, str):
                _date = datetime.datetime.strptime(_date, "%Y-%m-%d")
            sum_space_day = 0
            for i_day in range(_span):
                tmp_date, space_day = self.gd.get_work_date(_date - datetime.timedelta(days=i_day + sum_space_day))
                sum_space_day += space_day
            return tmp_date


