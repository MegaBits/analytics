
# Preproccessing all the combinations of _moves

# Needed: for every, for every type, craft a table 
# number of tables = number of _moves * number of types
# each table is needs to be [-5 to 5] by [-5 to 5]


import csv
import json



def getMoveByUUID(uuid):
	return _moves[uuid]

def getMoves():
	return _moves


sheetFile = './csv/MBDMove.csv'

_moves = {}

r = open(sheetFile, 'r')
reader = csv.reader(r)
headers = next(reader, None)
sheet = [row for row in reader]



for row in sheet:

	'''
	0 name
	1 uuid
	2 damageRate
	3 elementalType
	4 energyCost
	5 hitRate
	6 minHitCount
	7 maxHitCount
	8 mediaName
	9 Defender
	10 defenderDeferredConditions
	11 defenderImmediateConditions
	12 Attacker
	13 attackerDeferredConditions
	14 attackerImmediateConditions
	15 summary
	'''
	_moves[row[1]] = {}
	_moves[row[1]][headers[0]] = row[0]
	_moves[row[1]][headers[2]] = row[2]
	_moves[row[1]][headers[3]] = row[3]
	_moves[row[1]][headers[4]] = row[4]
	_moves[row[1]][headers[5]] = row[5]
	_moves[row[1]][headers[6]] = row[6]
	_moves[row[1]][headers[7]] = row[7]
	_moves[row[1]][headers[10]] = {} if '' == row[10] else json.loads(row[10])
	_moves[row[1]][headers[11]] = {} if '' == row[11] else json.loads(row[11])
	_moves[row[1]][headers[13]] = {} if '' == row[13] else json.loads(row[13])
	_moves[row[1]][headers[14]] = {} if '' == row[14] else json.loads(row[14])
