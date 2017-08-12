# -*- coding: utf-8 -*-
class StockData:
    def __init__(self):
        self.date = ""
        self.code = 0
        self.name = ""
        self.market = ""
        self.category = ""
        self.start = 0
        self.end = 0
        self.min = 0
        self.max = 0
        self.volume = 0
        self.sales = 0
        pass

    def set_date(self, date):
        self.date = str(date)

    def set_code(self, code):
        self.code = str(code)

    def set_name(self, name):
        self.name = str(name)

    def set_market(self, market):
        self.market = str(market)

    def set_category(self, category):
        self.category = str(category)

    def set_start(self, start):
        self.start = int(start)

    def set_end(self, end):
        self.end = int(end)

    def set_min(self, min):
        self.min = int(min)

    def set_max(self, max):
        self.max = int(max)

    def set_volume(self, volume):
        self.volume = int(volume)

    def set_sales(self, sales):
        self.sales = int(sales)

    def get_date(self):
        return self.date

    def get_code(self):
        return self.code

    def get_name(self):
        return self.name

    def get_market(self):
        return self.market

    def get_category(self):
        return self.category

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max

    def get_volume(self):
        return self.volume

    def get_sales(self):
        return self.sales
