#Main file

#imported .pys
import character, maker

#never ending loop
while True:
	reply = input('Welcome to the end of the world! Please enter your name: ')
	if reply == 'stop' : break																									
	elif not reply.isascii():
		print('Bad Input, Try again')
	else:
		name = character.Name(reply)

	silver = character.startCash()
	food = character.startFood()
	#debug print
	print('your name is ', name,'and you have ', silver, ' silver', ' You also have a waterskin and ', food, ' days of food.')

	abil = character.Abilities()
	#debug print 2
	print('your Agility is: ', abil[0], 'your Presence is: ', abil[1], 'your Strength is: ', abil[2], 'your Toughness is: ', abil[3])

	maker.playerWriter(name, silver, food, abil[0], abil[1], abil[2], abil[3])

	print('')