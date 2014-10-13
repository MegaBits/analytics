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
  #print(len(coords))
  bounded = []
  for i in coords:
   if i[1] > lat1 and i[0] > lon1 and i[1] < lat2 and i[0] < lon2:
    bounded.append((i[0], i[1]))
  return bounded
 else:
  raise TypeError("parameter \'records\' is not type \'list\'!")

def recordsBoundedLocationBySquare(records, lat1, lon1, lat2, lon2):
 if type(records) is type(list()):
  coords = [num2deg(i[0], i[1], 20) for i in records if i[0] is not 0 and i[1] is not 0]
  #print(len(coords))
  bounded = []
  for i in coords:
   if i[1] > lat1 and i[0] > lon1 and i[1] < lat2 and i[0] < lon2:
    bounded.append((record)
  return bounded
 else:
  raise TypeError("parameter \'records\' is not type \'list\'!")

def num2deg(xtile, ytile, zoom):
 n = 2.0 ** zoom
 lon_deg = xtile / n * 360.0 - 180.0
 lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
 lat_deg = math.degrees(lat_rad)
 return (lat_deg, lon_deg)




#====
# Version Filtering
#==== 


def onlyVersion(records, version):
 filterRecords = {}
 for l in records:
  filterRecords[l] = []
  for r in records[l]:
   if 'clientVersion' in r:
    if r['clientVersion'] == version:
     filterRecords[l].append(r)
 return filterRecords


def atLeastVersion(records, release=0, major=0, minor=0, build=0):
 raise(NotImplementedError, 'oh noes, the sky is fallingz')


def upToVersion():
 raise(NotImplementedError, 'SHITSHITSHIT')


#====
#  Time filtering
#====

# These are largely sfor LISTS, not dicts...get what you want in a list first then use these for time series analysis

'''

timeList = time.ctime(test[1]['timestamp']).replace('  ', ' ').split(' ')
timeList[:3] + [i for i in timeList[3].split(':')] + timeList[4:]

  >> ['Thu', 'Sep', '4', '03', '14', '00', '2014']

0 = Day of week
1 = Month
2 = Day
3 = Hour
4 = Minute
5 = Second
6 = Year

'''

import time
import calendar

months = [i[1] for i in enumerate(calendar.month_abbr)]

def timeSegments(record):
 timeList = time.ctime(record['timestamp']).replace('  ', ' ').split(' ')
 return timeList[:1] + [months.index(timeList[1])] + [int(timeList[2])]+ [int(i) for i in timeList[3].split(':')] + [int(timeList[4])]

# Returns a dict in the form ["<int month>/<int year>"]["<int day>"], where each <int day> key is a list of records
# Expects a list!
def groupByDay(records):
 filteredRecords = {}
 cleanRecords = [i for i in records if 'timestamp' in i]

 if len(cleanRecords) is 0:
  return
 print(map(timeSegments, cleanRecords))
 activeYears = set(i[6] for i in map(timeSegments, cleanRecords))

 for year in activeYears:
  filteredRecords[year] = {}
  for i in range(1,13):
   filteredRecords[year][i] = {}
   daysInMonth = calendar.monthrange(int(year), i)[1]
   for j in range(1, daysInMonth + 1):
    filteredRecords[year][i][j] = []
 
 for r in cleanRecords:
  info = timeSegments(r)
  filteredRecords[info[6]][info[1]][info[2]].append(r)
 
 return filteredRecords 

def groupByHour(records):
 filteredRecords = {}
 cleanRecords = [i for i in records if 'timestamp' in i]

 if len(cleanRecords) is 0:
  return

 activeYears = set(i[6] for i in map(timeSegments, cleanRecords))

 for year in activeYears:
  filteredRecords[year] = {}
  for i in range(1,13):
   filteredRecords[year][i] = {}
   daysInMonth = calendar.monthrange(int(year), i)[1]
   for j in range(1, daysInMonth + 1):
    filteredRecords[year][i][j] = {}
    for k in range(0,25):
     filteredRecords[year][i][j][k] = []

 for r in cleanRecords:
  info = timeSegments(r)
  filteredRecords[info[6]][info[1]][info[2]][info[3]].append(r)
 
 return filteredRecords

def filterByDayForMonth(records, month, year):
 raise(NotImplementedError, 'pls')
 
def filterByHourForDay(records, day, month, year):
 raise(NotImplementedError, 'pls')

def filterByMinuteForHour(records, hour, day, month, year):
 raise(NotImplementedError, 'pls')




#====
#  ID filtering
#====

'''

t = filter(lambda x, y='510D227E-FA74-4DC8-B1B5-F5653409E81D': x['anonymousId'] == y, test['locationInteraction'])

'''

#Expects dict
#returns a list
def getAllAnonymousIds(records, eventFilter=[]):
 if len(eventFilter) is not 0:
  raise(NotImplementedError, 'event type filtering options not available')

 aggregateIds = []

 for event in records:
  aggregateIds += set([i['anonymousId'] for i in records[event]])
 
 return set(aggregateIds)
  

#Expects a dict
#Returns a list
def filterByAnonymousId(records, playerId, timeSort=True, eventFilter=[]):
 aggregateRecords = [] 

 #If an event filter exists, check against it, else include everything
 #This can be done better
 if len(eventFilter) is not 0:
  for event in records:
   if event in eventFilter:
    aggregateRecords += filter(lambda x,y=playerId: x['anonymousId'] == y, records[event])
 else: 
  for event in records:
   aggregateRecords += filter(lambda x,y=playerId: x['anonymousId'] == y, records[event])
 
 if timeSort:
  aggregateRecords = sorted(aggregateRecords, key=lambda x: x['timestamp'])
 
 return aggregateRecords


#Consider including filtering by event type
def groupByAnonymousId(records, timeSort=True, eventFilter=[]):
 playerIds = getAllAnonymousIds(records)
 playerIdGroups = {} 

 for playerId in playerIds:
  playerIdGroups[playerId] = []
 
 #This can be done better
 if len(eventFilter) is not 0:
  for event in records:
   if event in eventFilter:
    for record in records[event]:
     if 'anonymousId' in record:
      playerIdGroups[record['anonymousId']].append(record)
 else:
  for event in records:
   for record in records[event]:
    if 'anonymousId' in record:
     playerIdGroups[record['anonymousId']].append(record)
 
 if timeSort:
  for player in playerIdGroups:
   playerIdGroups[player] = sorted(playerIdGroups[player], key=lambda x: x['timestamp'])

 return playerIdGroups
