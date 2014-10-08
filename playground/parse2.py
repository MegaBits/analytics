import os
import re
import ast
import time
import json


def craftRecordFromSegments(rawRecord):
  #print(rawRecord)
  segmentList = [y for y in re.split('\\x02|\\x03|\\n', rawRecord) if y is not '']
  keyList = segmentList[::2]
  #print temp
  #print([i.split('"') for i in segmentList[1::2]])
  temp = [i.split('"') for i in segmentList[1::2]]
  #for i in temp: print i[1] + ' ' + i[3]
  #print '******'
  #valueList = [json.loads(y) for y in segmentList[1::2]]
  valueList = [{i[1]:i[3]} for i in temp]
  record = {}
  for i in range(0, len(keyList)):
    record[keyList[i]] = valueList[i]
  return record



db = []

f = open('./dynamo_archive_file', 'r')

t1 = time.time()

rawRecords = []
recordSegments = []

for line in f: 
  #hmm = repr(line)
  #recordSegments.append([y for y in re.split('\\x02|\\x03|\\n', line) if y is not ''])
  rawRecords.append(line)

t2 = time.time()
print(t2-t1)


t1 = time.time()

records = map(craftRecordFromSegments, rawRecords)

t2 = time.time()

print(t2-t1)
#for record in records[:2]: print(record)







#for x in db:
#  print x
