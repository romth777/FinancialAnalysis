# -*- coding: utf-8 -*-
import sys
import StockDataTag
import StockData
import pandas as pd
from pandas import DataFrame


class CsvManager:
    @staticmethod
    def read_line(_name, _data):
        line_num_file = sum(1 for line in open(_name))
        if line_num_file < 3:
            print("File Line Number Error")
            sys.exit(1)
        file_object = open(_name, 'r')
        line_num = 0
        date = ""
        tag = StockDataTag.StockDataTag()
        for line in file_object:
            line_split = line.strip().split(',')
            while '' in line_split:
                line_split.remove('')
            if line_num == 0:
                if len(line_split) != 1:
                    sys.exit(1)
                line_split[0] = line_split[0].replace("年", "-")
                line_split[0] = line_split[0].replace("月", "-")
                line_split[0] = line_split[0].replace("日", "")
                date = line_split[0]
            elif line_num == 1:
                if len(line_split) != 10:
                    sys.exit(1)
                if not tag.check_tags(line_split):
                    print(line_split)
                    print("Data Tag Error")
                    sys.exit(1)
            else:
                if len(line_split) != 10:
                    sys.exit(1)
                data = StockData.StockData()
                data.set_date(date)
                data.set_code(line_split[tag.get_index(tag.get_code_tag(), line_split)])
                data.set_name(line_split[tag.get_index(tag.get_name_tag(), line_split)])
                data.set_market(line_split[tag.get_index(tag.get_market_tag(), line_split)])
                data.set_category(line_split[tag.get_index(tag.get_category_tag(), line_split)])
                if line_split[tag.get_index(tag.get_start_tag(), line_split)] is not "-":
                    data.set_start(float(line_split[tag.get_index(tag.get_start_tag(), line_split)]))
                else:
                    data.set_start(-1)
                if line_split[tag.get_index(tag.get_end_tag(), line_split)] is not "-":
                    data.set_end(float(line_split[tag.get_index(tag.get_end_tag(), line_split)]))
                else:
                    data.set_end(-1)
                if line_split[tag.get_index(tag.get_min_tag(), line_split)] is not "-":
                    data.set_min(float(line_split[tag.get_index(tag.get_min_tag(), line_split)]))
                else:
                    data.set_min(-1)
                if line_split[tag.get_index(tag.get_max_tag(), line_split)] is not "-":
                    data.set_max(float(line_split[tag.get_index(tag.get_max_tag(), line_split)]))
                else:
                    data.set_max(-1)
                data.set_volume(int(line_split[tag.get_index(tag.get_volume_tag(), line_split)]))
                data.set_sales(int(line_split[tag.get_index(tag.get_sales_tag(), line_split)]))
                _data.append(data)
            line_num += 1
        file_object.close()

    @staticmethod
    def read_csv(_name):
        indexes = ["code", "market", "name", "category", "start", "max", "min", "end", "volume", "sales"]
        df = pd.read_csv(_name, skiprows=[0, 1], encoding='shift-jis', names=indexes)
        file_object = open(_name, 'r')
        for line in file_object:
            line_split = line.strip().split(',')
            if len(line_split) != 1:
                sys.exit(1)
            line_split[0] = line_split[0].replace("年", "-")
            line_split[0] = line_split[0].replace("月", "-")
            line_split[0] = line_split[0].replace("日", "")
            date = line_split[0]
            break
        date = pd.to_datetime(date)
        df.index = [date for i in range(df.shape[0])]
        file_object.close()
        return df