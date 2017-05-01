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

# create string for 2d javascript array for the map
# format:
# var crashes = [ ['<crash_id>', <lat>,      <lon>, <zIndex>,'<imgurl> # replaces gmaps pin'],
# var crashes = [ ['11243623', 30.28608823, -97.6805777, 0, 'https://storage.googleapis.com/montco-stats/images/bike.png'], ];
# original format:
# var crashes = [ ['<case id> <num persons> <severity> <date> <time>', <lat>,      <lon>, <zIndex>,'<imgurl> # replaces gmaps pin'],
# var crashes = [ ['ST_CASE:10268 PER_NO:1 DEATH_TM:9999 2015-05-27 09:00:00 ', 30.26576667, -87.64966944, 0,'https://storage.googleapis.com/montco-stats/images/bikeKilled.png'],
# ideas: crash_id: crash_id | severity | date | time
def df_as_js2d_arr_str(df, limit_for_testing=-1):
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

def get_map_df(data, featdef):
  mapdf = data[list(featdef[featdef.jsmap == True].index) + ['bin_crash_severity']].dropna()
  # add title attribute (i.e. column)
  mapdf['title'] = pd.Series(index=featdef.index,dtype=str).replace(np.nan,False)
  return mapdf

def get_html_map_from_df(data, featdef):
  mapdf = get_map_df(data,featdef)
  js2darr = 'var crashes =' + df_as_js2d_arr_str(mapdf)
  if(verbose):
    print("-I-: ...done")
  print("-I-: html gen")
  htmlpage = generate_map_html_page(js2darr)
  write_html_files(htmlpage)
  return htmlpage

# insert js into html templates
def generate_map_html_page(js2darr):
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
  <!--
  original source: https://www.kaggle.com/mchirico/d/nhtsa/2015-traffic-fatalities/bike-zoom-chicago-map/code
  -->
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
  htmlpage = "%s\n%s\n%s" % (headV, js2darr, tailV)
  return htmlpage


def write_html_files(htmlpage, filename='output.html'):
  # Write out 
  # not sure if __results__ is special
  f=open('__results__.html','w')
  f.write(htmlpage)
  f.close()

  # Write out 
  f=open(filename,'w')
  f.write(htmlpage)
  f.close()


# run for testing purposes
if(__name__ == '__main__'):
  verbose = 1
  if(verbose):
    print("-I-: testing map generation")
  # Read data 
  # import the "crash" data
  datafile = "../data/txdot_2010_2017.csv"

  (data,featdef) = preprocess_data(datafile)
  # consolidated function
  get_html_map_from_df(data,featdef)
  print("-I-: DEVELOPMENT - current effort")


  # manual testing of each function
  if(0):
    print("-I-: ##############################")
    print("-I-: testing each function manually")
    # generate map dataframe
    mapdf = get_map_df(data,featdef)
    if(verbose):
      print("-I-: created mapdf")

    # generate javascript rows
    if(verbose):
      print("-I-: generate javascript rows")
    quicktest = 0
    if(quicktest):  # generate limited array, print results
      limit_for_testing=6
      jsrows = df_as_js2d_arr_str(mapdf, limit_for_testing)
      print("-I-: javascript rows")
      print(jsrows)
      print("-I-: javascript 2d arr")
      js2darr = 'var crashes =' + df_as_js2d_arr_str(mapdf)
      print(js2darr)
    else: # generate full array, don't print results (i.e. don't fill up screen)
      print("-I-: javascript 2d arr")
      js2darr = 'var crashes =' + df_as_js2d_arr_str(mapdf)
      print("-I-: ...done")

    # generate, write the html
    print("-I-: html gen")
    htmlpage = generate_map_html_page(js2darr)
    print("-I-: html write")
    # name 'from_fns' indicates that each function was called individually to create this file
    write_html_files(htmlpage, 'output_from_fns.html')
    # display in qtconsole - not working though
    # src http://stackoverflow.com/a/35760941
    from IPython.core.display import display, HTML
    display(HTML(htmlpage))
  print("-I-: DEVELOPMENT - current working progress")

print("-I-: DEVELOPMENT - End of working File")

