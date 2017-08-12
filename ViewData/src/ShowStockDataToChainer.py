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
import GetData

class ShowStockData:
    data_index = ["date", "code", "market", "name", "category", "start", "end", "min", "max", "volume", "sales"]

    def __init__(self):
        self.rd = RefineData.RefineData()
        self.gd = GetData.GetData()
        pass

    def show_code_data(self, _db_dir, _db_file, _code):
        return self.rd.get_code_data(_db_dir, _db_file, _code)

if __name__ == '__main__':
    import os
    import datetime
    average_day = [5, 25, 75]
    span_day = 10
    # 暫定で50足す
    data_span_day = span_day + max(average_day)
    code = "1570-T"
    if int(datetime.datetime.today().hour) <= 19:
        today = datetime.datetime.today() - datetime.timedelta(days=1)
    else:
        today = datetime.datetime.today()
    first_loop = True

    # 前回のファイルを削除
    to_test_train = ['test', 'train']
    for i_tt in range(len(to_test_train)):
        fig_save_path = os.path.split(os.path.split(os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0])[0])[0] + '\\data\\kdb\\stocks\\fig\\' + to_test_train[i_tt]
        if os.path.exists(fig_save_path):
             shutil.rmtree(fig_save_path)

    for i_day in range(600):
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
            print(filename)
            df = df.append(shd.show_code_data(db_dir, db_file, code))

        pd.set_option('mode.sim_interactive', True)
        fig = plt.figure(figsize=(0.75, 0.75)) # グラフのサイズを決める
        fig.patch.set_facecolor('white')
        ax1 = fig.add_subplot(2, 1, 1)
        plt.ylim([-15, 15])

        daily_rate = df[shd.data_index[6]].ix[objective_day]
        daily_rate = daily_rate.pct_change() * 100
        plt.subplots_adjust(wspace=0)
        plt.rcParams['axes.linewidth'] = 0
        plt.rcParams['xtick.major.width'] = 0
        plt.rcParams['ytick.major.width'] = 0
        plt.rcParams['xtick.color'] = 'white'
        plt.rcParams['ytick.color'] = 'white'

        daily_rate_ranged = daily_rate[objective_day]
        daily_rate_ranged_max = daily_rate_ranged.max()
        daily_rate_ranged_min = daily_rate_ranged.min()
        daily_rate_ranged_max = daily_rate_ranged_max - abs(daily_rate_ranged_max % 0.5) + 0.5
        daily_rate_ranged_min = daily_rate_ranged_min - abs(daily_rate_ranged_min % 0.5)
        daily_rate_ranged.ix[show_day].sort_index(ascending=True).plot(label='daily', color='black')
        # for i in range(len(average_day)):
        #     tmp = pd.rolling_mean(daily_rate.sort_index(ascending=True), average_day[i])
        #     tmp.ix[show_day].sort_index(ascending=True).plot(label='ave'+str(average_day[i]), style='-')
        plt.tick_params(axis='x', labeltop='off', labelbottom='off')
        plt.tick_params(axis='y', labelleft='on', labelright='off')
        plt.grid(b=False)

        plt.rcParams['axes.linewidth'] = 0
        plt.rcParams['xtick.major.width'] = 0
        plt.rcParams['ytick.major.width'] = 0
        plt.rcParams['xtick.color'] = 'white'
        plt.rcParams['ytick.color'] = 'white'

        ax3 = fig.add_subplot(2, 1, 2, sharex=ax1)
        plt.ylim([-200, 200])
        data_index = shd.data_index[10]
        tmp = df[data_index].ix[show_day].sort_index(ascending=True)
        tmp = tmp.pct_change() * 100
        tmp.plot(kind='bar', width=1, color='black')
        plt.tick_params(axis='x', labeltop='off', labelbottom='off')
        plt.tick_params(axis='y', labelleft='on', labelright='off')
        plt.grid(b=False)
#        plt.tight_layout()

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

        if assume_day_data[shd.data_index[5]] < assume_day_data[shd.data_index[6]]: #初めが終わりより小さい
            fig_save_path = os.path.split(os.path.split(os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0])[0])[0] + '\\data\\kdb\\stocks\\fig\\' + to_test_train[tt] + '\\short'
        elif assume_day_data[shd.data_index[5]] > assume_day_data[shd.data_index[6]]: #初めが終わりより大きい
            fig_save_path = os.path.split(os.path.split(os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0])[0])[0] + '\\data\\kdb\\stocks\\fig\\' + to_test_train[tt] + '\\large'
        else: #初めが終わりと等しい
            fig_save_path = os.path.split(os.path.split(os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0])[0])[0] + '\\data\\kdb\\stocks\\fig\\' + to_test_train[tt] + '\\eq'

        if not os.path.isdir(fig_save_path):
            os.makedirs(fig_save_path)

        fig_save_file = fig_save_path + "\\" + assume_day_data[shd.data_index[0]] + ".png"
        plt.savefig(fig_save_file)
        if first_loop:
            i_day -= 1
            first_loop = False
        else:
            today = assume_day - datetime.timedelta(days=1)
        plt.gray()
        #plt.show()
        print(fig_save_file)
        plt.close()