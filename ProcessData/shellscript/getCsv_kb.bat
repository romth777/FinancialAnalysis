@echo off
PATH=%PATH%;D:\tools\wget\bin
SETLOCAL enabledelayedexpansion
set YEAR=2016
set MONTH=04
set DAY=01
set WORKSPACE=D:\workspace\data\kdb\stocks\csv

set TYEAR=%date:~0,4%
set TMONTH=%date:~5,2%
set TDAY=%date:~8,2%

for /l %%y in (%YEAR%,1,%TYEAR%) do (
  set yy=%%y
  for /l %%m in (%MONTH%,01,12) do (
    set mm=%%m
    if %%m LSS 10 (
      set mm=0!mm!
    )
    for /l %%d in (%DAY%,1,31) do (
      set dd=%%d
      if %%d LSS 10 (
        set dd=0!dd!
      )
      set DT=!yy!-!mm!-!dd!
      set DF1=\stocks_
      set DF2=.csv
      set DF=!DF1!!DT!!DF2!
      if not exist %WORKSPACE%!DF! (
@rem       @echo wget -O %WORKSPACE%!DF! --wait=1 http://k-db.com/stocks/!DT!?download=csv
       @echo wget -O %WORKSPACE%!DF! --wait=1 http://k-db.com/stocks/!DT!^?download=csv
      )
      if !DT!==%TYEAR%-%TMONTH%-%TDAY% (
        pause
        exit
      )
    )
  )
)
