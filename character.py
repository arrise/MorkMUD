#File containing character creation functions

import random, maker

#Builds basic character with money, food and ability scores
def characterMaker():
	reply = input('Welcome to the end of the world! Please enter your name: ')
	if not reply.isascii():
		print('Bad Input, Try again')
	else:
		abil = Abilities()
		name = reply
		silver = startCash()
		food = startFood()
		#Takes all the player's info and stores it in a .csv file
		maker.playerWriter(name, silver, food, abil[0], abil[1], abil[2], abil[3])

	#debug print
	print('your name is:', name,'and you have', silver, 'silver', 'You also have a waterskin and', food, 'days of food.')

	#debug print 2
	print('your Agility is:', abil[0], 'your Presence is:', abil[1], 'your Strength is:', abil[2], 'your Toughness is:', abil[3])
	
	return

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