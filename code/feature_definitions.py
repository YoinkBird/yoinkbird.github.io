import pandas as pd

#df.append(pd.DataFrame({'newthing':{'type':'str'}}).T


'''
register attrributes here which need to be defaulted to False
this is almost any new attribute
'''
def get_list_of_attributes():
    attlist = ['target','jsmap']
    return attlist
def get_feature_defs():
    # data.dropna().info()
    # note: crash_time is marked categorical because by default it is encoded as HH:mm and therefore not continuous
    # note: 'street' is same as 'str' but doesn't get lowercased. use 'name' for string which needs to be untouched
    # jsmap : this var can be used to generate the javascript map
    feature_definitions = {
    'crash_id'                                 : {'target':0, 'type' : 'int',    'dummies':0, 'origin':False,  'regtype' : 'categorical' , 'pairplot':0, 'jsmap':1,  },
    'average_daily_traffic_amount'             : {'target':0, 'type' : 'int',    'dummies':0, 'origin':False,  'regtype' : 'continuous'  , 'pairplot':0, 'jsmap':0,  },
    'average_daily_traffic_year'               : {'target':0, 'type' : 'int',    'dummies':0, 'origin':False,  'regtype' : 'continuous'  , 'pairplot':0, 'jsmap':0,  },
    'crash_death_count'                        : {'target':1, 'type' : 'int',    'dummies':0, 'origin':False,  'regtype' : 'continuous'  , 'pairplot':1, 'jsmap':0,  },
    'crash_incapacitating_injury_count'        : {'target':1, 'type' : 'int',    'dummies':0, 'origin':False,  'regtype' : 'continuous'  , 'pairplot':0, 'jsmap':0,  },
    'crash_non-incapacitating_injury_count'    : {'target':1, 'type' : 'int',    'dummies':0, 'origin':False,  'regtype' : 'continuous'  , 'pairplot':0, 'jsmap':0,  },
    'crash_not_injured_count'                  : {'target':1, 'type' : 'int',    'dummies':0, 'origin':False,  'regtype' : 'continuous'  , 'pairplot':0, 'jsmap':0,  },
    'crash_possible_injury_count'              : {'target':1, 'type' : 'int',    'dummies':0, 'origin':False,  'regtype' : 'continuous'  , 'pairplot':0, 'jsmap':0,  },
    'crash_severity'                           : {'target':1, 'type' : 'str',    'dummies':1, 'origin':False,  'regtype' : 'categorical' , 'pairplot':0, 'jsmap':0,  },
    'crash_year'                               : {'target':0, 'type' : 'int',    'dummies':0, 'origin':False,  'regtype' : 'continuous'  , 'pairplot':1, 'jsmap':0,  },
    'crash_time'                               : {'target':0, 'type' : 'HH:mm',  'dummies':0, 'origin':False,  'regtype' : 'categorical' , 'pairplot':0, 'jsmap':0,  },
    'light_condition'                          : {'target':0, 'type' : 'str',    'dummies':1, 'origin':False,  'regtype' : 'categorical' , 'pairplot':0, 'jsmap':0,  },
    'day_of_week'                              : {'target':0, 'type' : 'str',    'dummies':1, 'origin':False,  'regtype' : 'categorical' , 'pairplot':0, 'jsmap':0,  },
    'latitude'                                 : {'target':0, 'type' : 'gps',    'dummies':0, 'origin':False,  'regtype' : 'continuous'  , 'pairplot':0, 'jsmap':1,  },
    'longitude'                                : {'target':0, 'type' : 'gps',    'dummies':0, 'origin':False,  'regtype' : 'continuous'  , 'pairplot':0, 'jsmap':1,  },
    'manner_of_collision'                      : {'target':0, 'type' : 'str',    'dummies':1, 'origin':False,  'regtype' : 'categorical' , 'pairplot':0, 'jsmap':0,  },
    'medical_advisory_flag'                    : {'target':1, 'type' : 'str',    'dummies':0, 'origin':False,  'regtype' : 'categorical' , 'pairplot':0, 'jsmap':0,  },
    'object_struck'                            : {'target':0, 'type' : 'str',    'dummies':0, 'origin':False,  'regtype' : 'categorical' , 'pairplot':0, 'jsmap':0,  },
    'road_base_type'                           : {'target':0, 'type' : 'str',    'dummies':1, 'origin':False,  'regtype' : 'categorical' , 'pairplot':0, 'jsmap':0,  },
    'speed_limit'                              : {'target':0, 'type' : 'int',    'dummies':0, 'origin':False,  'regtype' : 'continuous'  , 'pairplot':1, 'jsmap':0,  },
    'street_name'                              : {'target':0, 'type' : 'street', 'dummies':0, 'origin':False,  'regtype' : 'categorical' , 'pairplot':0, 'jsmap':0,  },
    'intersecting_street_name'                 : {'target':0, 'type' : 'street', 'dummies':0, 'origin':False,  'regtype' : 'categorical' , 'pairplot':0, 'jsmap':0,  },
    'intersection_related'                     : {'target':0, 'type' : 'str',    'dummies':1, 'origin':False,  'regtype' : 'categorical' , 'pairplot':0, 'jsmap':0,  },
    'surface_condition'                        : {'target':0, 'type' : 'int',    'dummies':0, 'origin':False,  'regtype' : 'categorical' , 'pairplot':0, 'jsmap':0,  },
    'weather_condition'                        : {'target':0, 'type' : 'str',    'dummies':0, 'origin':False,  'regtype' : 'categorical' , 'pairplot':0, 'jsmap':0,  },
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
    for attr in get_list_of_attributes():
        featdef[attr].replace(0, False, inplace=True)
        featdef[attr].replace(1, True, inplace=True)
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
    for attr in get_list_of_attributes():
        if(attr not in featdict):
            featdict[attr] = False

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
    featdef.set_value('bin_crash_time', 'origin', 'crash_time')
