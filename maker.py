#file containing functions that make other files
import csv

#Creates the player character file as a .csv
def playerWriter(name, silver, food, agil, pres, stre, toug):
	fileName = name + '.csv'
	with open(fileName, 'w', newline = '') as csvfile:
		fieldnames = ['Name', 'Silver', 'Food', 'Agility', 'Presence', 'Strength', 'Toughness']
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		writer.writerow({'Name': name, 'Silver': silver, 'Food': food, 'Agility': agil, 'Presence': pres, 'Strength': stre, 'Toughness': toug})
	#with open('playernames.csv', 'w', newline = '') as csvfile:
	#	listWriter = csv.Writer(csvfile)
	return

def invWriter(item):
	with open('testplayerInv.csv', 'w', newline = '') as csvfile:
		fieldnames = ['Item']
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		writer.writerow({'item': item})
	return