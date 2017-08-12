#!/bin/sh
rm -f index*.html*code*
i=2331
while test $i -lt 10000
do
    # | ��p���邱�ƂőO�̏�����̓��͂������p���Ōp���������邱�Ƃ��ł���
    # && �O�̏���������I�������玟�̃R�}���h�����s����
    echo $i
    echo "$i," > tmp
    wget --random-wait http://stocks.finance.yahoo.co.jp/stocks/detail/?code=$i.T && \
    cat index.html?code=$i.T | grep "stoksPrice" \
    | sed 's/[^0-9]*//' | sed 's/[^0-9]*$//' | sed 's/\,//' >>tmp

    cat tmp | tr -d '\n' | sed -e "s/\$/\n/" >>./data/`date +%Y%m%d`_price.csv
    rm -f tmp
    i=`expr $i + 1`
    sleep 3s
    rm -f index*.html*code*
done
