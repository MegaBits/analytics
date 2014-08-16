import os
import re
import ast


db = []

f = open('./dynamo_archive_file', 'r')
for line in f: 
  #hmm = repr(line)
  temp = [y for y in re.split('\\x02|\\x03|\\n', line) if y is not '']
  keyList = temp[::2]
  valueList = [ast.literal_eval(y) for y in temp[1::2]]
  record = {}
  for i in range(0, len(keyList)):
    record[keyList[i]] = valueList[i]
  db.append(record)

#for x in db:
#  print x
