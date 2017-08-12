# -*- coding: utf-8 -*-
class StockDataTag:
    global indexes
    indexes = {}

    def __init__(self):
        indexes.clear()
        pass

    @staticmethod
    def get_code_tag():
        return "コード"

    @staticmethod
    def get_name_tag():
        return "銘柄名"

    @staticmethod
    def get_market_tag():
        return "市場"

    @staticmethod
    def get_category_tag():
        return "業種"

    @staticmethod
    def get_start_tag():
        return "始値"

    @staticmethod
    def get_end_tag():
        return "終値"

    @staticmethod
    def get_min_tag():
        return "安値"

    @staticmethod
    def get_max_tag():
        return "高値"

    @staticmethod
    def get_volume_tag():
        return "出来高"

    @staticmethod
    def get_sales_tag():
        return "売買代金"

    @staticmethod
    def check_tags(tags):
        i = 0
        for tag in tags:
            if StockDataTag.get_code_tag() == tag:
                StockDataTag.set_index(StockDataTag.get_code_tag(), i)
            elif StockDataTag.get_name_tag() == tag:
                StockDataTag.set_index(StockDataTag.get_name_tag(), i)
            elif StockDataTag.get_market_tag() == tag:
                StockDataTag.set_index(StockDataTag.get_market_tag(), i)
            elif StockDataTag.get_category_tag() == tag:
                StockDataTag.set_index(StockDataTag.get_category_tag(), i)
            elif StockDataTag.get_start_tag() == tag:
                StockDataTag.set_index(StockDataTag.get_start_tag(), i)
            elif StockDataTag.get_end_tag() == tag:
                StockDataTag.set_index(StockDataTag.get_end_tag(), i)
            elif StockDataTag.get_min_tag() == tag:
                StockDataTag.set_index(StockDataTag.get_min_tag(), i)
            elif StockDataTag.get_max_tag() == tag:
                StockDataTag.set_index(StockDataTag.get_max_tag(), i)
            elif StockDataTag.get_volume_tag() == tag:
                StockDataTag.set_index(StockDataTag.get_volume_tag(), i)
            elif StockDataTag.get_sales_tag() == tag:
                StockDataTag.set_index(StockDataTag.get_sales_tag(), i)
            else:
                return False
            i += 1
        return True

    @staticmethod
    def set_index(key, index):
        indexes[key] = index

    @staticmethod
    def get_index(key, tags):
        for key_in_index in indexes.keys():
            if key == key_in_index:
                return indexes[key]
        return len(tags) + 1