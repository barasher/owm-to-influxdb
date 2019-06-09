#! /bin/bash

rm -rf work/*

oappid=${OTI_OWM_APPID?"No OpenWeatherMap appid specified"}
ostation=${OTI_OWM_STATION?"No OpenWeatherMap station specified"}
iurl=${OTI_IDB_URL?"No InfluxDB URL specified"}
idb=${OTI_IDB_DB?"No database specified"}
iloc=${OTI_IDB_LOC?"No localisation specified"}

python3 crawler.py -a $oappid -s $ostation -l $iloc > work/data.txt
status=$?
if [ $status -ne 0 ]; then
    exit 1
fi

./pusher -t 30s -u $iurl -d $idb -f work/data.txt
#cat work/data.txt
status=$?
if [ $status -ne 0 ]; then
    exit 1
fi
