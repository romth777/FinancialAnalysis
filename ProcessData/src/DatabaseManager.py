# -*- coding: utf-8 -*-
import os
import sqlite3

class DatabaseManager:
    def __init__(self):
        pass

    @staticmethod
    def connect(_name):
        conn = sqlite3.connect(_name, isolation_level=None)
        conn.execute("PRAGMA journal_mode=MEMORY")
        conn.text_factory = str
        return conn

    @staticmethod
    def disconnect(_conn):
        _conn.commit()
        _conn.close()

    @staticmethod
    def check_existence(_conn, _date, _code):
        cur = _conn.cursor()
        DatabaseManager.create_table(cur)
        return _conn.execute("""SELECT date_tbl, code_tbl FROM stockDay o WHERE EXISTS (SELECT 'X' FROM stockDay i WHERE ((date_tbl = ?) AND (code_tbl = ?)))""", (_date, _code))

    @staticmethod
    def get_from_date_code(_conn, _date, _code):
        cur = _conn.cursor()
        DatabaseManager.create_table(cur)
        return _conn.execute("""SELECT date_tbl, code_tbl, market_tbl, name_tbl, category_tbl, start_tbl, end_tbl, min_tbl, max_tbl, volume_tbl, sales_tbl FROM stockDay WHERE ((date_tbl=?) AND (code_tbl=?))""", (_date, _code))

    @staticmethod
    def get_from_date(_conn, _date):
        cur = _conn.cursor()
        DatabaseManager.create_table(cur)
        return _conn.execute("""SELECT date_tbl, code_tbl, market_tbl, name_tbl, category_tbl, start_tbl, end_tbl, min_tbl, max_tbl, volume_tbl, sales_tbl FROM stockDay WHERE (date_tbl=?)""", (_date,))

    @staticmethod
    def get_from_code(_conn, _code):
        cur = _conn.cursor()
        DatabaseManager.create_table(cur)
        return _conn.execute("""SELECT date_tbl, code_tbl, market_tbl, name_tbl, category_tbl, start_tbl, end_tbl, min_tbl, max_tbl, volume_tbl, sales_tbl FROM stockDay WHERE (code_tbl=?)""", (_code,))

    @staticmethod
    def get_from_name(_conn, _name):
        return _conn.execute("""SELECT date_tbl, code_tbl, market_tbl, name_tbl, category_tbl, start_tbl, end_tbl, min_tbl, max_tbl, volume_tbl, sales_tbl FROM stockDay WHERE (name_tbl=?)""", (_name,))

    @staticmethod
    def get_from_market(_conn, _market):
        return _conn.execute("""SELECT date_tbl, code_tbl, market_tbl, name_tbl, category_tbl, start_tbl, end_tbl, min_tbl, max_tbl, volume_tbl, sales_tbl FROM stockDay WHERE (market_tbl=?)""", (_market,))

    @staticmethod
    def get_from_category(_conn, _category):
        return _conn.execute("""SELECT date_tbl, code_tbl, market_tbl, name_tbl, category_tbl, start_tbl, end_tbl, min_tbl, max_tbl, volume_tbl, sales_tbl FROM stockDay WHERE (category_tbl=?)""", (_category,))

    @staticmethod
    def set_data(_conn, _data):
        cur = _conn.cursor()
        DatabaseManager.create_table(cur)
        cur.execute("""INSERT INTO stockDay\
            (date_tbl,\
            code_tbl,\
            market_tbl,\
            name_tbl,\
            category_tbl,\
            start_tbl,\
            end_tbl,\
            min_tbl,\
            max_tbl,\
            volume_tbl,\
            sales_tbl) VALUES(?,?,?,?,?,?,?,?,?,?,?)""", \
                    (_data.get_date(), \
                     _data.get_code(), \
                     _data.get_market(), \
                     _data.get_name(), \
                     _data.get_category(), \
                     _data.get_start(), \
                     _data.get_end(), \
                     _data.get_min(), \
                     _data.get_max(), \
                     _data.get_volume(), \
                     _data.get_sales()))

    @staticmethod
    def create_table(_cur):
        _cur.execute("""CREATE TABLE IF NOT EXISTS stockDay\
            (date_tbl TEXT,\
            code_tbl TEXT,\
            market_tbl TEXT,\
            name_tbl TEXT,\
            category_tbl TEXT,\
            start_tbl DOUBLE,\
            end_tbl DOUBLE,\
            min_tbl DOUBLE,\
            max_tbl DOUBLE,\
            volume_tbl DOUBLE,\
            sales_tbl DOUBLE);""")

    @staticmethod
    def get_db_name(_date):
        if isinstance(_date, str):
            _date = datetime.datetime.strptime(_date, "%Y-%m-%d")

        if int(_date.day) < 16:
            half = "01"
        else:
            half = "02"
        year_month = _date.strftime("%Y-%m")
        return year_month + "_" + half

    @staticmethod
    def get_db_dir():
        return os.path.split(os.path.split(os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0])[0])[0] + '\\data\\kdb\\stocks\\db\\'
