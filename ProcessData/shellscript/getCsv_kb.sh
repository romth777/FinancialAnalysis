#!/bin/sh
rm -f index*.html*code*
YEAR=2007
MONTH=01
DAY=01

for YEAR in 2007 2008 2009 2010 2011 2012 2013 2014
do
for MONTH in 01 02 03 04 05 06 07 08 09 10 11 12
do
for DAY in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
do
	wget -O ${YEAR}${MONTH}${DAY}_price.csv http://k-db.com/stocks/date=$YEAR-$MONTH-$DAY?download=csv
    mv *_price.csv ./data/
    sleep 3s
done
done
done
