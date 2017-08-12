# -*- coding:utf-8 -*-
import gzip
import os
import sys
import numpy as np
import six
import pandas as pd

sys.path.append(os.pardir + "\\" + os.pardir + '\\ProcessData\\src')
sys.path.append(os.pardir + "\\" + os.pardir + '\\ViewData\\src')

import RefineData
import datetime


class ChainerDataManager:
        def __init__(self, _path):
            self.rd = RefineData.RefineData()
            self.pkl_name = _path
            self.num_train = 450
            self.num_test = 100 # テーブル数
            self.span = 20 # 1テーブルあたりのデータ取得日数
            self.data_sets = 4 # 1日あたりのデータセット数（平均データ等）
            self.data_names = 5 # 1データセットあたりのデータ種類数（4本値+出来高）
            self.target_cat_num = 3 # 最終的な出力ノードの数（分類数）
            self.dim = self.span * self.data_sets * self.data_names
            self.code = "1570-T"
            self.start_date_1570T = datetime.datetime.strptime("2013-07-16", "%Y-%m-%d")
        pass

        def load_a_stock(self, _date, _span, _with_target=True):
            if isinstance(_date, str):
                _date = datetime.datetime.strptime(_date, "%Y-%m-%d")

            # data
            rolling_span = [1, 5, 25, 75]
            num = max(rolling_span) + _span
            data_ohlc = self.rd.get_ohlc(self.rd.get_db_dir(), _date, num, self.code)

            data_ohlc1 = np.round(self.rd.get_rolling_mean(data_ohlc, _day=rolling_span[0]))
            data_ohlc2 = np.round(self.rd.get_rolling_mean(data_ohlc, _day=rolling_span[1]))
            data_ohlc3 = np.round(self.rd.get_rolling_mean(data_ohlc, _day=rolling_span[2]))
            data_ohlc4 = np.round(self.rd.get_rolling_mean(data_ohlc, _day=rolling_span[3]))

            data1 = data_ohlc1[0:_span]
            data2 = data_ohlc2[0:_span]
            data3 = data_ohlc3[0:_span]
            data4 = data_ohlc4[0:_span]
            data1.columns = ["start1", "end1", "max1", "min1", "volume1"]
            data2.columns = ["start2", "end2", "max2", "min2", "volume2"]
            data3.columns = ["start3", "end3", "max3", "min3", "volume3"]
            data4.columns = ["start4", "end4", "max4", "min4", "volume4"]

            data = pd.concat([data1, data2, data3, data4], axis=1)

            if _with_target:
                # target : 0:マイナス、1:イコール、2:プラス
                target = 1
                target_span = 1

                data_ohlc_target = self.rd.get_ohlc(self.rd.get_db_dir(), _date + datetime.timedelta(days=target_span), target_span, self.code)
                # 0.5%以上の変動をキャッチ
                if data_ohlc_target["end"][0] >= data_ohlc_target["start"][0] * 1.005:
                    target = np.array([0, 0, 1])
                elif data_ohlc_target["end"][0] <= data_ohlc_target["start"][0] * 0.995:
                    target = np.array([1, 0, 0])
                else:
                    target = np.array([0, 1, 0])

            return data, target

        # data:開始日(ここから遡る)/num:データセットの数/span:1つのデータセットに含まれる日数
        def load_stocks(self, _date, _num, _span, _with_target):
            # 出力データ領域確保
            data = np.zeros(_num * _span * self.data_sets * self.data_names, dtype=np.uint64).reshape((_num, _span * self.data_sets * self.data_names))
            target = np.zeros(_num * self.target_cat_num, dtype=np.uint8).reshape((_num, self.target_cat_num))

            sum_space_day = 0
            if isinstance(_date, str):
                _date = datetime.datetime.strptime(_date, "%Y-%m-%d")
            for i_day in range(_num):
                tmp_date, space_day = self.rd.get_work_date(_date - datetime.timedelta(days=i_day + sum_space_day))
                sum_space_day += space_day
                print("load_stocks:" + str(i_day + 1) + "/" + str(_num) + " " + tmp_date.strftime("%Y-%m-%d"))
                t_data, t_target = self.load_a_stock(tmp_date, _span, _with_target)
                data[i_day] = np.array(t_data.values.flatten())
                target[i_day] = t_target
            return data, target

        # data:開始日(ここから遡る)/num:データセットの数/span:1つのデータセットに含まれる日数
        def load_stocks_with_timestep_array(self, _date, _num, _span, _with_target):
            # 出力データ領域確保
            data = np.zeros(_num * _span * self.data_sets * self.data_names, dtype=np.uint64).reshape((_num, _span, self.data_sets * self.data_names))
            target = np.zeros(_num * self.target_cat_num, dtype=np.uint8).reshape((_num, self.target_cat_num))

            sum_space_day = 0
            if isinstance(_date, str):
                _date = datetime.datetime.strptime(_date, "%Y-%m-%d")
            for i_day in range(_num):
                tmp_date, space_day = self.rd.get_work_date(_date - datetime.timedelta(days=i_day + sum_space_day))
                sum_space_day += space_day
                print("load_stocks:" + str(i_day + 1) + "/" + str(_num) + " " + tmp_date.strftime("%Y-%m-%d"))
                t_data, t_target = self.load_a_stock(tmp_date, _span, _with_target)
                data[i_day] = np.array(t_data)
                target[i_day] = t_target
            return data, target

        def download_stock_data(self, _start_date, _span, _num_train, _num_target, _with_target):
            print('Setting Start date...')
            start_day_target = self.rd.get_last_work_date(_start_date, _num_target)
            start_day_train = self.rd.get_last_work_date(start_day_target, _num_train)

            if start_day_train < self.start_date_1570T:
                print("download_stock_date:Err start date over limit")

            start_day_train = start_day_target - datetime.timedelta(days=1)
            start_day_target = _start_date

            print('Done')

            print('Converting test data...')
            #data_test, target_test = self.load_stocks(start_day_target, _num_target, _span, _with_target)
            data_test, target_test = self.load_stocks_with_timestep_array(start_day_target, _num_target, _span, _with_target)
            print('Done')

            print('Converting training data...')
            #data_train, target_train = self.load_stocks(start_day_train, _num_train, _span, _with_target)
            data_train, target_train = self.load_stocks_with_timestep_array(start_day_train, _num_train, _span, _with_target)
            print('Done')


            # trainとtestデータをマージ、target:label, data:data
            stock = {}
            stock['data'] = np.append(data_train, data_test, axis=0)
            stock['target'] = np.append(target_train, target_test, axis=0)

            print('Done')
            print('Save output...')
            with open(self.pkl_name, 'wb') as output:
                six.moves.cPickle.dump(stock, output, -1)
            print('Done')
            print('Convert completed')

        def load_stock_data(self, _start_date):
            if not os.path.exists(self.pkl_name):
                self.download_stock_data(_start_date, self.span, self.num_train, self.num_test)
            with open(self.pkl_name, 'rb') as stock_pickle:
                stock = six.moves.cPickle.load(stock_pickle)
            return stock

        def load_stock_data_dqn(self, _start_date):
            if not os.path.exists(self.pkl_name):
                self.download_stock_data(_start_date, self.span, self.num_train, self.num_test, _with_target=False)
            with open(self.pkl_name, 'rb') as stock_pickle:
                stock = six.moves.cPickle.load(stock_pickle)
            return stock

if __name__ == '__main__':
    cdm = ChainerDataManager()
    cdm.download_stock_data("2016-03-14", cdm.span, cdm.num_train, cdm.num_test)
