# -*- coding:utf-8 -*-
import JapaneseHoliday
import datetime

class GetBusinessDay:
    day_list = []

    def __init__(self):
        self.day_list = []
        pass

    def get_business_day(self, today, delta):
        day_delta = 0

        # delta日だけfor文を回す
        for i in range(delta):
            view_day = today
            day_limit = 0
            # 20は20日以上の連休が発生しないという前提のもと立てた無限ループ防止
            # day_limitが連休カウント
            # day_deltaにはdelta分だけ日付前の日付の差分がカウントされていく
            # 土日でなく、祝日でない場合break。それ以外は土日祝日以外の日までさかのぼり
            while day_limit < 20:
                view_day = today - datetime.timedelta(days=day_delta)
                day_delta += 1
                # 土曜か日曜日でなければ
                if not(view_day.weekday() == 5 or view_day.weekday() == 6):
                    # 祝日でなければ
                    holiday_name = JapaneseHoliday.holiday_name(year=view_day.year, month=view_day.month, day=view_day.day)
                    if holiday_name is None:
                        break
                day_limit += 1
            self.day_list.append(view_day)
        return self.day_list
