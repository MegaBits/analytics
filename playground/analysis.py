
import munging


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


# Overworld interactions per DATE_1 to DATE_2


# Mean and stddev overworld interaction from DATE_1 to DATE_2


# Mean play radius from DATE_1 to DATE_2 per player[] 
