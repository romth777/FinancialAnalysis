# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.append('../src')
import SetData
import DatabaseManager


class TestSetData(unittest.TestCase):
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

    def test_set_data1(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '\\data\\stocks_*.csv'
        db_dir = os.path.dirname(os.path.abspath(__file__)) + '\\data\\'
        db_file = 'testSetData1.db'
        db_dir_file1 = db_dir + '2014-01_01_' + db_file
        db_dir_file2 = db_dir + '2014-01_02_' + db_file
        if os.path.isfile(db_dir_file1):
            os.remove(db_dir_file1)
        if os.path.isfile(db_dir_file2):
            os.remove(db_dir_file2)
        set_data = SetData.SetData()
        set_data.set_data(path, db_dir, db_file)
        dbm = DatabaseManager.DatabaseManager()
        conn = dbm.connect(db_dir_file1)
        cur2 = dbm.get_from_date(conn, "2014-01-14")
        row2 = cur2.fetchall()
        self.assertEquals(9, len(row2))
        for i in range(len(self.ans1)):
            self.assertEquals(row2[i][0], self.ans1[i][0])
            self.assertEquals(row2[i][1], self.ans1[i][1])
            self.assertEquals(row2[i][2], self.ans1[i][2])
            self.assertEquals(row2[i][3], self.ans1[i][3])
            self.assertEquals(row2[i][4], self.ans1[i][4])
            self.assertEquals(row2[i][5], self.ans1[i][5])
            self.assertEquals(row2[i][6], self.ans1[i][8])
            self.assertEquals(row2[i][7], self.ans1[i][7])
            self.assertEquals(row2[i][8], self.ans1[i][6])
            self.assertEquals(row2[i][9], self.ans1[i][9])
            self.assertEquals(row2[i][10], self.ans1[i][10])
        cur3 = dbm.get_from_date(conn, "2014-01-15")
        row3 = cur3.fetchall()
        self.assertEquals(10, len(row3))
        for i in range(len(self.ans2)):
            self.assertEquals(row3[i][0], self.ans2[i][0])
            self.assertEquals(row3[i][1], self.ans2[i][1])
            self.assertEquals(row3[i][2], self.ans2[i][2])
            self.assertEquals(row3[i][3], self.ans2[i][3])
            self.assertEquals(row3[i][4], self.ans2[i][4])
            self.assertEquals(row3[i][5], self.ans2[i][5])
            self.assertEquals(row3[i][6], self.ans2[i][8])
            self.assertEquals(row3[i][7], self.ans2[i][7])
            self.assertEquals(row3[i][8], self.ans2[i][6])
            self.assertEquals(row3[i][9], self.ans2[i][9])
            self.assertEquals(row3[i][10], self.ans2[i][10])
        set_data.set_data(path, db_dir, db_file)
        dbm = DatabaseManager.DatabaseManager()
        conn = dbm.connect(db_dir_file2)
        cur4 = dbm.get_from_date(conn, "2014-01-16")
        row4 = cur4.fetchall()
        dbm.disconnect(conn)
        self.assertEquals(19, len(row4))
        for i in range(len(self.ans3)):
            self.assertEquals(row4[i][0], self.ans3[i][0])
            self.assertEquals(row4[i][1], self.ans3[i][1])
            self.assertEquals(row4[i][2], self.ans3[i][2])
            self.assertEquals(row4[i][3], self.ans3[i][3])
            self.assertEquals(row4[i][4], self.ans3[i][4])
            if self.ans3[i][3] == "日経300株価指数連動型上場投資信託":
                self.assertEquals(row4[i][5], -1)
                self.assertEquals(row4[i][6], -1)
                self.assertEquals(row4[i][7], -1)
                self.assertEquals(row4[i][8], -1)
            else:
                self.assertEquals(row4[i][5], self.ans3[i][5])
                self.assertEquals(row4[i][6], self.ans3[i][8])
                self.assertEquals(row4[i][7], self.ans3[i][7])
                self.assertEquals(row4[i][8], self.ans3[i][6])
            self.assertEquals(row4[i][9], self.ans3[i][9])
            self.assertEquals(row4[i][10], self.ans3[i][10])