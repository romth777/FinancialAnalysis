# -*- coding:utf-8 -*-
import os
import glob
import CsvManager
import DatabaseManager


class SetData:
    def __init__(self):
        pass

    @staticmethod
    def set_data(path, db_dir, db_file):
        dbm = DatabaseManager.DatabaseManager()
        for name in glob.glob(path):
            filename = os.path.basename(name)
            filename = os.path.splitext(filename)[0]
            filename = filename.split("_")[1]
            filename = filename.split("-")
            if int(filename[2]) < 16:
                half = "01"
            else:
                half = "02"
            if db_file == ".db":
                file = db_dir + filename[0] + "-" + filename[1] + "_" + half + db_file
            else:
                file = db_dir + filename[0] + "-" + filename[1] + "_" + half + "_" + db_file
            with dbm.connect(file) as conn:
                daily_data = list()
                print(name)
                cm = CsvManager.CsvManager()
                cm.read_line(name, daily_data)
                for one_data in daily_data:
                    code = one_data.get_code()
                    date = one_data.get_date()
                    check_date = date.split("-")
                    if check_date != filename:
                        break
                    check_cur = dbm.check_existence(conn, date, code)
                    check_row = check_cur.fetchone()
                    check_cur.close()
                    if check_row is None:
                        dbm.set_data(conn, one_data)
            dbm.disconnect(conn)

if __name__ == '__main__':
    import os
    import datetime
    year = datetime.datetime.today().strftime("%Y")
    month = datetime.datetime.today().strftime("%m")
    _path = os.path.split(os.path.split(os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0])[0])[0] + '\\data\\kdb\\stocks\\csv\\stocks_' + year + '-' + month + '-*.csv'
    _db_dir = os.path.split(os.path.split(os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0])[0])[0] + '\\data\\kdb\\stocks\\db\\'
    _db_file = 'stocks.db'
    sd = SetData()
    sd.set_data(_path, _db_dir, _db_file)