
import parse2
import math
import time


#print parse.db

t1 = time.time()

eventTypes = set([record['event']['s'] for record in parse2.records])

t2 = time.time()

print(t2 - t1)

sortedRecords = {}
records = []

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
  records.append(parsedRecord)
t2 = time.time()

print(t2 - t1)


def sortRecords(recordList):
 sortedRec = {}
 events = set([record['event']['s'] for record in recordList])

 for event in set(events):
  sortedRec[event] = []

 for record in recordList:
  parsedRecord = {}
  for k in record.keys():
   if 's' in record[k]:
    parsedRecord[k] = record[k]['s']
   if 'n' in record[k]:
    if '.' in record[k]['n']:
     parsedRecord[k] = float(record[k]['n'])
    else:
     parsedRecord[k] = int(record[k]['n'])
  sortedRec[record['event']['s']].append(parsedRecord)
 
 return sortedRec
