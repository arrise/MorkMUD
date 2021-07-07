#File containing character creation functions

import random

def Name(x):
	charName = x
	return charName

def startCash():
	charCash = (random.randint(2, 12) * 10)
	return charCash

def startFood():
	charFood = random.randint(1, 4)
	return charFood

def pack():
	charPackInt = random.randint(1, 6)
	
	if charPackInt < 2:
		charPack = 'nothing'
	elif charPackInt == 3:
		charPack = 'backpack'
	elif charPackInt == 4:
		charPack = 'sack'
	elif charPackInt == 5:
		charPack = 'small wagon'
	elif charPackInt == 6:
		charPack = 'donkey'

	return charPack

def items():
	charItemsInt = random.randint(1, 12)

	if charItemsInt == 1:
		charItems = '30 feet of rope'
	elif charItemsInt == 2:
		charItems = ''

	return charItems

#def Inventory():


def Abilities():
	i = 0
	skills = [0,0,0,0]
	while i < 4:
		skills[i] = random.randint(3, 18)
		i += 1
	return skills