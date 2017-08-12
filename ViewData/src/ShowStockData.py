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


class ShowStockData:
    data_index = ["date", "code", "market", "name", "category", "start", "end", "min", "max", "volume", "sales"]

    def __init__(self):
        self.rd = RefineData.RefineData()
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

    day_count = 0
    view_day = today
    while day_count < 10:
        if view_day.weekday() != 5 and view_day.weekday() != 6:
            holiday_name = JapaneseHoliday.holiday_name(date=today.date())
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
        tmp_day = view_day - datetime.timedelta(days=i)
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
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)

    plt.subplots_adjust(wspace=0)
    daily_rate = df[shd.data_index[6]].ix[objective_day]
    daily_rate = daily_rate.pct_change() * 100
    daily_rate_ranged = daily_rate[objective_day]
    daily_rate_ranged_max = daily_rate_ranged.max()
    daily_rate_ranged_min = daily_rate_ranged.min()
    daily_rate_ranged_max = daily_rate_ranged_max - abs(daily_rate_ranged_max % 0.5) + 0.5
    daily_rate_ranged_min = daily_rate_ranged_min - abs(daily_rate_ranged_min % 0.5)
    daily_rate_ranged.ix[show_day].sort_index(ascending=True).plot(label='daily')
    for i in range(len(average_day)):
        tmp = pd.rolling_mean(daily_rate.sort_index(ascending=True), average_day[i])
        tmp.ix[show_day].sort_index(ascending=True).plot(label='ave'+str(average_day[i]), style='-')
    plt.tick_params(axis='x', labeltop='off', labelbottom='off')
    plt.tick_params(axis='y', labelleft='on', labelright='off')

    ax2 = fig.add_subplot(2, 2, 2, sharey=ax1)
    daily_rate_ranged.ix[show_day].hist(bins=15, orientation='horizontal')
    plt.tick_params(axis='y', labelleft='off', labelright='on')
    price_average = daily_rate_ranged.ix[show_day].mean()
    price_sigma = daily_rate_ranged.ix[show_day].std()
    price_today = daily_rate_ranged.ix[view_day.strftime("%Y-%m-%d"), shd.data_index[6]]
    price_today_sigma = abs(price_today - price_average) / price_sigma
    plt.title(("today=%.f/ave=%.1f/std=%.1f" %
             (df.ix[view_day.strftime("%Y-%m-%d"), shd.data_index[6]], price_average, price_today_sigma)))
    plt.annotate("", xy=(2, daily_rate_ranged.ix[view_day.strftime("%Y-%m-%d"), shd.data_index[6]]),
          xytext=(2.5, daily_rate_ranged.ix[view_day.strftime("%Y-%m-%d"), shd.data_index[6]]),
          arrowprops=dict(facecolor='black'),
          verticalalignment='center')

    ax3 = fig.add_subplot(2, 2, 3, sharex=ax1)
    data_index = shd.data_index[10]
    tmp = df[data_index].ix[show_day].sort_index(ascending=True)
    tmp = tmp.pct_change() * 100
    tmp.plot(kind='bar', width=1)
    plt.tick_params(axis='x', labeltop='off', labelbottom='on')
    plt.tick_params(axis='y', labelleft='on', labelright='off')

    plt.show()