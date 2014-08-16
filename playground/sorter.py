
import parse



#print parse.db


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

