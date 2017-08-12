# -*- coding:utf-8 -*-
import os
import sys
import unittest

sys.path.append('../src')
import DatabaseManager
import StockData


class TestDatabaseManager(unittest.TestCase):
    def test_set_data1(self):
        dbm = DatabaseManager.DatabaseManager()
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testSetData1.db'
        if os.path.isfile(name):
            os.remove(name)
        conn = dbm.connect(name)
        sd = StockData.StockData()
        tmp = ["2015年01月01日", "9999", "市場", "銘柄名", "業種", 100, 200, 99, 250, 12334, 1002201]
        sd.set_date(tmp[0])
        sd.set_code(tmp[1])
        sd.set_name(tmp[3])
        sd.set_market(tmp[2])
        sd.set_category(tmp[4])
        sd.set_start(tmp[5])
        sd.set_end(tmp[6])
        sd.set_min(tmp[7])
        sd.set_max(tmp[8])
        sd.set_volume(tmp[9])
        sd.set_sales(tmp[10])
        dbm.set_data(conn, sd)
        cur = dbm.check_existence(conn, tmp[0], tmp[1])
        row = cur.fetchone()
        dbm.disconnect(conn)
        self.assertNotEquals(row, None)

    def test_get_from_date_code1(self):
        dbm = DatabaseManager.DatabaseManager()
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testGetDataOfDateCodeData1.db'
        if os.path.isfile(name):
            os.remove(name)
        conn = dbm.connect(name)
        sd = StockData.StockData()
        tmp = ["2015年01月01日", "9999", "市場", "銘柄名", "業種", 100, 200, 99, 250, 12334, 1002201]
        sd.set_date(tmp[0])
        sd.set_code(tmp[1])
        sd.set_name(tmp[3])
        sd.set_market(tmp[2])
        sd.set_category(tmp[4])
        sd.set_start(tmp[5])
        sd.set_end(tmp[6])
        sd.set_min(tmp[7])
        sd.set_max(tmp[8])
        sd.set_volume(tmp[9])
        sd.set_sales(tmp[10])
        dbm.set_data(conn, sd)
        cur = dbm.get_from_date_code(conn, tmp[0], tmp[1])
        row = cur.fetchone()
        dbm.disconnect(conn)
        self.assertEquals(row[0], tmp[0])

    def test_get_from_date1(self):
        dbm = DatabaseManager.DatabaseManager()
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testGetDailyData1.db'
        if os.path.isfile(name):
            os.remove(name)
        conn = dbm.connect(name)
        sd = StockData.StockData()
        tmp = ["2015年01月01日", "9999", "市場", "銘柄名", "業種", 100, 200, 99, 250, 12334, 1002201]
        sd.set_date(tmp[0])
        sd.set_code(tmp[1])
        sd.set_name(tmp[3])
        sd.set_market(tmp[2])
        sd.set_category(tmp[4])
        sd.set_start(tmp[5])
        sd.set_end(tmp[6])
        sd.set_min(tmp[7])
        sd.set_max(tmp[8])
        sd.set_volume(tmp[9])
        sd.set_sales(tmp[10])
        dbm.set_data(conn, sd)
        cur = dbm.get_from_date(conn, tmp[0])
        row = cur.fetchone()
        dbm.disconnect(conn)
        for i in range(len(tmp)):
            self.assertEquals(row[i], tmp[i])

    def test_get_from_code1(self):
        dbm = DatabaseManager.DatabaseManager()
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testGetCodeData1.db'
        if os.path.isfile(name):
            os.remove(name)
        conn = dbm.connect(name)
        sd = StockData.StockData()
        tmp = ["2015年01月01日", "9999", "市場", "銘柄名", "業種", 100, 200, 99, 250, 12334, 1002201]
        sd.set_date(tmp[0])
        sd.set_code(tmp[1])
        sd.set_name(tmp[3])
        sd.set_market(tmp[2])
        sd.set_category(tmp[4])
        sd.set_start(tmp[5])
        sd.set_end(tmp[6])
        sd.set_min(tmp[7])
        sd.set_max(tmp[8])
        sd.set_volume(tmp[9])
        sd.set_sales(tmp[10])
        dbm.set_data(conn, sd)
        cur = dbm.get_from_code(conn, tmp[1])
        row = cur.fetchone()
        dbm.disconnect(conn)
        for i in range(len(tmp)):
            self.assertEquals(row[i], tmp[i])

    def test_get_from_name1(self):
        dbm = DatabaseManager.DatabaseManager()
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testGetNameData1.db'
        if os.path.isfile(name):
            os.remove(name)
        conn = dbm.connect(name)
        sd = StockData.StockData()
        tmp = ["2015年01月01日", "9999", "市場", "銘柄名", "業種", 100, 200, 99, 250, 12334, 1002201]
        sd.set_date(tmp[0])
        sd.set_code(tmp[1])
        sd.set_name(tmp[3])
        sd.set_market(tmp[2])
        sd.set_category(tmp[4])
        sd.set_start(tmp[5])
        sd.set_end(tmp[6])
        sd.set_min(tmp[7])
        sd.set_max(tmp[8])
        sd.set_volume(tmp[9])
        sd.set_sales(tmp[10])
        dbm.set_data(conn, sd)
        cur = dbm.get_from_name(conn, tmp[3])
        row = cur.fetchone()
        dbm.disconnect(conn)
        for i in range(len(tmp)):
            self.assertEquals(row[i], tmp[i])

    def test_get_from_market1(self):
        dbm = DatabaseManager.DatabaseManager()
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testGetMarketData1.db'
        if os.path.isfile(name):
            os.remove(name)
        conn = dbm.connect(name)
        sd = StockData.StockData()
        tmp = ["2015年01月01日", "9999", "市場", "銘柄名", "業種", 100, 200, 99, 250, 12334, 1002201]
        sd.set_date(tmp[0])
        sd.set_code(tmp[1])
        sd.set_name(tmp[3])
        sd.set_market(tmp[2])
        sd.set_category(tmp[4])
        sd.set_start(tmp[5])
        sd.set_end(tmp[6])
        sd.set_min(tmp[7])
        sd.set_max(tmp[8])
        sd.set_volume(tmp[9])
        sd.set_sales(tmp[10])
        dbm.set_data(conn, sd)
        cur = dbm.get_from_market(conn, tmp[2])
        row = cur.fetchone()
        dbm.disconnect(conn)
        for i in range(len(tmp)):
            self.assertEquals(row[i], tmp[i])

    def test_get_from_category1(self):
        dbm = DatabaseManager.DatabaseManager()
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testGetCategoryData1.db'
        if os.path.isfile(name):
            os.remove(name)
        conn = dbm.connect(name)
        sd = StockData.StockData()
        tmp = ["2015年01月01日", "9999", "市場", "銘柄名", "業種", 100, 200, 99, 250, 12334, 1002201]
        sd.set_date(tmp[0])
        sd.set_code(tmp[1])
        sd.set_name(tmp[3])
        sd.set_market(tmp[2])
        sd.set_category(tmp[4])
        sd.set_start(tmp[5])
        sd.set_end(tmp[6])
        sd.set_min(tmp[7])
        sd.set_max(tmp[8])
        sd.set_volume(tmp[9])
        sd.set_sales(tmp[10])
        dbm.set_data(conn, sd)
        cur = dbm.get_from_category(conn, tmp[4])
        row = cur.fetchone()
        dbm.disconnect(conn)
        for i in range(len(tmp)):
            self.assertEquals(row[i], tmp[i])

    def test_get_db_name1(self):
        dbm = DatabaseManager.DatabaseManager()
        import datetime
        import calendar

        year = 2015
        for month in range(1, 13):
            for day in range(1, calendar.monthrange(year, month)[1]):
                d = datetime.date(year, month, day)
                ret = dbm.get_db_name(d)

                ans = d.strftime("%Y-%m")
                if day < 16:
                    ans += "_01"
                else:
                    ans += "_02"
                self.assertEqual(ret, ans)

    def test_get_db_dir(self):
        dbm = DatabaseManager.DatabaseManager()
        ret = dbm.get_db_dir()
        ans = "D:\\workspace\\data\\kdb\\stocks\\db\\"
        self.assertEqual(ret, ans)