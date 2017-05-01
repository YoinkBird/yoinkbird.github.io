from helpers import *
from feature_definitions import *
from txdot_parse import *

import pandas as pd
import numpy as np
import random
import datetime


import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

# src: https://www.kaggle.com/mchirico/d/nhtsa/2015-traffic-fatalities/bike-zoom-chicago-map/output
#  src https://www.kaggle.com/mchirico/d/nhtsa/2015-traffic-fatalities/bike-zoom-chicago-map/code

# Read data 
# import the "crash" data
datafile = "../data/txdot_2010_2017.csv"

(data,featdef) = preprocess_data(datafile)

# create string for 2d javascript array for the map
def df_as_js2d_arr_str(df, limit_for_testing=''):
  jsrows = "[\n"
  for rownum,row in df[:limit_for_testing].iterrows():
      #print(rownum)
      row_ind = df.index.get_loc(rownum)
      # TODO: remember that bin_crash_severity includes both incapacitating as well as killed
      imgurl = 'https://storage.googleapis.com/montco-stats/images/bike.png'
      if(row['bin_crash_severity']):
        imgurl = 'https://storage.googleapis.com/montco-stats/images/bikeKilled.png'
      # 'title', lat, lon, zindex, imgurl
      jsrows += "['%s', %s, %s, %d, '%s'],\n" % (row.crash_id, row.latitude,row.longitude, rownum, imgurl)
  jsrows += "];\n"
  return jsrows

# run for testing purposes
if(__name__ == '__main__'):
  verbose = 1
  if(verbose):
    print("-I-: testing kaggle bikezoom")
  mapdf = data[list(featdef[featdef.jsmap == True].index) + ['bin_crash_severity']].dropna()
  # add title attribute (i.e. column)
  mapdf['title'] = pd.Series(index=featdef.index,dtype=str).replace(np.nan,False)
  if(verbose):
    print("-I-: created mapdf")

#  print("-I-: creating total involved count")
#  individual_counts = [
#    'crash_death_count',
#    'crash_incapacitating_injury_count',
#    'crash_non-incapacitating_injury_count'
#    'crash_not_injured_count',
#    'crash_possible_injury_count',
#  ]
#  total_count = pd.Series(index=mapdf.index,dtype=int)
#  for icount in individual_counts:
#    total_count += mapdf[icount]
##    mapdf['person_number'] = mapdf['person_number'] + mapdf[icount]

  # generate rows
  if(verbose):
    print("-I-: generate javascript rows")
  limit_for_testing=6
  jsrows = df_as_js2d_arr_str(mapdf, limit_for_testing)
  print("-I-: javascript rows")
  print(jsrows)
  js2darr = 'var crashes =' + df_as_js2d_arr_str(mapdf, limit_for_testing)
  print("-I-: javascript 2d arr")
  print(js2darr)

print("-I-: DEVELOPMENT - current working progress")
print("-I-: html templates")
# Creating an HTML HEADER FILE
headV="""<!DOCTYPE html>
<html>
  <head>
  <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>bicycle accidents - severe and not severe</title>
    <style>
      html, body {
      height: 100%;
      margin: 0;
      padding: 0;
      }
      #map {
      height: 100%;
      }
    </style>
  </head>
  <body> 
      

      <!--  DataCanary_s fix -->
      <div id="map" class="main-container"></div>
    <script>

      function initMap() {
          //center: {lat: 41.7720713, lng: -87.5867187}
      var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 14,
        center: {lat: 30.2849, lng: -97.7341}
      
      });
      	 
      setMarkers(map);
      // Add traffic
      trafficLayer = new google.maps.TrafficLayer();
	  trafficLayer.setMap(map);	
	  
	  // Add bikeLayer
	  var bikeLayer = new google.maps.BicyclingLayer();
      bikeLayer.setMap(map);
	  
      }
"""

tailV="""      function setMarkers(map) {
      // Adds markers to the map.

      // Marker sizes are expressed as a Size of X,Y where the origin of the image
      // (0,0) is located in the top left of the image.

      // Origins, anchor positions and coordinates of the marker increase in the X
      // direction to the right and in the Y direction down.
      var image = {
            url: 'https://storage.googleapis.com/montco-stats/images/carCrash.png',

      // This marker is 20 pixels wide by 32 pixels high.
      size: new google.maps.Size(20, 32),
      // The origin for this image is (0, 0).
      origin: new google.maps.Point(0, 0),
      // The anchor for this image is the base of the flagpole at (0, 32).
      anchor: new google.maps.Point(0, 32)
      };
      // Shapes define the clickable region of the icon. The type defines an HTML
      // <area> element 'poly' which traces out a polygon as a series of X,Y points.
// The final coordinate closes the poly by connecting to the first coordinate.

      function htmlEntities(str) {
//         return String(str).replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
         return String(str).replace(/>/g, '&gt;').replace(/"/g, '&quot;');
       }

      var shape = {
      coords: [1, 1, 1, 20, 18, 20, 18, 1],
      type: 'poly'
      };
      
       for (var i = 0; i < crashes.length; i++) {
                          var crash = crashes[i];
                          var marker = new google.maps.Marker({
                          position: {lat: crash[1], lng: crash[2]},
                          map: map,
                          icon: crash[4],
                          shape: shape,
                          draggable: true,
                          title: htmlEntities(crash[0]),
                          zIndex: crash[3]
                          });
                          }
                          }

                          </script>

            <!--
            key="AIzaSyALU94pLkit5lx_QU62wnzOsO6y1H_BWfI"
            src="https://maps.googleapis.com/maps/api/js?key="+key+"&callback=initMap"></script>
            -->
        <script async defer
            src="https://maps.googleapis.com/maps/api/js?key=AIzaSyALU94pLkit5lx_QU62wnzOsO6y1H_BWfI&callback=initMap"></script>

  </body>
</html>
      
""" 
print("-I-: html gen")

# Write out 
f=open('__results__.html','w')
f.write(headV)
f.write(js2darr)
f.write(tailV)
f.close()

# Write out 
f=open('output.html','w')
f.write(headV)
f.write(js2darr)
f.write(tailV)
f.close()

print("-I-: DEVELOPMENT - End of working File")

## original approach
FILE="../input/accident.csv"
d=pd.read_csv(FILE)

FILE="../input/pbtype.csv"
b=pd.read_csv(FILE)

FILE="../input/person.csv"
person=pd.read_csv(FILE)

def f(x):
    year = x[0]
    month = x[1]
    day = x[2]
    hour = x[3]
    minute = x[4]
    # Sometimes they don't know hour and minute
    if hour == 99:
        hour = 0
    if minute == 99:
        minute = 0
    s = "%02d-%02d-%02d %02d:%02d:00" % (year,month,day,hour,minute)
    c = datetime.datetime.strptime(s,'%Y-%m-%d %H:%M:%S')
    return c
 
d['crashTime']   = d[['YEAR','MONTH','DAY','HOUR','MINUTE']].apply(f, axis=1)
d['crashDay']    = d['crashTime'].apply(lambda x: x.date())
d['crashMonth']  = d['crashTime'].apply(lambda x: x.strftime("%B") )
d['crashMonthN'] = d['crashTime'].apply(lambda x: x.strftime("%d") ) # sorting


db = pd.merge(d, b, how='right',left_on='ST_CASE', right_on='ST_CASE')

per = person[person['PER_TYP']==6][['ST_CASE','PER_NO','STR_VEH','DEATH_TM']]

# Throw this back in d
d = pd.merge(per, db, how='left',left_on=['ST_CASE','PER_NO'], right_on=['ST_CASE','PER_NO'])

# Throw this back in d
#d = db[db['PBPTYPE']==6][['ST_CASE','crashTime','PER_NO','LATITUDE','LONGITUD','FATALS','DRUNK_DR']]

# db['PBPTYPE']==6


# Set index
# d.index = pd.DatetimeIndex(d.timeStamp)



# TODO: s = 'var crashes =' + df_as_js2d_arr_str(mapdf, limit_for_testing)
s=' var crashes = [\n'


#  **  SELECT SECTION **





# So many points at exact location
def myRand():
    r=random.random()*0.001-0.0005
    return r

#d.lat=d.lat.apply(lambda x: str(float(x)+myRand()))
#d.lng=d.lng.apply(lambda x: str(float(x)+myRand()))





t=d[d['DEATH_TM']!=8888]
title=[]
for i in t.ST_CASE.tolist():
    title.append("ST_CASE:%d" % i)

desc=[]
for i in t.PER_NO.tolist():
    desc.append("PER_NO:%d" % i)

twp=[]
for i in t.DEATH_TM.tolist():
    twp.append("DEATH_TM:%d" % i)


#    var crashes = [ [displayTitle,lat,lon,image] ]
# var crashes = [ ['ST_CASE:10268 PER_NO:1 DEATH_TM:9999 2015-05-27 09:00:00 ', 30.26576667, -87.64966944, 0,'https://storage.googleapis.com/montco-stats/images/bikeKilled.png'],
imgkilled = 'https://storage.googleapis.com/montco-stats/images/bikeKilled.png'
timeStamp=t.crashTime.tolist()
lat=t.LATITUDE.tolist()
lng=t.LONGITUD.tolist()
for i in range(0,len(lat)):
    displayTitle="%s %s %s %s" % (title[i],desc[i],twp[i],timeStamp[i])
    displayTitle=displayTitle.replace('\n',' ')
    s+="['%s ', %s, %s, %s,'https://storage.googleapis.com/montco-stats/images/bikeKilled.png'],\n" % (displayTitle,lat[i],lng[i],i)


t=d[d['DEATH_TM']==8888]
title=t.ST_CASE.tolist()
desc=t.PER_NO.tolist()
twp=t.DEATH_TM.tolist()
timeStamp=t.crashTime.tolist()
lat=t.LATITUDE.tolist()
lng=t.LONGITUD.tolist()
for i in range(0,len(lat)):
    displayTitle="%s %s %s %s" % (title[i],desc[i],twp[i],timeStamp[i])
    displayTitle=displayTitle.replace('\n',' ')
    s+="['%s ', %s, %s, %s,'https://storage.googleapis.com/montco-stats/images/bike.png'],\n" % (displayTitle,lat[i],lng[i],i)




s+='];'

# Write out 
f=open('__results__.html','w')
f.write(headV)
f.write(s)
f.write(tailV)
f.close()

# Write out 
f=open('output.html','w')
f.write(headV)
f.write(s)
f.write(tailV)
f.close()

