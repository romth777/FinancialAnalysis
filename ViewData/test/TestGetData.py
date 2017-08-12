# -*- coding:utf-8 -*-
import os
import sys
import unittest
import datetime
sys.path.append(os.pardir + '\\ProcessData\\src')

import SetData
import GetData
import GetBusinessDay


class TestGetData(unittest.TestCase):
    ans1 = (("2014-01-14", "1301-T", "東証1部", "極洋", "水産・農林業", 269, 271, 269, 269, 418000, 112745000),
            ("2014-01-14", "1305-T", "東証", "ダイワ上場投信-トピックス", "その他", 1309, 1311, 1297, 1303, 1841470, 2400591210),
            ("2014-01-14", "1306-T", "東証", "TOPIX連動型上場投資信託", "その他", 1296, 1298, 1283, 1289, 9123080, 11780400560),
            ("2014-01-14", "1308-T", "東証", "上場インデックスファンドTOPIX", "その他", 1281, 1283, 1270, 1276, 1079700, 1379167100),
            ("2014-01-14", "1309-T", "東証", "上海株式指数・上証50連動型上場投資信託", "その他", 18050, 18250, 18010, 18230, 2772, 50210810),
            ("2014-01-14", "1310-T", "東証", "ダイワ上場投信-トピックス・コア30", "その他", 659, 659, 654, 654, 13060, 8589320),
            ("2014-01-14", "1311-T", "東証", "TOPIX Core 30 連動型上場投資信託", "その他", 680, 680, 670, 676, 28390, 19176990),
            ("2014-01-14", "1312-T", "東証", "ラッセル野村小型コア・インデックス連動型上場投資信託", "その他", 14120, 14180, 14010, 14010, 73, 1030310),
            ("2014-01-14", "1313-T", "東証", "サムスンKODEX200証券上場指数投資信託", "その他", 2491, 2491, 2425, 2425, 920, 2257770))

    ans2 = (("2014-01-15", "1301-T", "東証1部", "極洋", "水産・農林業", 267, 269, 266, 266, 555000, 148041000),
            ("2014-01-15", "1305-T", "東証", "ダイワ上場投信-トピックス", "その他", 1269, 1275, 1265, 1267, 1631360, 2070606400),
            ("2014-01-15", "1306-T", "東証", "TOPIX連動型上場投資信託", "その他", 1256, 1262, 1251, 1256, 7940790, 9975333350),
            ("2014-01-15", "1308-T", "東証", "上場インデックスファンドTOPIX", "その他", 1242, 1248, 1238, 1240, 1708800, 2123144700),
            ("2014-01-15", "1309-T", "東証", "上海株式指数・上証50連動型上場投資信託", "その他", 18100, 18230, 17900, 17960, 4485, 80949670),
            ("2014-01-15", "1310-T", "東証", "ダイワ上場投信-トピックス・コア30", "その他", 640, 642, 637, 640, 11440, 7320750),
            ("2014-01-15", "1311-T", "東証", "TOPIX Core 30 連動型上場投資信託", "その他", 664, 664, 654, 658, 46860, 30891150),
            ("2014-01-15", "1312-T", "東証", "ラッセル野村小型コア・インデックス連動型上場投資信託", "その他", 13550, 13800, 13550, 13790, 33, 450350),
            ("2014-01-15", "1313-T", "東証", "サムスンKODEX200証券上場指数投資信託", "その他", 2360, 2373, 2356, 2373, 550, 1301210),
            ("2014-01-15", "1314-T", "東証", "上場インデックスファンドS&P日本新興株100", "その他", 1191, 1199, 1145, 1158, 17400, 20363100))

    ans3 = (("2014-01-16", "1301-T", "東証1部", "極洋", "水産・農林業", 268, 269, 266, 266, 361000, 96413000),
            ("2014-01-16", "1305-T", "東証", "ダイワ上場投信-トピックス", "その他", 1272, 1274, 1262, 1262, 334790, 424995700),
            ("2014-01-16", "1306-T", "東証", "TOPIX連動型上場投資信託", "その他", 1258, 1262, 1250, 1251, 3987230, 5006655810),
            ("2014-01-16", "1308-T", "東証", "上場インデックスファンドTOPIX", "その他", 1244, 1248, 1236, 1237, 710600, 881999500),
            ("2014-01-16", "1309-T", "東証", "上海株式指数・上証50連動型上場投資信託", "その他", 17960, 18100, 17960, 18020, 1021, 18421460),
            ("2014-01-16", "1310-T", "東証", "ダイワ上場投信-トピックス・コア30", "その他", 641, 641, 635, 636, 2870, 1833040),
            ("2014-01-16", "1311-T", "東証", "TOPIX Core 30 連動型上場投資信託", "その他", 657, 660, 655, 655, 6770, 4449240),
            ("2014-01-16", "1312-T", "東証", "ラッセル野村小型コア・インデックス連動型上場投資信託", "その他", 13800, 13800, 13680, 13680, 111, 1519200),
            ("2014-01-16", "1313-T", "東証", "サムスンKODEX200証券上場指数投資信託", "その他", 2373, 2398, 2373, 2398, 50, 119650),
            ("2014-01-16", "1314-T", "東証", "上場インデックスファンドS&P日本新興株100", "その他", 1158, 1199, 1150, 1199, 17500, 20559100),
            ("2014-01-16", "1316-T", "東証", "上場インデックスファンドTOPIX100日本大型株", "その他", 810, 818, 810, 816, 1010, 822710),
            ("2014-01-16", "1317-T", "東証", "上場インデックスファンドTOPIX Mid400日本中型株", "その他", 1314, 1325, 1308, 1325, 890, 1172710),
            ("2014-01-16", "1318-T", "東証", "上場インデックスファンドTOPIX Small日本小型株", "その他", 1412, 1439, 1401, 1439, 1970, 2800750),
            ("2014-01-16", "1319-T", "東証", "日経300株価指数連動型上場投資信託", "その他", "-", "-", "-", "-", 0, 0),
            ("2014-01-16", "1319-F", "福証", "日経300株価指数連動型上場投資信託", "その他", "-", "-", "-", "-", 0, 0),
            ("2014-01-16", "1319-S", "札証", "日経300株価指数連動型上場投資信託", "その他", "-", "-", "-", "-", 0, 0),
            ("2014-01-16", "1320-T", "東証", "ダイワ上場投信-日経225", "その他", 15350, 15400, 15280, 15310, 198449, 3044472870))

    ans_to_row = [0, 1, 2, 3, 4, 5, 8, 7, 6, 9, 10]

    def test_get_from_date_code1(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '\\data\\stocks_*csv'
        db_dir = os.path.dirname(os.path.abspath(__file__)) + '\\data\\'
        db_file = 'testGetFromDateCode1.db'
        db_dir_file1 = db_dir + '2014-01_01_' + db_file
        db_dir_file2 = db_dir + '2014-01_02_' + db_file
        if os.path.isfile(db_dir_file1):
            os.remove(db_dir_file1)
        if os.path.isfile(db_dir_file2):
            os.remove(db_dir_file2)
        sd = SetData.SetData()
        sd.set_data(path, db_dir, db_file)
        gd = GetData.GetData()
        conn = gd.connect(db_dir, '2014-01_01_' + db_file)
        cur = gd.get_from_date_code(conn, "2014-01-14", "1301-T")
        row = cur.fetchall()
        gd.disconnect(conn)
        self.assertEquals(1, len(row))
        for j in range(len(row)):
            for k in range(10):
                self.assertEquals(row[j][k], self.ans1[0][self.ans_to_row[k]])
        conn = gd.connect(db_dir, '2014-01_01_' + db_file)
        cur = gd.get_from_date_code(conn, "2014-01-15", "1301-T")
        row = cur.fetchall()
        gd.disconnect(conn)
        self.assertEquals(1, len(row))
        for j in range(len(row)):
            for k in range(10):
                self.assertEquals(row[j][k], self.ans2[0][self.ans_to_row[k]])
        conn = gd.connect(db_dir, '2014-01_02_' + db_file)
        cur = gd.get_from_date_code(conn, "2014-01-16", "1301-T")
        row = cur.fetchall()
        gd.disconnect(conn)
        self.assertEquals(1, len(row))
        for j in range(len(row)):
            for k in range(10):
                self.assertEquals(row[j][k], self.ans3[0][self.ans_to_row[k]])

    def test_get_from_date1(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '\\data\\stocks_*csv'
        db_dir = os.path.dirname(os.path.abspath(__file__)) + '\\data\\'
        db_file = 'testGetFromDate1.db'
        db_dir_file1 = db_dir + '2014-01_01_' + db_file
        db_dir_file2 = db_dir + '2014-01_02_' + db_file
        if os.path.isfile(db_dir_file1):
            os.remove(db_dir_file1)
        if os.path.isfile(db_dir_file2):
            os.remove(db_dir_file2)
        sd = SetData.SetData()
        sd.set_data(path, db_dir, db_file)
        gd = GetData.GetData()
        conn = gd.connect(db_dir, '2014-01_01_' + db_file)
        cur = gd.get_from_date(conn, "2014-01-14")
        row = cur.fetchall()
        gd.disconnect(conn)
        for i in range(len(self.ans1)):
            for j in range(len(row)):
                if self.ans1[i][1] == row[j][1]:
                    for k in range(10):
                        self.assertEquals(row[j][k], self.ans1[i][self.ans_to_row[k]])
        conn = gd.connect(db_dir, '2014-01_01_' + db_file)
        cur = gd.get_from_date(conn, "2014-01-15")
        row = cur.fetchall()
        gd.disconnect(conn)
        self.assertEquals(10, len(row))
        for i in range(len(self.ans2)):
            for j in range(len(row)):
                if self.ans2[i][1] == row[j][1]:
                    for k in range(10):
                        self.assertEquals(row[j][k], self.ans2[i][self.ans_to_row[k]])
        conn = gd.connect(db_dir, '2014-01_02_' + db_file)
        cur = gd.get_from_date(conn, "2014-01-16")
        row = cur.fetchall()
        gd.disconnect(conn)
        self.assertEquals(19, len(row))
        for i in range(len(self.ans3)):
            for j in range(len(row)):
                if self.ans3[i][1] == row[j][1]:
                    for k in range(10):
                        if self.ans3[i][self.ans_to_row[k]] == "-":
                            self.assertEquals(row[j][k], -1)
                        else:
                            self.assertEquals(row[j][k], self.ans3[i][self.ans_to_row[k]])

    def test_get_from_code1(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '\\data\\stocks_*csv'
        db_dir = os.path.dirname(os.path.abspath(__file__)) + '\\data\\'
        db_file = 'testGetFromCode1.db'
        db_dir_file1 = db_dir + '2014-01_01_' + db_file
        db_dir_file2 = db_dir + '2014-01_02_' + db_file
        if os.path.isfile(db_dir_file1):
            os.remove(db_dir_file1)
        if os.path.isfile(db_dir_file2):
            os.remove(db_dir_file2)
        sd = SetData.SetData()
        sd.set_data(path, db_dir, db_file)
        gd = GetData.GetData()
        conn = gd.connect(db_dir, '2014-01_01_' + db_file)
        test_data = "1301-T"
        cur = gd.get_from_code(conn, test_data)
        row = cur.fetchall()
        gd.disconnect(conn)
        self.assertEquals(2, len(row))
        for i in range(len(self.ans1)):
            for j in range(len(row)):
                if self.ans1[i][0] == row[j][0] and self.ans1[i][1] == row[j][1]:
                    for k in range(10):
                        self.assertEquals(row[j][k], self.ans1[i][self.ans_to_row[k]])
        for i in range(len(self.ans2)):
            for j in range(len(row)):
                if self.ans2[i][0] == row[j][0] and self.ans2[i][1] == row[j][1]:
                    for k in range(10):
                        self.assertEquals(row[j][k], self.ans2[i][self.ans_to_row[k]])
        conn = gd.connect(db_dir, '2014-01_02_' + db_file)
        test_data = "1301-T"
        cur = gd.get_from_code(conn, test_data)
        row = cur.fetchall()
        gd.disconnect(conn)
        self.assertEquals(1, len(row))
        for i in range(len(self.ans3)):
            for j in range(len(row)):
                if self.ans3[i][0] == row[j][0] and self.ans3[i][1] == row[j][1]:
                    for k in range(10):
                        if self.ans3[i][self.ans_to_row[k]] == "-":
                            self.assertEquals(row[j][k], -1)
                        else:
                            self.assertEquals(row[j][k], self.ans3[i][self.ans_to_row[k]])

    def test_get_from_name1(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '\\data\\stocks_*csv'
        db_dir = os.path.dirname(os.path.abspath(__file__)) + '\\data\\'
        db_file = 'testGetFromName1.db'
        db_dir_file1 = db_dir + '2014-01_01_' + db_file
        db_dir_file2 = db_dir + '2014-01_02_' + db_file
        if os.path.isfile(db_dir_file1):
            os.remove(db_dir_file1)
        if os.path.isfile(db_dir_file2):
            os.remove(db_dir_file2)
        sd = SetData.SetData()
        sd.set_data(path, db_dir, db_file)
        gd = GetData.GetData()
        conn = gd.connect(db_dir, '2014-01_01_' + db_file)
        test_data = "ラッセル野村小型コア・インデックス連動型上場投資信託"
        cur = gd.get_from_name(conn, test_data)
        row = cur.fetchall()
        gd.disconnect(conn)
        self.assertEquals(2, len(row))
        for i in range(len(self.ans1)):
            for j in range(len(row)):
                if self.ans1[i][0] == row[j][0] and self.ans1[i][1] == row[j][1]:
                    for k in range(10):
                        self.assertEquals(row[j][k], self.ans1[i][self.ans_to_row[k]])
        for i in range(len(self.ans2)):
            for j in range(len(row)):
                if self.ans2[i][0] == row[j][0] and self.ans2[i][1] == row[j][1]:
                    for k in range(10):
                        self.assertEquals(row[j][k], self.ans2[i][self.ans_to_row[k]])
        conn = gd.connect(db_dir, '2014-01_02_' + db_file)
        test_data = "ラッセル野村小型コア・インデックス連動型上場投資信託"
        cur = gd.get_from_name(conn, test_data)
        row = cur.fetchall()
        gd.disconnect(conn)
        for i in range(len(self.ans3)):
            for j in range(len(row)):
                if self.ans3[i][0] == row[j][0] and self.ans3[i][1] == row[j][1]:
                    for k in range(10):
                        if self.ans3[i][self.ans_to_row[k]] == "-":
                            self.assertEquals(row[j][k], -1)
                        else:
                            self.assertEquals(row[j][k], self.ans3[i][self.ans_to_row[k]])

    def test_get_from_market1(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '\\data\\stocks_*csv'
        db_dir = os.path.dirname(os.path.abspath(__file__)) + '\\data\\'
        db_file = 'testGetFromMarket1.db'
        db_dir_file1 = db_dir + '2014-01_01_' + db_file
        db_dir_file2 = db_dir + '2014-01_02_' + db_file
        if os.path.isfile(db_dir_file1):
            os.remove(db_dir_file1)
        if os.path.isfile(db_dir_file2):
            os.remove(db_dir_file2)
        sd = SetData.SetData()
        sd.set_data(path, db_dir, db_file)
        gd = GetData.GetData()
        conn = gd.connect(db_dir, '2014-01_01_' + db_file)
        test_data = "東証"
        cur = gd.get_from_market(conn, test_data)
        row = cur.fetchall()
        gd.disconnect(conn)
        for i in range(len(self.ans1)):
            for j in range(len(row)):
                if self.ans1[i][0] == row[j][0] and self.ans1[i][1] == row[j][1]:
                    for k in range(10):
                        self.assertEquals(row[j][k], self.ans1[i][self.ans_to_row[k]])
        for i in range(len(self.ans2)):
            for j in range(len(row)):
                if self.ans2[i][0] == row[j][0] and self.ans2[i][1] == row[j][1]:
                    for k in range(10):
                        self.assertEquals(row[j][k], self.ans2[i][self.ans_to_row[k]])
        conn = gd.connect(db_dir, '2014-01_02_' + db_file)
        test_data = "東証"
        cur = gd.get_from_market(conn, test_data)
        row = cur.fetchall()
        gd.disconnect(conn)
        for i in range(len(self.ans3)):
            for j in range(len(row)):
                if self.ans3[i][0] == row[j][0] and self.ans3[i][1] == row[j][1]:
                    for k in range(10):
                        if self.ans3[i][self.ans_to_row[k]] == "-":
                            self.assertEquals(row[j][k], -1)
                        else:
                            self.assertEquals(row[j][k], self.ans3[i][self.ans_to_row[k]])

    def test_get_from_category1(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '\\data\\stocks_*.csv'
        db_dir = os.path.dirname(os.path.abspath(__file__)) + '\\data\\'
        db_file = 'testGetFromCategory1.db'
        db_dir_file1 = db_dir + '2014-01_01_' + db_file
        db_dir_file2 = db_dir + '2014-01_02_' + db_file
        if os.path.isfile(db_dir_file1):
            os.remove(db_dir_file1)
        if os.path.isfile(db_dir_file2):
            os.remove(db_dir_file2)
        sd = SetData.SetData()
        sd.set_data(path, db_dir, db_file)
        gd = GetData.GetData()
        conn = gd.connect(db_dir, '2014-01_01_' + db_file)
        test_data = "水産・農林業"
        cur = gd.get_from_category(conn, test_data)
        row = cur.fetchall()
        gd.disconnect(conn)
        for i in range(len(self.ans1)):
            for j in range(len(row)):
                if self.ans1[i][0] == row[j][0] and self.ans1[i][1] == row[j][1]:
                    for k in range(10):
                        self.assertEquals(row[j][k], self.ans1[i][self.ans_to_row[k]])
        for i in range(len(self.ans2)):
            for j in range(len(row)):
                if self.ans2[i][0] == row[j][0] and self.ans2[i][1] == row[j][1]:
                    for k in range(10):
                        self.assertEquals(row[j][k], self.ans2[i][self.ans_to_row[k]])
        conn = gd.connect(db_dir, '2014-01_02_' + db_file)
        test_data = "水産・農林業"
        cur = gd.get_from_category(conn, test_data)
        row = cur.fetchall()
        gd.disconnect(conn)
        for i in range(len(self.ans3)):
            for j in range(len(row)):
                if self.ans3[i][0] == row[j][0] and self.ans3[i][1] == row[j][1]:
                    for k in range(10):
                        if self.ans3[i][self.ans_to_row[k]] == "-":
                            self.assertEquals(row[j][k], -1)
                        else:
                            self.assertEquals(row[j][k], self.ans3[i][self.ans_to_row[k]])

    def test_get_from_category2(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '\\data\\stocks_*csv'
        db_dir = os.path.dirname(os.path.abspath(__file__)) + '\\data\\'
        db_file = 'testGetFromCategory2.db'
        db_dir_file1 = db_dir + '2014-01_01_' + db_file
        db_dir_file2 = db_dir + '2014-01_02_' + db_file
        if os.path.isfile(db_dir_file1):
            os.remove(db_dir_file1)
        if os.path.isfile(db_dir_file2):
            os.remove(db_dir_file2)
        sd = SetData.SetData()
        sd.set_data(path, db_dir, db_file)
        gd = GetData.GetData()
        conn = gd.connect(db_dir, '2014-01_01_' + db_file)
        test_data = "その他"
        cur = gd.get_from_category(conn, test_data)
        row = cur.fetchall()
        gd.disconnect(conn)
        for i in range(len(self.ans1)):
            for j in range(len(row)):
                if self.ans1[i][0] == row[j][0] and self.ans1[i][1] == row[j][1]:
                    for k in range(10):
                        self.assertEquals(row[j][k], self.ans1[i][self.ans_to_row[k]])
        for i in range(len(self.ans2)):
            for j in range(len(row)):
                if self.ans2[i][0] == row[j][0] and self.ans2[i][1] == row[j][1]:
                    for k in range(10):
                        self.assertEquals(row[j][k], self.ans2[i][self.ans_to_row[k]])
        conn = gd.connect(db_dir, '2014-01_02_' + db_file)
        test_data = "その他"
        cur = gd.get_from_category(conn, test_data)
        row = cur.fetchall()
        gd.disconnect(conn)
        for i in range(len(self.ans3)):
            for j in range(len(row)):
                if self.ans3[i][0] == row[j][0] and self.ans3[i][1] == row[j][1]:
                    for k in range(10):
                        if self.ans3[i][self.ans_to_row[k]] == "-":
                            self.assertEquals(row[j][k], -1)
                        else:
                            self.assertEquals(row[j][k], self.ans3[i][self.ans_to_row[k]])

    def test_get_db_file_name1(self):
        gd = GetData.GetData()
        gbd = GetBusinessDay.GetBusinessDay()
        today = datetime.datetime.today()

        day_list = gbd.get_business_day(today, 300)

        for i_day in day_list:
            half = ""
            if int(i_day.day) < 16:
                half = "01"
            else:
                half = "02"
            fname, date = gd.get_db_file_name(i_day)
            self.assertEqual(fname, i_day.strftime("%Y-%m") + "_" + half)
            self.assertEqual(date, i_day)

    def test_get_db_dir1(self):
        gd = GetData.GetData()
        ans = "D:\\workspace\\data\\kdb\\stocks\\db\\"
        self.assertEqual(ans, gd.get_db_dir())
