# -*- coding: utf-8 -*-
import sys
import unittest

sys.path.append('../src')
import StockData
import datetime


class TestStockData(unittest.TestCase):
    def test_date(self):
        today = str(datetime.date.year) + '-' \
                + str(datetime.date.month) + '-' \
                + str(datetime.date.day)
        sd = StockData.StockData()
        sd.set_date(today)
        self.assertEquals(sd.get_date(), today)

    def test_code(self):
        code = "9999"
        sd = StockData.StockData()
        sd.set_code(code)
        self.assertEquals(sd.get_code(), code)

    def test_name(self):
        name = 'NAME'
        sd = StockData.StockData()
        sd.set_name(name)
        self.assertEquals(sd.get_name(), name)

    def test_market(self):
        market = 'MARKET'
        sd = StockData.StockData()
        sd.set_market(market)
        self.assertEquals(sd.get_market(), market)

    def test_category(self):
        category = 'CATEGORY'
        sd = StockData.StockData()
        sd.set_category(category)
        self.assertEquals(sd.get_category(), category)

    def test_start(self):
        start = 1
        sd = StockData.StockData()
        sd.set_start(start)
        self.assertEquals(sd.get_start(), start)

    def test_end(self):
        end = 2
        sd = StockData.StockData()
        sd.set_end(end)
        self.assertEquals(sd.get_end(), end)

    def test_min(self):
        minimum = 3
        sd = StockData.StockData()
        sd.set_min(minimum)
        self.assertEquals(sd.get_min(), minimum)

    def test_max(self):
        maximum = 4
        sd = StockData.StockData()
        sd.set_max(maximum)
        self.assertEquals(sd.get_max(), maximum)

    def test_volume(self):
        volume = 5
        sd = StockData.StockData()
        sd.set_volume(volume)
        self.assertEquals(sd.get_volume(), volume)

    def test_sales(self):
        sales = 6
        sd = StockData.StockData()
        sd.set_sales(sales)
        self.assertEquals(sd.get_sales(), sales)
