
import parse2
import math
import time


#print parse.db

t1 = time.time()

eventTypes = set([record['event']['s'] for record in parse2.records])

t2 = time.time()

print(t2 - t1)

sortedRecords = {}


for event in set(eventTypes):
  sortedRecords[event] = []

t1 = time.time()

for record in parse2.records:
  parsedRecord = {}
  #print record
  for k in record.keys():
   if 's' in record[k]:
    parsedRecord[k] = record[k]['s']
   if 'n' in record[k]:
    if '.' in record[k]['n']:
     parsedRecord[k] = float(record[k]['n'])
    else:
     parsedRecord[k] = int(record[k]['n'])
  sortedRecords[record['event']['s']].append(parsedRecord)
  
t2 = time.time()

print(t2 - t1)



#for r in sortedRecords['locationInteraction']:
#  print r

#print(sortedRecords)

#if record['event']['s'] == 'locationInteraction':
    
##print set(eventTypes)

