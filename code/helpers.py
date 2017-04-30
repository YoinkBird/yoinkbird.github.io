# helper functions

# don't need most of these imports
from sklearn.ensemble import RandomForestClassifier
from sklearn import (metrics, model_selection, linear_model, preprocessing, ensemble, neighbors, decomposition)
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns
import numpy as np
import pandas as pd
import pprint as pp
import re
#import xgboost as xgb

def print_test():
    print("hi")
    return("hi")

# time conversions
# convert integer crashtime to datetime with year
# input: dataframe with year and time (int)
# todo: add month
def create_datetime_series(df):
    if('crash_month' in df):
        print("-E-: function can't handle months yet")
        return False
    return pd.to_datetime(df.apply(lambda x: "%s.%04d" % (x.crash_year,x.crash_time), axis=1),format="%Y.%H%M")
# convert to 24h time
# data.crash_time = data.crash_time.apply(lambda x: str(x).zfill(4)) # leading zeros
# could convert to datetime, but this forces a year,month,day to be present
# pd.to_datetime(data.crash_time.apply(lambda x: "2015%s"%x),format="%Y%H%M") # http://strftime.org/
# data.apply(lambda x: "%s%s" % (x.crash_year,x.crash_time), axis=1) # flexible year
# data['datetime'] = pd.to_datetime(data.crash_time.apply(lambda x: "2015%s"%x),format="%Y%H%M")
# src: http://stackoverflow.com/a/32375581
# pd.to_datetime(data.crash_time.apply(lambda x: "2015%s"%x),format="%Y%H%M").dt.time
# final:
# convert to decimal time
# src: https://en.wikipedia.org/wiki/Decimal_time#Scientific_decimal_time
# convert hours to fraction of day (HH/24) and minutes to fraction of day (mm/24*60), then add together
def time_base10(time):
    import pandas as pd
    time = pd.tslib.Timestamp(time)
    dech = time.hour/24; decm = time.minute/(24*60)
    #print("%s %f %f %f" % (time.time(), dech, decm, dech+decm))
    base10 = dech+decm
    return base10
def time_base10_to_60(time):
    verbose = 0
    # only round on final digit
    hours10 = time * 24  # 0.9 * 24  == 21.6
    hours10 = round(hours10, 5) # round out floating point issues
    hours24 = int(hours10)  # int(21.6) == 21
    min60 = round((hours10 * 60) % 60)     # 21.6*60 == 1296; 1296%60 == 36
    if(verbose):
        print("time: %f | hours24 %s | hours10 %s | min60 %s" % (time,hours24,hours10,min60))
    return hours24 * 100 + min60
# round to half hour
def time_round30min(pd_ts_time):
    import datetime
    pd_ts_time = pd.tslib.Timestamp(pd_ts_time)
    newtime = datetime.time()
    retmin = 61
    if(pd_ts_time.minute < 16):
        newtime = datetime.time(pd_ts_time.hour,0)
        retmin = 00
    elif((pd_ts_time.minute > 15) & (pd_ts_time.minute < 46)):
        newtime = datetime.time(pd_ts_time.hour,30)
        retmin = "30"
    elif(pd_ts_time.minute > 45):
        pd_ts_time += datetime.timedelta(hours=1)
        newtime = datetime.time(pd_ts_time.hour,00)
        retmin = 00
    #print("%s %s %f %f" % (pd_ts_time.pd_ts_time(), newtime, newtime.hour, newtime.minute))
    time_str = "%s.%02d%02d" % (pd_ts_time.year, newtime.hour, newtime.minute)
    # omit - would have to specify the year
    # time2 = pd.tslib.Timestamp("%02d:%02d" % (newtime.hour, newtime.minute))
    if(0):
        time2 = pd.to_datetime(time_str, format="%Y.%H%M")
    else:
        time_str = "%02d%02d" % (newtime.hour, newtime.minute)
        time2 = int(time_str)
    return time2

if(__name__ == '__main__'):
    # testing - visual inspection
    if(1):
        print("verify correct operation of time_base10")
        # not testing 24:00 -> 1.0 because "hour must be in 0..23" for dateutil
        testtimes1 = ["0:00", "4:48"  , "7:12"  , "21:36" , "23:59"     , "0:59"      , "23:00"    ] # "24:00"
        testtimes2 = [0.0   , 0.2     , 0.3     , 0.9     , 0.999305556 , 0.040972222 , 0.958333333] # 1.0
        for i, testtime in enumerate(testtimes1):
            rettime = time_base10(testtime)
            status = "FAIL"
            # round for comparisson because floating point gets messy
            if(round(testtimes2[i],4) == round(rettime,4)):
                status = "PASS"
            print("%s: %6s: %s == %s ?" % (status, testtime , testtimes1[i] , rettime))
        print("verify correct operation of time_base10_to_60")
        for i, testtime in enumerate(testtimes2):
            status = "FAIL"
            rettime = time_base10_to_60(testtime)
            if(int(testtimes1[i].replace(':','')) == rettime):
                status = "PASS"
            print("%s: %6f: %s == %s ?" % (status, testtime , testtimes1[i] , rettime,))
    if(1):
        print("verify correct operation of time_round30min")
        testtimes1 = ["0:00" , "0:14" , "0:15" , "0:16", "0:29","0:30","0:31","0:44","0:45","0:46", "4:48"  , "7:12"  , "21:36" , "23:59"]
        testtimes2 = ["0:00" , "0:00" , "0:00" , "0:30", "0:30","0:30","0:30","0:30","0:30","1:00", "5:00"  , "7:00"  , "21:30" , "00:00"]
        for i, testtime in enumerate(testtimes1):
            #rettime = time_round30min(pd.tslib.Timestamp(testtime))
            rettime = time_round30min(testtime)
            status = "FAIL"
            if(int(testtimes2[i].replace(':','')) == rettime):
                status = "PASS"
            print("%s: %6s: %s == %s ?" % (status, testtime , testtimes2[i] , rettime))
