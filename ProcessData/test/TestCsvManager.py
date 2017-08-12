# -*- coding:utf-8 -*-
import os
import sys
import unittest
sys.path.append('../src')

import CsvManager
import DataManager
import StockData
from pandas import Series
import pandas as pd


class TestCsvManager(unittest.TestCase):
    def test_read_line1(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine1.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line2(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine2.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "市場", "銘柄名", "業種", "始値", "高値", "安値", "終値", "出来高", "売買代金")
        dm.make_data(name, data_in2)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line3(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine3.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "市場", "銘柄名", "業種", "始値", "高値", "安値", "終値", "出来高", "売買代金")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "268", "270", "418000", "112745000")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = list()
        cm.read_line(name, data_out)

        sd = StockData.StockData()
        sd.set_date(data_in1[0])
        sd.set_code(data_in3[0])
        sd.set_name(data_in3[2])
        sd.set_market(data_in3[1])
        sd.set_category(data_in3[3])
        sd.set_start(data_in3[4])
        sd.set_end(data_in3[7])
        sd.set_min(data_in3[6])
        sd.set_max(data_in3[5])
        sd.set_volume(data_in3[8])
        sd.set_sales(data_in3[9])
        self.assertEqual(data_out[0].get_date(), sd.get_date())
        self.assertEqual(data_out[0].get_code(), sd.get_code())
        self.assertEqual(data_out[0].get_name(), sd.get_name())
        self.assertEqual(data_out[0].get_market(), sd.get_market())
        self.assertEqual(data_out[0].get_category(), sd.get_category())
        self.assertEqual(data_out[0].get_start(), sd.get_start())
        self.assertEqual(data_out[0].get_end(), sd.get_end())
        self.assertEqual(data_out[0].get_min(), sd.get_min())
        self.assertEqual(data_out[0].get_max(), sd.get_max())
        self.assertEqual(data_out[0].get_volume(), sd.get_volume())
        self.assertEqual(data_out[0].get_sales(), sd.get_sales())

    def test_read_line4(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine4.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "市場", "銘柄名", "業種", "始値", "高値", "安値", "終値", "出来高", "売買代金")
        dm.make_data(name, data_in2)
        data_in3 = ("", "")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line5(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine5.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = "2014-6-24"
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "市場", "銘柄名", "業種", "始値", "高値", "安値", "終値", "出来高", "売買代金")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "269", "269", "418000", "112745000")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line6(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine6.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24", "test"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "市場", "銘柄名", "業種", "始値", "高値", "安値", "終値", "出来高", "売買代金")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "269", "269", "418000", "112745000")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line7(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine7.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "市場", "銘柄名", "業種", "始値", "高値", "安値", "終値", "出来高", "売買代金", "test")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "269", "269", "418000", "112745000")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line8(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine8.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "市場", "銘柄名", "業種", "始値", "高値", "安値", "終値", "出来高")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "269", "269", "418000", "112745000")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line9(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine9.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "", "市場", "業種", "始値", "高値", "安値", "終値", "出来高", "売買代金")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "269", "269", "418000", "112745000")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line10(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine10.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("test", "市場", "銘柄名", "業種", "始値", "高値", "安値", "終値", "出来高", "売買代金")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "269", "269", "418000", "112745000")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line11(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine11.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "test", "市場", "業種", "始値", "高値", "安値", "終値", "出来高", "売買代金")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "269", "269", "418000", "112745000")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line12(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine12.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "銘柄名", "test", "業種", "始値", "高値", "安値", "終値", "出来高", "売買代金")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "269", "269", "418000", "112745000")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line13(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine13.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "市場", "銘柄名", "test", "始値", "高値", "安値", "終値", "出来高", "売買代金")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "269", "269", "418000", "112745000")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line14(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine14.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "市場", "銘柄名", "業種", "test", "高値", "安値", "終値", "出来高", "売買代金")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "269", "269", "418000", "112745000")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line15(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine15.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "市場", "銘柄名", "業種", "始値", "test", "安値", "終値", "出来高", "売買代金")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "269", "269", "418000", "112745000")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line16(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine16.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "市場", "銘柄名", "業種", "始値", "高値", "test", "終値", "出来高", "売買代金")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "269", "269", "418000", "112745000")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line17(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine17.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "市場", "銘柄名", "業種", "始値", "高値", "安値", "test", "出来高", "売買代金")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "269", "269", "418000", "112745000")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line18(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine18.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "市場", "銘柄名", "業種", "始値", "高値", "安値", "終値", "test", "売買代金")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "269", "269", "418000", "112745000")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_line19(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadLine19.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "市場", "銘柄名", "業種", "始値", "高値", "安値", "終値", "出来高", "test")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "269", "269", "418000", "112745000")
        dm.make_data(name, data_in3)
        cm = CsvManager.CsvManager()
        data_out = StockData.StockData()
        with self.assertRaises(SystemExit) as ar:
            cm.read_line(name, data_out)
        self.assertEqual(ar.exception.code, 1)

    def test_read_csv1(self):
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testReadCsv1.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm = DataManager.DataManager()
        data_in1 = ["2014-6-24"]
        dm.make_data(name, data_in1)
        data_in2 = ("コード", "市場", "銘柄名", "業種", "始値", "高値", "安値", "終値", "出来高", "売買代金")
        dm.make_data(name, data_in2)
        data_in3 = ("1301-T", "東証1部", "極洋", "水産・農林業", "269", "271", "269", "269", "418000", "112745000")
        dm.make_data(name, data_in3)
        data_in4 = ("1305-T", "東証", "ダイワ上場投信-トピックス", "その他", "1309", "1311", "1297", "1303", "1841470", "2400591210")
        dm.make_data(name, data_in4)

        cm = CsvManager.CsvManager()
        df = cm.read_csv(name)
        self.assertEqual(2, df.shape[0])
        self.assertEqual(10, df.shape[1])
        self.assertEqual(pd.to_datetime(data_in1), df.index[0])
        self.assertEqual(pd.to_datetime(data_in1), df.index[1])
        self.assertEqual(data_in3[0], df["code"][0])
        self.assertEqual(data_in3[1], df["market"][0])
        self.assertEqual(data_in3[2], df["name"][0])
        self.assertEqual(data_in3[3], df["category"][0])
        self.assertEqual(float(data_in3[4]), df["start"][0])
        self.assertEqual(float(data_in3[5]), df["max"][0])
        self.assertEqual(float(data_in3[6]), df["min"][0])
        self.assertEqual(float(data_in3[7]), df["end"][0])
        self.assertEqual(int(data_in3[8]), df["volume"][0])
        self.assertEqual(int(data_in3[9]), df["sales"][0])
        self.assertEqual(data_in4[0], df["code"][1])
        self.assertEqual(data_in4[1], df["market"][1])
        self.assertEqual(data_in4[2], df["name"][1])
        self.assertEqual(data_in4[3], df["category"][1])
        self.assertEqual(float(data_in4[4]), df["start"][1])
        self.assertEqual(float(data_in4[5]), df["max"][1])
        self.assertEqual(float(data_in4[6]), df["min"][1])
        self.assertEqual(float(data_in4[7]), df["end"][1])
        self.assertEqual(int(data_in4[8]), df["volume"][1])
        self.assertEqual(int(data_in4[9]), df["sales"][1])