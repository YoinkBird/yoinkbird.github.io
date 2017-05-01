import pandas as pd

#df.append(pd.DataFrame({'newthing':{'type':'str'}}).T


def get_feature_defs():
    # data.dropna().info()
    # note: crash_time is marked categorical because by default it is encoded as HH:mm and therefore not continuous
    feature_definitions = {
    'crash_id'                                 : {'type' : 'int',  'dummies':0, 'regtype' : 'categorical'  },
    'average_daily_traffic_amount'             : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'   },
    'average_daily_traffic_year'               : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'   },
    'crash_death_count'                        : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'  },
    'crash_incapacitating_injury_count'        : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'  },
    'crash_non-incapacitating_injury_count'    : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'  },
    'crash_not_injured_count'                  : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'  },
    'crash_possible_injury_count'              : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'  },
    'crash_severity'                           : {'type' : 'str',  'dummies':1, 'regtype' : 'categorical'  },
    'crash_year'                               : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'   },
    'crash_time'                               : {'type' : 'HH:mm','dummies':0, 'regtype' : 'categorical'   },
    'light_condition'                          : {'type' : 'str',  'dummies':1, 'regtype' : 'categorical'  },
    'day_of_week'                              : {'type' : 'str',  'dummies':1, 'regtype' : 'categorical'  },
    'intersecting_street_name'                 : {'type' : 'str',  'dummies':0, 'regtype' : 'categorical'  },
    'intersection_related'                     : {'type' : 'str',  'dummies':1, 'regtype' : 'categorical'  },
    'latitude'                                 : {'type' : 'gps',  'dummies':0, 'regtype' : 'continuous'   },
    'longitude'                                : {'type' : 'gps',  'dummies':0, 'regtype' : 'continuous'   },
    'manner_of_collision'                      : {'type' : 'str',  'dummies':1, 'regtype' : 'categorical'  },
    'medical_advisory_flag'                    : {'type' : 'str',  'dummies':0, 'regtype' : 'categorical'  },
    'object_struck'                            : {'type' : 'str',  'dummies':0, 'regtype' : 'categorical'  },
    'road_base_type'                           : {'type' : 'str',  'dummies':1, 'regtype' : 'categorical'  },
    'speed_limit'                              : {'type' : 'int',  'dummies':0, 'regtype' : 'continuous'   },
    'street_name'                              : {'type' : 'str',  'dummies':0, 'regtype' : 'categorical'  },
    'surface_condition'                        : {'type' : 'int',  'dummies':0, 'regtype' : 'categorical'  },
    'weather_condition'                        : {'type' : 'str',  'dummies':0, 'regtype' : 'categorical'  },
    }
    #'bin_crash_severity'                       : {'type' : 'float', 'dummies':0, 'regtype' : 'continuous'   },
    #'bin_intersection_related'                 : {'type' : 'float', 'dummies':0,   },
    #'bin_light_condition'                      : {'type' : 'float', 'dummies':0,   },
    #'bin_manner_of_collision'                  : {'type' : 'int',   'dummies':0,   },
    featdef = pd.DataFrame.from_dict(feature_definitions).transpose()
    return featdef


# add_feature(featdef, 'bin_crash_severity', {'type':'int','dummies':0,'regtype':'bin_cat'})
def add_feature(df, featname, featdict):
    # defaults to "useless" features - string which can't be dummied and is not continuous
    if('dummies' not in featdict):
        featdict['dummies'] = 0
    if('type' not in featdict):
        featdict['type'] = 'str'
    if('regtype' not in featdict):
        featdict['regtype'] = 'categorical'
    return df.append(pd.DataFrame({featname: featdict}).T)

# usage
# featdef = add_feature(featdef, 'bin_intersection_related', {'type':'int','regtype':'bin_cat'})
# featdef = add_feature(featdef, 'crash_time_dec', {'type' : 'float', 'dummies':1, 'regtype' : 'continuous'   })

if(__name__ == '__main__'):
    featdef = get_feature_defs()
    # testing
    # usage
    featdef = add_feature(featdef, 'bin_intersection_related', {'type':'int','regtype':'bin_cat'})
    featdef = add_feature(featdef, 'crash_time_dec', {'type' : 'float', 'dummies':1, 'regtype' : 'continuous'   })
