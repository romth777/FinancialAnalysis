# -*- coding: utf-8 -*-
import sys
import unittest

sys.path.append('../src')
import StockDataTag


class TestStockDataTag(unittest.TestCase):
    def test_get_code_tag1(self):
        sdt = StockDataTag.StockDataTag()
        self.assertEquals(sdt.get_code_tag(), 'コード')

    def test_get_name_tag1(self):
        sdt = StockDataTag.StockDataTag()
        self.assertEquals(sdt.get_name_tag(), '銘柄名')

    def test_get_market_tag1(self):
        sdt = StockDataTag.StockDataTag()
        self.assertEquals(sdt.get_market_tag(), '市場')

    def test_get_category_tag1(self):
        sdt = StockDataTag.StockDataTag()
        self.assertEquals(sdt.get_category_tag(), '業種')

    def test_get_start_tag1(self):
        sdt = StockDataTag.StockDataTag()
        self.assertEquals(sdt.get_start_tag(), '始値')

    def test_get_end_tag1(self):
        sdt = StockDataTag.StockDataTag()
        self.assertEquals(sdt.get_end_tag(), '終値')

    def test_get_min_tag1(self):
        sdt = StockDataTag.StockDataTag()
        self.assertEquals(sdt.get_min_tag(), '安値')

    def test_get_max_tag1(self):
        sdt = StockDataTag.StockDataTag()
        self.assertEquals(sdt.get_max_tag(), '高値')

    def test_get_volume_tag1(self):
        sdt = StockDataTag.StockDataTag()
        self.assertEquals(sdt.get_volume_tag(), '出来高')

    def test_get_sales_tag1(self):
        sdt = StockDataTag.StockDataTag()
        self.assertEquals(sdt.get_sales_tag(), '売買代金')

    def test_check_tags1(self):
        sdt = StockDataTag.StockDataTag()
        data_in = ("コード", "銘柄名", "市場", "業種", "始値", "高値", "安値", "終値", "出来高")
        self.assertEquals(sdt.check_tags(data_in), True)

    def test_check_tags2(self):
        sdt = StockDataTag.StockDataTag()
        data_in = "コード"
        self.assertEquals(sdt.check_tags(data_in), False)

    def test_check_tags3(self):
        sdt = StockDataTag.StockDataTag()
        data_in = ("コード", "銘柄名")
        self.assertEquals(sdt.check_tags(data_in), True)

    def test_check_tags4(self):
        sdt = StockDataTag.StockDataTag()
        data_in = ("test1", "test2")
        self.assertEquals(sdt.check_tags(data_in), False)

    def test_get_index1(self):
        sdt = StockDataTag.StockDataTag()
        keys = ("コード", "銘柄名", "市場", "業種", "始値", "高値", "安値", "終値", "出来高")
        data_in = ("コード", "銘柄名", "市場", "業種", "始値", "高値", "安値", "終値", "出来高")
        self.assertEquals(sdt.check_tags(data_in), True)
        i = 0
        for key in keys:
            self.assertEquals(sdt.get_index(key, data_in), i)
            i += 1

    def test_get_index2(self):
        sdt = StockDataTag.StockDataTag()
        keys = ("コード", "test", "市場", "業種", "始値", "高値", "安値", "終値", "出来高")
        data_in = ("コード", "銘柄名", "市場", "業種", "始値", "高値", "安値", "終値", "出来高")
        self.assertEquals(sdt.check_tags(data_in), True)
        i = 0
        for key in keys:
            if key == "test":
                self.assertEquals(sdt.get_index(key, data_in), len(data_in) + 1)
            else:
                self.assertEquals(sdt.get_index(key, data_in), i)
            i += 1