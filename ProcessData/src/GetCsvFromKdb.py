# -*- coding: utf-8 -*-
import os
import sys
import wget
import datetime

sys.path.append(os.pardir + "\\" + os.pardir + '\\ViewData\\src')
import GetBusinessDay

url_head = "http://k-db.com/stocks/"
url_foot = "?download=csv"
outpath = "D:\\workspace\\data\\kdb\\stocks\\csv"

tdy = datetime.datetime.today()
if 0 <= tdy.hour < 20:
    today = datetime.datetime.today() - datetime.timedelta(days=1)
else:
    today = datetime.datetime.today()

gbd = GetBusinessDay.GetBusinessDay()

delta_day = 30
day_list = gbd.get_business_day(today, delta_day)

f_header = "stocks_"
f_footer = ".csv"

for i in range(delta_day):
    f_day = day_list[delta_day - i - 1].strftime("%Y-%m-%d")
    fname = outpath + "\\" + f_header + f_day + f_footer
    if not os.path.exists(fname):
        url = url_head + f_day + url_foot
        print("downloading:" + url)
        filename = wget.download(url, out=fname)