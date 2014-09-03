
# Preproccessing all the combinations of _conditions

# Needed: for every, for every type, craft a table 
# number of tables = number of _conditions * number of types
# each table is needs to be [-5 to 5] by [-5 to 5]


import csv
import json



def getConditionByUUID(uuid):
	return _conditions[uuid]

def getConditions():
	return _conditions


sheetFile = './csv/MBDCondition.csv'

_conditions = {}

r = open(sheetFile, 'r')
reader = csv.reader(r)
headers = next(reader, None)
sheet = [row for row in reader]


for row in sheet:

	'''
	0 category
	1 conditionName
	2 targetProperty
	3 hasVisual
	4 mediaName
	5 conditionVariables
	6 uuid
	7 elementalType
	8 initializedSummary
	9 finishedSummary
	10 canSwitch
	11 canMove
	12 immune
	'''
	_conditions[row[6]] = {}
	_conditions[row[6]][headers[0]] = row[0]
	_conditions[row[6]][headers[1]] = row[1]
	_conditions[row[6]][headers[2]] = row[2]
	_conditions[row[6]][headers[6]] = row[6]
	_conditions[row[6]][headers[7]] = row[7]
	_conditions[row[6]][headers[10]] = row[10]
	_conditions[row[6]][headers[11]] = row[11]
	_conditions[row[6]][headers[12]] = row[12]
