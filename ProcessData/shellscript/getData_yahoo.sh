#!/bin/sh
rm -f index*.html*code*
i=2331
while test $i -lt 10000
do
    # | を用いることで前の処理後の入力を引き継いで継続処理することができる
    # && 前の処理が正常終了したら次のコマンドを実行する
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
