#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER6
"""


from time import localtime, strftime, mktime, strptime
from datetime import datetime, timezone
import pytz

Now = 1407694710
Local_tuple = localtime(Now)
Time_Format = '%Y-%m-%d %H:%M:%S'
Time_Str = strftime(Time_Format, Local_tuple)
print(Time_Str)

Utc_Now = mktime(strptime(Time_Str,Time_Format))
print(Utc_Now)

Parse_Format = '%Y-%m-%d %H:%M:%S %Z'
Depart_Sfo = '2014-05-01 15:45:16 PDT'
# Time_Tuple_Cannot_Work_on_Windows = strptime(Depart_Sfo, Parse_Format)
# Time_Str_Cannot_Work_on_Windows = strftime(Time_Format, Time_Tuple_Cannot_Work_on_Windows)
# print(Time_Str_Cannot_Work_on_Windows)


Now = datetime(2018, 1, 3, 0, 0 , 0)
Now_Utc = Now.replace(tzinfo=timezone.utc)
Now_Local = Now_Utc.astimezone()
print(Now_Local)

Time_Str = '2018-01-03 09:00:00'
Now = datetime.strptime(Time_Str, Time_Format)
Time_Tuple = Now.timetuple()
Utc_Now = mktime(Time_Tuple)
print(Utc_Now)
print()

Arrival_Nyc = '2018-01-03 09:00:00'
Nyc_Dt_Native = datetime.strptime(Arrival_Nyc, Time_Format)
Eastern = pytz.timezone('US/Eastern')
Nyc_Dt = Eastern.localize(Nyc_Dt_Native)
Utc_Dt = pytz.utc.normalize(Nyc_Dt.astimezone(pytz.utc))
print(Nyc_Dt)
print(Utc_Dt)

Pacific = pytz.timezone('US/Pacific')
Sf_Dt = Pacific.normalize(Utc_Dt.astimezone(Pacific))
print(Sf_Dt)

Tokyo = pytz.timezone('Asia/Tokyo')
Tokyo_Dt = Tokyo.normalize(Utc_Dt.astimezone(Tokyo))
print(Tokyo_Dt)
