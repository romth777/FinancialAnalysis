# -*- coding:utf-8 -*-
import os
import sys
import glob

sys.path.append(os.pardir + '\\ProcessData\\src')
import RefineData
from pandas import DataFrame
import pandas as pd
import json
import datetime
import codecs
import GetBusinessDay
import DatabaseManager

class ShowDailyData:
    data_index = ["code", "market", "name", "category", "start", "end", "min", "max", "volume", "sales"]

    def __init__(self):
        self.rd = RefineData.RefineData()
        pass

    def show_date_data(self, _db_dir, _db_file, _date):
        return self.rd.get_date_data(_db_dir, _db_file, _date)


if __name__ == '__main__':
    # 今日の日付を設定する
    # 19時より前はcsvファイルが更新されていない可能性があるので前日のデータを利用する
    if int(datetime.datetime.today().hour) <= 19:
        today = datetime.datetime.today() - datetime.timedelta(days=1)
    else:
        today = datetime.datetime.today()

    # 土日、祝日を除くdata_span_day日分前までのdateリストを作成する。
    data_span_day = 60
    gbd = GetBusinessDay.GetBusinessDay()
    business_days = gbd.get_business_day(today, data_span_day)

    # 指定日（start_day）～本日（view_day）までのすべての日付に対して対応するDBファイル名を決定する
    # ファイル名はfile_listに日付をkeyとして記録する
    file_list = {}
    day_list = []
    dbm = DatabaseManager.DatabaseManager()
    for one_day in business_days:
        file_list[one_day.strftime("%Y-%m-%d")] = dbm.get_db_name(one_day)
        day_list.append(one_day.strftime("%Y-%m-%d"))

    # 表示用に指定のbusiness_daysをjsonファイルに保存
    file_path = "D:\\workspace\\src\\trunk\\Finance\\ViewData\\src\\data\\"
    file_path += "date.json"
    if os.path.isfile(file_path):
        os.remove(file_path)
    f = codecs.open(file_path, "w", "utf-8")
    f.write(json.dumps(day_list, sort_keys=True, indent=4, ensure_ascii=False))
    f.close()

    # 指定日～本日までのすべてのデータを取得する
    sdd = ShowDailyData()
    df = DataFrame(columns=sdd.data_index)
    for date in file_list.keys():
        print(date)
        ret = sdd.show_date_data(dbm.get_db_dir(), file_list[date], date)
        df = df.append(ret)

    # 本日分の全てのcategoryを抽出する
    df_today_category = df.loc[business_days[0].strftime("%Y-%m-%d"), "category"]

    # 指定日～本日までのデータを探索する
    print("Get category Data")
    for day in business_days:
        print(day.strftime("%Y-%m-%d"))
        # 異常データを排除する為に、salesとendの値も取得する
        # 異常データは読み込み時にsales=0, start/end/min/max=-1としている
        df_day_sales = df.loc[day.strftime("%Y-%m-%d"), "sales"]
        df_day_end = df.loc[day.strftime("%Y-%m-%d"), "end"]

        # 本日分の全てのcategoryから重複分を取り除き、その全てのcategoryについてfor文を回す
        file_path = "D:\\workspace\\src\\trunk\\Finance\\ViewData\\src\\data\\"
        file_path += day.strftime("%Y-%m-%d") + "_category.json"
        stats = DataFrame()
        for cat in range(df_today_category.drop_duplicates().__len__()):
            # 本日分のデータの内、catで指定されたcategoryのものを抽出
            # 同時にsalesが0かつendが-1のものは取引されていないので除外
            ddf = DataFrame(df.loc[day.strftime("%Y-%m-%d")].loc[(df.loc[day.strftime("%Y-%m-%d"), "category"] == df_today_category.drop_duplicates().iloc[cat]) & (df_day_sales != 0) & (df_day_end != -1)])
            d = DataFrame(ddf["end"] / ddf["start"])
            stat = d.describe()
            stat.columns = [df_today_category.drop_duplicates().iloc[cat]]
            stats = pd.concat([stats, stat], axis=1)
        stats.columns.name = day.strftime("%Y-%m-%d")
        if os.path.isfile(file_path):
            os.remove(file_path)
        f = codecs.open(file_path, "w", "utf-8")
        tmp = json.loads(stats.to_json(orient="columns"))
        f.write(json.dumps(tmp, sort_keys=True, indent=4, ensure_ascii=False))
        f.close()
