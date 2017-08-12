@echo off
PATH=%PATH%;D:\tools\wget\bin
SETLOCAL enabledelayedexpansion
set YEAR=%date:~0,4%
set MONTH=%date:~5,2%
set DAY=%date:~8,2%
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
      set DF="\stocks_"!DT!".csv"

      if not exist %WORKSPACE%!DF! (
       wget -O %WORKSPACE%!DF! --wait=1 http://k-db.com/stocks/!DT!?download=csv
      )
      if !DT!==%TYEAR%-%TMONTH%-%TDAY% (
        exit
      )
    )
  )
)
