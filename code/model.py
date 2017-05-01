
from helpers import *
from feature_definitions import *
from txdot_parse import *
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

# import the "crash" data
datafile = "../data/txdot_2010_2017.csv"

(data,featdef) = preprocess_data(datafile)


print(data.head())
print(data.info())
if(1):
  data.describe()
  data.hist()
  data.corr().plot() # TODO: seaborn
  plt.show()
else:
  print("-I-: Skipping...")

# alternative visualisation
datapt = data.pivot_table(values=['crash_death_count','crash_incapacitating_injury_count','crash_non-incapacitating_injury_count'], index=['speed_limit','crash_time'])
print(datapt)


# inspect features with high covariance
pairplot_bin_var_list = list(featdef[featdef['pairplot']].index)
if(0):
    sns.pairplot(data, vars=pairplot_var_list)
    plt.show()

# list of vars which become dummie'd
dummies_needed_list = list(featdef[featdef.dummies == 1].index)

# dummies
# http://stackoverflow.com/a/36285489 - use of columns
data_dummies = pd.get_dummies(data, columns=dummies_needed_list)
# no longer need to convert headers, already done in process_data_punctuation
pp.pprint(list(data_dummies))

# pca stub
# pca = decomposition.PCA(svd_solver='full')
# pca.fit(pd.get_dummies(data[dummies_needed_list])).transform(pd.get_dummies(data[dummies_needed_list]))

'''
pandas tricks
filtering
http://stackoverflow.com/a/11872393
# select data with average_daily_traffic_amount but intersecting_street_name null
# => busy roads without an intersection
data[~data['average_daily_traffic_amount'].isnull() & data['intersecting_street_name'].isnull()]

# select intersection_related == 'Non Intersection' and intersecting_street_name null
# => verify whether intersecting_street_name==null indicates that there is no intersection
# => then only display the columns pertaining to street names
data[(data['intersection_related'] == 'Non Intersection') & data['intersecting_street_name'].isnull()][['street_name','intersecting_street_name','intersection_related']]

data[(data['intersection_related'] == 'Non Intersection') & data['intersecting_street_name'].isnull()][colgrps['intersection']]
'''

print("-I-: train-test split")

# predictors  = list(featdef[(featdef.regtype == 'bin_cat') & (featdef.target != True)].index)
# responsecls = list(featdef[(featdef.regtype == 'bin_cat') & (featdef.target == True)].index)
predictors = [
# 'crash_time',
# 'crash_time_dec',
 'bin_intersection_related',
 'bin_light_condition',
 'bin_manner_of_collision',
 ]
responsecls = [
 'bin_crash_severity'
 ]
testsize = 0.3
data_nonan = data[ predictors + responsecls ].dropna()
X_train, X_test, y_train, y_test = model_selection.train_test_split(data_nonan[predictors],data_nonan[responsecls], test_size=testsize)

from sklearn import tree
clf = tree.DecisionTreeClassifier() #max_depth = 5)
clf.fit(X_train,y_train)

# prediction and scoring
print("-I-: cross_val_score on train (itself)")
print(model_selection.cross_val_score(clf, X_train, y_train.values.ravel()))
y_pred = clf.predict_proba(X_test)
print("-I-: cross_val_score against test")
print(model_selection.cross_val_score(clf, X_test, y_test.values.ravel()))

# DOC: How to interpret decision trees' graph results and find most informative features?
# src: http://stackoverflow.com/a/34872454
print("-I-: most important features:")
for i in np.argsort(clf.feature_importances_)[::-1]:
  print("%f : %s" % (clf.feature_importances_[i],predictors[i]))

# plotting important features
for i in np.argsort(clf.feature_importances_)[::-1]:
  feat = predictors[i]
  feat = predictors[i].replace('bin_','')
  pltkind = 'pie'
  if(featdef.ix[feat].origin):
      feat_orig = featdef.ix[predictors[i]].origin
      data[feat].value_counts().plot(kind=pltkind, title="%s - original values for %s" % (feat_orig, feat))
  else:
      data[feat].value_counts().plot(kind=pltkind, title="%s " % (feat))
  plt.show()

print("time of day:")
timelbl = sorted(data.crash_time_30m.unique())
ax_time = plt.subplot(111)
#ax_time.set_xticks(range(0,24))
time_hrs = range(0,2400,200)
timelbl = []
for i in time_hrs:
    timelbl.append("%02d:%02d" % (i//100,i%100))
ax_time.set_xticks(time_hrs)
ax_time.set_xticklabels(timelbl, rotation=45, rotation_mode="anchor",ha="right")
ax_time.set_title("crash time rounded to 30 min")
data.crash_time.hist(bins=48,ax=ax_time)
plt.show()
# data.crash_time_30m.value_counts(sort=False).plot(kind='pie');plt.show()
# /plotting important features

# display tree criteria
# src: http://scikit-learn.org/stable/modules/tree.html#classification
from IPython.display import Image
# pydot plus had to be installed as python -m pip
# src : http://stackoverflow.com/a/42469100
import pydotplus
dot_data = tree.export_graphviz(clf, out_file=None,
        feature_names=predictors,
        class_names=['0']+responsecls, # seems to require at least two class names
        rounded=True,
        filled=True,
        # proportion = True,  : bool, optional (default=False) When set to True, change the display of ‘values’ and/or ‘samples’ to be proportions and percentages respectively.

        )
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png() , retina=True)
print("-I-: if img doesn't show, run \n Image(pydotplus.graph_from_dot_data(dot_data).create_png() , retina=True)")
print("-I-: End of File")


# miscellaneous
'''
# look into dictvectorizer dv.get_feature_names http://stackoverflow.com/a/34194521
'''
# DOC
# feature importance and feature selection
# e.g. reducing complexity of a tree model
# https://www.analyticsvidhya.com/blog/2016/12/introduction-to-feature-selection-methods-with-an-example-or-how-to-select-the-right-variables/
# 
# automatically discarding low-importance features
# http://scikit-learn.org/stable/modules/feature_selection.html#feature-selection-using-selectfrommodel
