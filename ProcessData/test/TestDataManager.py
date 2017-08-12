# -*- coding:utf-8 -*-
import os
import sys
import unittest
sys.path.append('../src')
sys.path.append('./data')
import DataManager


class TestDataManager(unittest.TestCase):
    def test_make_data1(self):
        dm = DataManager.DataManager()
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testMakeData1.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm.make_data(name, ("A", "B", "C", "D"))
        file = open(name, 'r')
        for line in file:
            line_split = line.strip().split(',')
        self.assertEquals(line_split[0], "A")
        self.assertEquals(line_split[1], "B")
        self.assertEquals(line_split[2], "C")
        self.assertEquals(line_split[3], "D")
        self.assertEquals(len(line_split), 4)

    def test_make_data2(self):
        dm = DataManager.DataManager()
        name = os.path.dirname(os.path.abspath(__file__)) + '\\data\\testMakeData2.csv'
        if os.path.isfile(name):
            os.remove(name)
        dm.make_data(name, ("A", "B", "C", "D"))
        dm.make_data(name, ("E", "F", "G", "H"))
        file = open(name, 'r')
        line_num = 0
        for line in file:
            line_split = line.strip().split(',')
            if line_num == 0:
                self.assertEquals(line_split[0], "A")
                self.assertEquals(line_split[1], "B")
                self.assertEquals(line_split[2], "C")
                self.assertEquals(line_split[3], "D")
                self.assertEquals(len(line_split), 4)
            elif line_num == 1:
                self.assertEquals(line_split[0], "E")
                self.assertEquals(line_split[1], "F")
                self.assertEquals(line_split[2], "G")
                self.assertEquals(line_split[3], "H")
                self.assertEquals(len(line_split), 4)
            line_num += 1
