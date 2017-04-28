# impute missing speed limits

# dataframe with all -1 and 0 valued speed_limits, only three 'speed_limit','street_name','intersecting_street_name'
data2 = data[((data.speed_limit == -1) | (data.speed_limit == 0)) & (~data.intersecting_street_name.isnull())][['speed_limit','street_name','intersecting_street_name']]

# new dataframe. concat all street-pairs without limit from original dataframe
# i.e. contains all 
df3 = pd.DataFrame()
for ser in data2.iterrows(): 
  #print (ser[1].street_name)
  df3 = pd.concat([df3,data[(data['street_name'] == ser[1].street_name) & (data['intersecting_street_name'] == ser[1].intersecting_street_name)]],axis=0)

# find limits - all valid limits and valid intersecting_street_name
df3[~((df3.speed_limit == 0) | (df3.speed_limit == -1)) & ~(df3.intersecting_street_name.isnull() | (df3.intersecting_street_name == "UNKNOWN"))][['speed_limit','street_name','intersecting_street_name']]

# remove duplicates of intersection,speed_limit
df3[~((df3.speed_limit == 0) | (df3.speed_limit == -1)) & ~(df3.intersecting_street_name.isnull() | (df3.intersecting_street_name == "UNKNOWN"))][['speed_limit','street_name','intersecting_street_name']].drop_duplicates()
# remove duplicates of intersection , i.e. without regards to speed_limit
df3[~((df3.speed_limit == 0) | (df3.speed_limit == -1)) & ~(df3.intersecting_street_name.isnull() | (df3.intersecting_street_name == "UNKNOWN"))][['street_name','intersecting_street_name']].drop_duplicates()

# unique missing intersections with unique speed limit (e.g. one intersection, several limits)
df3[((df3.speed_limit == 0) | (df3.speed_limit == -1)) & ~(df3.intersecting_street_name.isnull() | (df3.intersecting_street_name == "UNKNOWN"))][['speed_limit','street_name','intersecting_street_name']].drop_duplicates().shape


# original dataset, overall number of missing data
# total missing speed limits for intersections
data[((data.speed_limit == 0) | (data.speed_limit == -1)) & ~(data.intersecting_street_name.isnull() | (data.intersecting_street_name == "UNKNOWN"))][['street_name','intersecting_street_name']].shape
# Out[174]: (279, 2)

# unique missing intersections (e.g. one intersection with any speed limit)
data[((data.speed_limit == 0) | (data.speed_limit == -1)) & ~(data.intersecting_street_name.isnull() | (data.intersecting_street_name == "UNKNOWN"))][['street_name','intersecting_street_name']].drop_duplicates().shape
# Out[179]: (253, 2)


