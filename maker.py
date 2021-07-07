#file containing functions that make other files

import csv

def playerWriter(name, silver, food, agil, pres, stre, toug):
	with open('testplayer.csv', "w") as csvfile:
		fieldnames = ['Name', 'Silver', 'Food', 'Agility', 'Presence', 'Strength', 'Toughness']
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		writer.writerow({'Name': name, 'Silver': silver, 'Food': food, 'Agility': agil, 'Presence': pres, 'Strength': stre, 'Toughness': toug})
	return

def invWriter(item):
	with open('testplayerInv.csv', "w") as csvfile:
		fieldnames = ['Item']
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		writer.writerow({'item': item})
	return