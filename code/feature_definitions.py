import pandas as pd

#df.append(pd.DataFrame({'newthing':{'type':'str'}}).T


def get_feature_defs():
    # data.dropna().info()
    # note: crash_time is marked categorical because by default it is encoded as HH:mm and therefore not continuous
    # note: 'street' is same as 'str' but doesn't get lowercased. use 'name' for string which needs to be untouched
    feature_definitions = {
    'crash_id'                                 : {'type' : 'int',  'dummies':0, 'regtype' : 'categorical' , 'pairplot':0,  },
    'average_daily_traffic_amount'             : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'  , 'pairplot':0,  },
    'average_daily_traffic_year'               : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'  , 'pairplot':0,  },
    'crash_death_count'                        : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'  , 'pairplot':1, },
    'crash_incapacitating_injury_count'        : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'  , 'pairplot':0, },
    'crash_non-incapacitating_injury_count'    : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'  , 'pairplot':0, },
    'crash_not_injured_count'                  : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'  , 'pairplot':0, },
    'crash_possible_injury_count'              : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'  , 'pairplot':0, },
    'crash_severity'                           : {'type' : 'str',  'dummies':1, 'regtype' : 'categorical' , 'pairplot':0,  },
    'crash_year'                               : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'  , 'pairplot':1,  },
    'crash_time'                               : {'type' : 'HH:mm','dummies':0, 'regtype' : 'categorical' , 'pairplot':0,   },
    'light_condition'                          : {'type' : 'str',  'dummies':1, 'regtype' : 'categorical' , 'pairplot':0,  },
    'day_of_week'                              : {'type' : 'str',  'dummies':1, 'regtype' : 'categorical' , 'pairplot':0,  },
    'latitude'                                 : {'type' : 'gps',  'dummies':0, 'regtype' : 'continuous'  , 'pairplot':0,  },
    'longitude'                                : {'type' : 'gps',  'dummies':0, 'regtype' : 'continuous'  , 'pairplot':0,  },
    'manner_of_collision'                      : {'type' : 'str',  'dummies':1, 'regtype' : 'categorical' , 'pairplot':0,  },
    'medical_advisory_flag'                    : {'type' : 'str',  'dummies':0, 'regtype' : 'categorical' , 'pairplot':0,  },
    'object_struck'                            : {'type' : 'str',  'dummies':0, 'regtype' : 'categorical' , 'pairplot':0,  },
    'road_base_type'                           : {'type' : 'str',  'dummies':1, 'regtype' : 'categorical' , 'pairplot':0,  },
    'speed_limit'                              : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'  , 'pairplot':1,  },
    'street_name'                              : {'type' : 'street',  'dummies':0, 'regtype' : 'categorical' , 'pairplot':0,  },
    'intersecting_street_name'                 : {'type' : 'street',  'dummies':0, 'regtype' : 'categorical' , 'pairplot':0,  },
    'intersection_related'                     : {'type' : 'str',  'dummies':1, 'regtype' : 'categorical' , 'pairplot':0,  },
    'surface_condition'                        : {'type' : 'int',  'dummies':0, 'regtype' : 'categorical' , 'pairplot':0,  },
    'weather_condition'                        : {'type' : 'str',  'dummies':0, 'regtype' : 'categorical' , 'pairplot':0,  },
    }
    #'bin_crash_severity'                       : {'type' : 'float', 'dummies':0, 'regtype' : 'continuous'   },
    #'bin_intersection_related'                 : {'type' : 'float', 'dummies':0,   },
    #'bin_light_condition'                      : {'type' : 'float', 'dummies':0,   },
    #'bin_manner_of_collision'                  : {'type' : 'int',   'dummies':0,   },
    featdef = pd.DataFrame.from_dict(feature_definitions).transpose()
    # hand-entry is '0','1' for simplicity
    # dataframe is 'False,'True' for easier selection
    featdef['dummies'].replace(0,False, inplace=True)
    featdef['dummies'].replace(1,True, inplace=True)
    featdef.pairplot.replace(0,False, inplace=True)
    featdef.pairplot.replace(1,True, inplace=True)
    # add attribute for <...>
    ## attname = '...'
    ## df[attname] = pd.Series(index=featdef.index,dtype=bool).replace(True,False)
    return featdef


# add_feature(featdef, 'bin_crash_severity', {'type':'int','dummies':0,'regtype':'bin_cat'})
def add_feature(df, featname, featdict):
    # defaults to "useless" features - string which can't be dummied and is not continuous
    if('dummies' not in featdict):
        featdict['dummies'] = False
    if('type' not in featdict):
        featdict['type'] = 'str'
    if('regtype' not in featdict):
        featdict['regtype'] = 'categorical'
    if('pairplot' not in featdict):
        featdict['pairplot'] = False

    # special defaults
    if('type' in featdict):
        if(featdict['type'] == 'bin_cat'):
            if('pairplot' not in featdict):
                featdict['pairplot'] = True
    # done
    return df.append(pd.DataFrame({featname: featdict}).T)

def add_attribute_bool(df, attname, attvalue=False):
    if(attname not in df):
        # new series
        ser = pd.Series(index=featdef.index,dtype=bool).replace(True,False)
        # ser = pd.Series(index=featdef.index).fillna(attvalue, downcast='infer')
        df[attname] = ser
    return df

# usage
# featdef = add_feature(featdef, 'bin_intersection_related', {'type':'int','regtype':'bin_cat'})
# featdef = add_feature(featdef, 'crash_time_dec', {'type' : 'float', 'dummies':1, 'regtype' : 'continuous'   })

if(__name__ == '__main__'):
    featdef = get_feature_defs()
    # testing
    # usage
    featdef = add_feature(featdef, 'bin_intersection_related', {'type':'int','regtype':'bin_cat'})
    featdef = add_feature(featdef, 'crash_time_dec', {'type' : 'float', 'dummies':1, 'regtype' : 'continuous'   })
    featdef = add_attribute_bool(featdef, 'pairplot')
    # http://stackoverflow.com/a/24517695
    featdef.set_value('crash_time', 'pairplot', True)
