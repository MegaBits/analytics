

import csv





def getLocations(records):
 if type(records) is type(dict()):
  return [(i['x'], i['y']) for i in records if 'x' in i and 'y' in i]
 else:
  raise TypeError("parameter \'records\' is not type \'dict\'!")

def writeLocationsToCsv(records, filename):
 if type(records) is type(dict()):
  coords = [[i['x'], i['y']] for i in records if 'x' in i and 'y' in i]
  with open(filename, 'wb') as f:
   writer = csv.writer(f)
   writer.writerows(coords)
 else:
   raise TypeError("parameter \'records\' is not type \'dict\'!")
