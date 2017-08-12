# -*- coding:utf-8 -*-
import os
import sys
import glob
sys.path.append(os.pardir + '\\ProcessData\\src')
import RefineData
import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas as pd
import JapaneseHoliday
import shutil
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates

class ShowStockData:
    data_index = ["date", "code", "market", "name", "category", "start", "end", "min", "max", "volume", "sales"]

    def __init__(self):
        self.rd = RefineData.RefineData()
        pass

    def show_code_data(self, _db_dir, _db_file, _code):
        return self.rd.get_code_data_date_index(_db_dir, _db_file, _code)

    def show_date_data(self, _db_dir, _db_file, _date):
        return self.rd.get_date_data(_db_dir, _db_file, _date)

if __name__ == '__main__':
    import os
    import datetime
    average_day = [1, 2, 10]
    span_day = 25
    data_span_day = span_day + max(average_day)
    if int(datetime.datetime.today().hour) <= 19:
        today = datetime.datetime.today() - datetime.timedelta(days=1)
    else:
        today = datetime.datetime.today()
    first_loop = True

    # 前回のファイルを削除
    to_test_train = ['test', 'train']
    # for i_tt in range(len(to_test_train)):
    #     fig_save_path = os.path.split(os.path.split(os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0])[0])[0] + '\\data\\kdb\\stocks\\fig\\' + to_test_train[i_tt]
    #     if os.path.exists(fig_save_path):
    #          shutil.rmtree(fig_save_path)

    file_list = []
    day_count = 0
    tmp_day = today
    while day_count < 10:
        if tmp_day.weekday() != 5 and tmp_day.weekday() != 6:
            holiday_name = JapaneseHoliday.holiday_name(date=tmp_day.date())
            if holiday_name is None:
                break
        tmp_day -= datetime.timedelta(days=1)
        day_count += 1
    if int(tmp_day.day) < 16:
        half = "01"
    else:
        half = "02"
    year_month = tmp_day.strftime("%Y-%m")
    if (year_month + "_" + half) not in file_list:
        file_list.append(year_month + "_" + half)
    db_dir = os.path.split(os.path.split(os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0])[0])[0] + '\\data\\kdb\\stocks\\db\\'
    shd = ShowStockData()
    df = DataFrame(columns=shd.data_index)
    for filename in file_list:
        db_file = filename + '_stocks.db'
        print(filename)
        df = df.append(shd.show_date_data(db_dir, db_file, tmp_day.strftime('%Y-%m-%d')))
    df = pd.DataFrame(df, columns=(shd.data_index[0],
                                   shd.data_index[5],
                                   shd.data_index[8],
                                   shd.data_index[7],
                                   shd.data_index[6],
                                   shd.data_index[9],
                                   shd.data_index[1],
                                   shd.data_index[2],
                                   shd.data_index[3],
                                   shd.data_index[4],
                                   shd.data_index[10]))
    df = df.sort_index()
    df2 = df[df[shd.data_index[9]] > 0]

    for code in df2.code:
        if int(datetime.datetime.today().hour) <= 19:
            today = datetime.datetime.today() - datetime.timedelta(days=1)
        else:
            today = datetime.datetime.today()
        first_loop = True
        for i_day in range(10000):
            print(code)
            day_count = 0
            assume_day = today
            while day_count < 10:
                if assume_day.weekday() != 5 and assume_day.weekday() != 6:
                    holiday_name = JapaneseHoliday.holiday_name(date=assume_day.date())
                    if holiday_name is None:
                        break
                assume_day -= datetime.timedelta(days=1)
                day_count += 1

            day_count = 0
            view_day = assume_day - datetime.timedelta(days=1)
            while day_count < 10:
                if view_day.weekday() != 5 and view_day.weekday() != 6:
                    holiday_name = JapaneseHoliday.holiday_name(date=view_day.date())
                    if holiday_name is None:
                        break
                view_day -= datetime.timedelta(days=1)
                day_count += 1

            all_start_day_count = 0
            start_day_count = 0
            objective_day = []
            show_day = []
            while start_day_count < data_span_day:
                check_day = view_day - datetime.timedelta(days=all_start_day_count + start_day_count)
                if check_day.weekday() == 5 or check_day.weekday() == 6:
                    all_start_day_count += 1
                else:
                    holiday_name = JapaneseHoliday.holiday_name(date=check_day.date())
                    if holiday_name is not None:
                        all_start_day_count += 1
                    else:
                        start_day = check_day
                        objective_day.append(check_day.strftime("%Y-%m-%d"))
                        if start_day_count < span_day:
                            show_day.append(check_day.strftime("%Y-%m-%d"))
                        start_day_count += 1

            file_list = []
            for i in range(all_start_day_count + start_day_count):
                tmp_day = assume_day - datetime.timedelta(days=i)
                if int(tmp_day.day) < 16:
                    half = "01"
                else:
                    half = "02"
                year_month = tmp_day.strftime("%Y-%m")
                if (year_month + "_" + half) not in file_list:
                    file_list.append(year_month + "_" + half)
            db_dir = os.path.split(os.path.split(os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0])[0])[0] + '\\data\\kdb\\stocks\\db\\'
            shd = ShowStockData()
            df = DataFrame(columns=shd.data_index)
            for filename in file_list:
                db_file = filename + '_stocks.db'
                df = df.append(shd.show_code_data(db_dir, db_file, code))
                for i in range(len(df.index)):
                    dd = df.index[i]
                    df.ix[df.index[i], "date"] = matplotlib.dates.date2num(dd)
            df = pd.DataFrame(df, columns=(shd.data_index[0],
                                           shd.data_index[5],
                                           shd.data_index[8],
                                           shd.data_index[7],
                                           shd.data_index[6],
                                           shd.data_index[9],
                                           shd.data_index[1],
                                           shd.data_index[2],
                                           shd.data_index[3],
                                           shd.data_index[4],
                                           shd.data_index[10]))
            df = df.sort_index()

            if len(df) < span_day:
                break

            pd.set_option('mode.sim_interactive', True)
            fig, ax1 = plt.subplots()

            fig.set_figheight(0.9)
            fig.set_figwidth(0.9)
            fig.patch.set_facecolor('white')
            plt.axis('off')
            plt.gray()

            limit_day_d = datetime.datetime.strptime(show_day[len(show_day) - 1], "%Y-%m-%d")
            limit_day_u = datetime.datetime.strptime(show_day[0], "%Y-%m-%d")
            # candlestick_ohlc(ax1, df.truncate(before=limit_day_d, after=limit_day_u).values, width=0.4, colorup='#77d879', colordown='#db3f3f')

            ewma_x = df[shd.data_index[0]]
            ewma_y = pd.ewma(df[shd.data_index[6]], span=4)
            #plt.plot(ewma_x.truncate(before=limit_day), ewma_y.truncate(before=limit_day))
            plt.xlim(xmin=matplotlib.dates.date2num(limit_day_d) - 1, xmax=matplotlib.dates.date2num(limit_day_u) + 1)

            ewmstd_y_p3 = ewma_y + pd.ewmstd(df[shd.data_index[6]], span=4)
            ewmstd_y_m3 = ewma_y - pd.ewmstd(df[shd.data_index[6]], span=4)
            ax1.fill_between(ewma_x.truncate(before=limit_day_d, after=limit_day_u).index, ewmstd_y_m3.truncate(before=limit_day_d, after=limit_day_u), ewmstd_y_p3.truncate(before=limit_day_d, after=limit_day_u), facecolor='black')

            # mean_x = df[shd.data_index[0]]
            # mean_y = pd.rolling_mean(df[shd.data_index[6]], 3)
            # plt.plot(mean_x.truncate(before=limit_day), mean_y.truncate(before=limit_day))
            # std_y_p3 = mean_y + pd.rolling_std(df[shd.data_index[6]], 3)
            # std_y_m3 = mean_y - pd.rolling_std(df[shd.data_index[6]], 3)
            # ax1.fill_between(mean_x.truncate(before=limit_day).index, std_y_m3.truncate(before=limit_day), std_y_p3.truncate(before=limit_day))

            ax1.xaxis_date()
            #fig.autofmt_xdate()
            plt.tick_params(axis='x', labeltop='off', labelbottom='off')
            plt.tick_params(axis='y', labelleft='off', labelright='off')
            plt.grid(b=False)

            # 直近100日のデータをテストデータにする
            if i_day < 100:
                tt = 0
            else:
                tt = 1

            # check next day data
            assume_day_data = {}
            for i in range(len(shd.data_index)):
                assume_day_data[shd.data_index[i]] = df[shd.data_index[i]].ix[assume_day.strftime("%Y-%m-%d")]
                if shd.data_index[i] == 'date':
                    assume_day_data[shd.data_index[i]] = assume_day.strftime("%Y-%m-%d")

            if assume_day_data[shd.data_index[5]] < assume_day_data[shd.data_index[6]]: #次の日の初めが終わりより小さい
                fig_save_path = os.path.split(os.path.split(os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0])[0])[0] + '\\data\\kdb\\stocks\\fig\\' + to_test_train[tt] + '\\long'
            elif assume_day_data[shd.data_index[5]] > assume_day_data[shd.data_index[6]]: #初めが終わりより大きい
                fig_save_path = os.path.split(os.path.split(os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0])[0])[0] + '\\data\\kdb\\stocks\\fig\\' + to_test_train[tt] + '\\short'
            else:
                fig_save_path = os.path.split(os.path.split(os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0])[0])[0] + '\\data\\kdb\\stocks\\fig\\' + to_test_train[tt] + '\\eq'

            if not os.path.isdir(fig_save_path):
                os.makedirs(fig_save_path)

            fig_save_file = fig_save_path + "\\" + code + "_" + assume_day_data[shd.data_index[0]] + ".png"
            plt.savefig(fig_save_file)
            if first_loop:
                i_day -= 1
                first_loop = False
            else:
                today = assume_day - datetime.timedelta(days=1)

            print(fig_save_file)
            #plt.show()
            plt.close()