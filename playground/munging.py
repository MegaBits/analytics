

import csv
import math




def getLocations(records, clearNulls=True):
 if type(records) is type(list()):
  if clearNulls:
   return [[i['x'], i['y']] for i in records if 'x' in i and 'y' in i and i['x'] is not 0 and i['y'] is not 0]
  else:
   return [[i['x'], i['y']] for i in records if 'x' in i and 'y' in i]
 else:
  raise TypeError("parameter \'records\' is not type \'list\'!")

def getTimestampedLocations(records, clearNulls=True):
 if type(records) is type(list()):
  if clearNulls:
   return [(i['timestamp'], [i['x'], i['y']]) for i in records if 'x' in i and 'y' in i and 'timestamp' in i and i['x'] is not 0 and i['y'] is not 0 and i['timestamp'] is not 0]
  else:
   return [(i['timestamp'], [i['x'], i['y']]) for i in records if 'x' in i and 'y' in i and 'timestamp' in i]
 else:
  raise TypeError("parameter \'records\' is not type \'list\'!") 

def writeLocationsToCsv(records, filename, clearNulls=True):
 if type(records) is type(list()):
  #if clearNulls:
  # coords = [[i['x'], i['y']] for i in records if 'x' in i and 'y' in i and i['x'] is not 0 and i['y'] is not 0]
  #else:
  # coords = [[i['x'], i['y']] for i in records if 'x' in i and 'y' in i]
  with open(filename, 'wb') as f:
   writer = csv.writer(f)
   writer.writerows(records)
 else:
   raise TypeError("parameter \'records\' is not type \'list\'!")

def boundLocationBySquare(records, lat1, lon1, lat2, lon2): # (lat1,lon1) -> top left corner // (lat2,lon2) -> bottom right corner
 if type(records) is type(list()):
  coords = [num2deg(i[0], i[1], 20) for i in records if i[0] is not 0 and i[1] is not 0]
  print(len(coords))
  bounded = []
  for i in coords:
   if i[1] > lat1 and i[0] > lon1 and i[1] < lat2 and i[0] < lon2:
    bounded.append((i[0], i[1]))
  return bounded
 else:
  raise TypeError("parameter \'records\' is not type \'list\'!")

def num2deg(xtile, ytile, zoom):
 n = 2.0 ** zoom
 lon_deg = xtile / n * 360.0 - 180.0
 lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
 lat_deg = math.degrees(lat_rad)
 return (lat_deg, lon_deg)


