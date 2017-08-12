# -*- coding:utf-8 -*-
import os
import sys
import unittest

sys.path.append(os.pardir + '\\MyFirstChainer\\src')

import FileManager

class TestFileManager(unittest.TestCase):
    def test_get_file_num1(self):
        fm = FileManager.FileManager()
        target_dir = os.path.dirname(__file__) + '\\data\\TestFileManager'
        ret = fm.get_file_num(target_dir, "\\", "png", "")
        self.assertEquals(ret, 81)

    def test_get_file_num2(self):
        fm = FileManager.FileManager()
        target_dir = os.path.dirname(__file__) + '\\data\\TestFileManager'
        ret = fm.get_file_num(target_dir, "\\", "", "")
        self.assertEquals(ret, 81)

    def test_get_file_num3(self):
        fm = FileManager.FileManager()
        target_dir = os.path.dirname(__file__) + '\\data\\TestFileManager'
        ret = fm.get_file_num(target_dir, "\\", "bmp", "")
        self.assertEquals(ret, 0)

    def test_get_file_num4(self):
        fm = FileManager.FileManager()
        target_dir = os.path.dirname(__file__) + '\\data\\TestFileManager'
        ret = fm.get_file_num(target_dir, "", "", "")
        self.assertEquals(ret, 0)

    def test_get_file_num5(self):
        fm = FileManager.FileManager()
        target_dir = os.path.dirname(__file__) + '\\data\\TestFileManager'
        ret = fm.get_file_num(target_dir, "\\", "", "1301")
        self.assertEquals(ret, 74)
