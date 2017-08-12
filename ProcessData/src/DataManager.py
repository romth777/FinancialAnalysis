# -*- coding:utf-8 -*-
import codecs

class DataManager:
    @staticmethod
    def make_data(_name, _data):
        file = codecs.open(_name, 'a+', 'shift_jis')
        for i in range(len(_data)):
            file.write(_data[i])
            if i < len(_data) - 1:
                file.write(',')
            elif i == len(_data) - 1:
                file.write('\n')
        file.flush()
        file.close()
