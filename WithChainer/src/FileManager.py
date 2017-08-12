# -*- coding:utf-8 -*-
import os
import os.path


class FileManager:
    def __init__(self):
        pass

    def get_file_num(self, _target_dir="", _sep="\\", _ext="", _str=""):
        ch = os.listdir(_target_dir)
        counter = 0
        for c in ch:
            if os.path.isdir(_target_dir + _sep + c):
                counter += self.get_file_num(_target_dir + _sep + c, _sep, _ext, _str)
            else:
                file, ext = os.path.splitext(c)
                file = file.lower()
                ext = ext.lower().replace(".", "")
                if file != "" and (_str == "" or (_str != "" and file.find(_str) != -1)):
                    if ext != "" and (_ext == "" or ext == _ext):
                        counter += 1
        return counter