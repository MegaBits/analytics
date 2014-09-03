
# Preproccessing all the combinations of _moves

# Needed: for every, for every type, craft a table 
# number of tables = number of _moves * number of types
# each table is needs to be [-5 to 5] by [-5 to 5]

import csv
import json


def getMonsterByName(name):
	for key in _monsters.keys():
		if _monsters[key]['name'] == name:
			return (key, _monsters[key])

def getMonsterNameByUUID(uuid):
	return _monsters[uuid]['name']

def getMonsterByUUID(uuid):
	return _monsters[uuid]

def getMonsters():
	return _monsters

_monsters = {}


r = open('./csv/MBDMonster.csv', 'r')
reader = csv.reader(r)
headers = next(reader, None)
dummy = next(reader, None)
sheet = [row for row in reader]


for row in sheet:
	
	'''
	0 name
	1 uuid
	2 baseAttack
	3 baseDefense
	4 baseAccuracy
	5 baseSpeed
	6 baseCritRate
	7 baseEnergy
	8 baseHealth
	9 diurnalityType
	10 elementalSubtype
	11 elementalType
	12 encyclopediaIndex
	13 mediaName
	14 movementType
	15 rarityType
	16 region
	17 spriteSize
	18 summary
	19 evolvesFrom
	20 learnableMoves
	21 possibleDefaultMoves
	22 possibleAbilities
	23 baseMove
	'''

	_monsters[row[1]] = {}
	_monsters[row[1]][headers[0]] = row[0]
	_monsters[row[1]][headers[2]] = row[2]
	_monsters[row[1]][headers[3]] = row[3]
	_monsters[row[1]][headers[4]] = row[4]
	_monsters[row[1]][headers[5]] = row[5]
	_monsters[row[1]][headers[6]] = row[6]
	_monsters[row[1]][headers[7]] = row[7]
	_monsters[row[1]][headers[8]] = row[8]
	_monsters[row[1]][headers[10]] = row[10]
	_monsters[row[1]][headers[11]] = row[11]
	_monsters[row[1]][headers[20]] = json.loads(row[20])
	_monsters[row[1]][headers[23]] = row[23]