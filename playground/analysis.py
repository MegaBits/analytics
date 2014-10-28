from __future__ import division
import munging
import math
import time
import datetime

# User acquisition (new users from before DATE_1 up until DATE_2)

''' 
Ok, so we need a decent way to communicate dates...so I'm going to do it like this for now:

 dates are lists -> date[] = [day, month, year]
'''

   # records should be all records, we'll take their set() 
def userAcquisition(records, startDate, endDate):

 priorRecords = filter(lambda x: munging.isPriorToDate(x, startDate), records)
 priorIds = set([i['anonymousId'] for i in priorRecords if 'anonymousId' in i]) 

 currentRecords = filter(lambda x: munging.isBetweenDates(x, startDate, endDate), records) 
 currentIds = set([i['anonymousId'] for i in currentRecords if 'anonymousId' in i])
 
 return len(currentIds - priorIds)
 
 

# User retention (users from DATE_1 to DATE_2 that also existed before DATE_1)
  # So, [startDate, splitDate) is the origin set, [splitDate, endDate) is the comparison set
  # since isBetweenDates is endDate exclusive, the passed date should be one day greater than the actual last day you want to capture 
def userRetention(records, startDate, splitDate, endDate):
  originSet = set([i['anonymousId'] for i in filter(lambda x: munging.isBetweenDates(x, startDate, splitDate), records) if 'anonymousId' in i])
   
  comparisonSet = set([i['anonymousId'] for i in filter(lambda x: munging.isBetweenDates(x, splitDate, endDate), records) if 'anonymousId' in i])

  return (len(comparisonSet) - len(comparisonSet - originSet)) / len(originSet)


# Mean and stddev overworld interaction from DATE_1 to DATE_2
def meanOverworldInteractionsPerDay(records, startDate, endDate):
  focusSet = [i for i in filter(lambda x: munging.isBetweenDates(x, startDate, endDate), records) if 'anonymousId' in i and 'event' in i]
  filteredFocusSet = filter(lambda x: x['event'] == 'locationInteraction', focusSet)
  timeSortedSet = munging.groupByDay(filteredFocusSet)

  totalsByDay = [] 

  for y in timeSortedSet:
   for m in timeSortedSet[y]:
    for d in timeSortedSet[y][m]:
      # isBetweenDate will fill in days for any included months, so we need to prune the days in the dict that shouldn't be included
      if munging.isBetweenDates({'timestamp':time.mktime(datetime.datetime.strptime('/'.join([str(i) for i in [d,m,y]]), "%d/%m/%Y").timetuple())}, startDate, endDate):
        totalsByDay.append(len(timeSortedSet[y][m][d]))

  print(totalsByDay)
  mean = sum(totalsByDay)/len(totalsByDay)
  sqMeanDiffs = [math.pow(float(i) - mean, 2) for i in totalsByDay]
  stdev = math.sqrt(sum(sqMeanDiffs)/len(sqMeanDiffs))
  return (mean, stdev)

def meanOverworldInteractionsPerHour(records, startDate, endDate):
  raise(NotImplementedError, 'sorry :(') 


# Mean play radius from DATE_1 to DATE_2 per player[]

 
