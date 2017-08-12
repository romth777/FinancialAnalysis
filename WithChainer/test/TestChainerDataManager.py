# -*- coding:utf-8 -*-
import os
import sys
import unittest

sys.path.append(os.pardir + '\\MyFirstChainer\\src')

import ChainerDataManager

class TestChainerDataManager(unittest.TestCase):
    def test_load_a_stock1(self):
        cdm = ChainerDataManager.ChainerDataManager()
        cdm.load_a_stock("2016-03-10", 20)
        pass

    def test_load_stocks1(self):
        cdm = ChainerDataManager.ChainerDataManager()
        cdm.load_stocks("2016-03-10", 25, 20)
        pass

    def test_download_stock_data1(self):
        cdm = ChainerDataManager.ChainerDataManager()
        cdm.download_stock_data("2016-03-14", 20, 500, 100)
        pass