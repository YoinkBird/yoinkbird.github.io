
from sklearn.ensemble import RandomForestClassifier
from sklearn import (metrics, model_selection, linear_model, preprocessing, ensemble, neighbors)
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns
import numpy as np
import pandas as pd
import pprint as pp
import re
#import xgboost as xgb

# import the "crash" data
data = pd.read_csv("../data/txdot_2015.csv",header=7)

print(list(data.columns))
# preprocessing
# lowercase: http://stackoverflow.com/a/38931854
data.columns = data.columns.str.lower()
# remove spaces
data.columns = data.columns.str.replace(' ', '_')
# special cases
data.columns = data.columns.str.replace('crash_i_d', 'crash_id')
# process categorical data
if(1):
    # replace ['No Data','Not Applicable'] with NaN
    data.replace(to_replace='No Data', value=np.nan, inplace=True)
    data.replace(to_replace='Not Applicable', value=np.nan, inplace=True)
    # factorizable data
    # convert 'Wet' 'Dry' to '1' '0'
    data['surface_condition'] = data['surface_condition'].factorize()[0]
    # DOC: rename col http://stackoverflow.com/a/11346337
    data.rename(columns={'surface_condition':'surface_wet'})
    # print number of unique entries
    for colname in data.columns:
        print("% 4d : %s" % (len(data[colname].unique()), colname))
    # remove data which is has no importance
    # better to drop cols with all NaN and convert "unimportant" data to NaN
    #  - can't universally decide to drop col just based on uniqueness
    # e.g. all of object_struck is 'Not Applicable' and useless, but if surface_condition had only one value "dry" this would be important
    # ? for colname in data.columns:
    # colname = 'object_struck'
    # if(len(data[colname].unique()) == 1):
    #   print("-I-: dropping %s for having all homogenous values %s", (colname, data[colname].unique()[0]))
    #   data.drop(colname,axis=1,inplace=True)


    

print(data.head())
print(data.info())
if(1):
  data.describe()
  data.hist()
  data.corr().plot() # TODO: seaborn
  plt.show()
else:
  print("-I-: Skipping...")

pairplot_var_list = [
# 'crash_id',
 'average_daily_traffic_amount',
 'average_daily_traffic_year',
 'crash_death_count',
# 'crash_incapacitating_injury_count',
# 'crash_non-incapacitating_injury_count',
# 'crash_not_injured_count',
# 'crash_possible_injury_count',
 'crash_severity',
 'crash_time',
 'crash_year',
 'day_of_week',
# 'intersecting_street_name',
 'intersection_related',
# 'latitude',
 'light_condition',
# 'longitude',
 'manner_of_collision',
 'medical_advisory_flag',
 'number_of_entering_roads',
 'number_of_lanes',
# 'object_struck',
 'road_base_type',
 'speed_limit',
# 'street_name',
 'surface_condition'
 ]

dummies_needed_list = [
 'crash_severity',
 'day_of_week',
 'intersection_related',
 'light_condition',
 'manner_of_collision',
 'number_of_entering_roads',
 'road_base_type',
# 'surface_condition' # factorized
        ]

# tmp disable
if(0):
    sns.pairplot(data, vars=pairplot_var_list)
    plt.show()

# alternative visualisation
datapt = data.pivot_table(values=['crash_death_count','crash_incapacitating_injury_count','crash_non-incapacitating_injury_count'], index=['speed_limit','crash_time'])
print(datapt)

pp.pprint(list(pd.get_dummies(data[dummies_needed_list]).columns))
pp.pprint(list(pd.get_dummies(data[dummies_needed_list]).columns.str.replace('[,\s]+','_').str.lower()))
# http://stackoverflow.com/a/36285489 - use of columns=
pp.pprint(list(pd.get_dummies(data, columns=dummies_needed_list).columns.str.replace('[,\s]+','_').str.lower()))
'''
 'Dark, Lighted', 'dark_lighted_yes'
 'Dark, Not Lighted', 'dark_lighted_no'
 'Dark, Unknown Lighting', 'dark_lighted_unknown'
 'Dawn',
 'Daylight',
 'Dusk',
 'Unknown',
'''

