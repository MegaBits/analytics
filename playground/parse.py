import os
import re
import ast
import time

db = []

f = open('./dynamo_archive_file', 'r')

t1 = time.time()

for line in f: 
  #hmm = repr(line)
  temp = [y for y in re.split('\\x02|\\x03|\\n', line) if y is not '']
  keyList = temp[::2]
  valueList = [ast.literal_eval(y) for y in temp[1::2]]
  record = {}
  for i in range(0, len(keyList)):
    record[keyList[i]] = valueList[i]
  db.append(record)

t2 = time.time()

print(t2-t1)


#for x in db:
#  print x
