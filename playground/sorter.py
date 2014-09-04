
import parse
import math



#print parse.db

def num2deg(xtile, ytile, zoom):
  n = 2.0 ** zoom
  lon_deg = xtile / n * 360.0 - 180.0
  lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
  lat_deg = math.degrees(lat_rad)
  return (lat_deg, lon_deg)





eventTypes = set([record['event']['s'] for record in parse.db])
sortedRecords = {}

for event in set(eventTypes):
  sortedRecords[event] = []

for record in parse.db:
  sortedRecords[record['event']['s']].append(record)




#for r in sortedRecords['locationInteraction']:
#  print r

#print(sortedRecords)

#if record['event']['s'] == 'locationInteraction':
    
##print set(eventTypes)

