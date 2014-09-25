

import csv





def getLocations(records, clearNulls=True):
 if type(records) is type(list()):
  if clearNulls:
   return [[i['x'], i['y']] for i in records if 'x' in i and 'y' in i and i['x'] is not 0 and i['y'] is not 0]
  else:
   return [[i['x'], i['y']] for i in records if 'x' in i and 'y' in i]
 else:
  raise TypeError("parameter \'records\' is not type \'list\'!")

def writeLocationsToCsv(records, filename, clearNulls=True):
 if type(records) is type(list()):
  if clearNulls:
   coords = [[i['x'], i['y']] for i in records if 'x' in i and 'y' in i and i['x'] is not 0 and i['y'] is not 0]
  else:
   coords = [[i['x'], i['y']] for i in records if 'x' in i and 'y' in i]
  with open(filename, 'wb') as f:
   writer = csv.writer(f)
   writer.writerows(coords)
 else:
   raise TypeError("parameter \'records\' is not type \'list\'!")
