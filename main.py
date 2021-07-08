#Main file

#imported .pys
import character

#never ending loop
while True:
	reply = input('[N]ew or [R]eturning character?')
	if reply == 'stop' : break
	elif reply == 'N'or'n':
		character.characterMaker()
	elif reply == 'R'or'r':
		#load character somehow
		print('TODO: load character somehow')
	else:
		print('Bad Input, Try again')

	reply = input('Yeah I havent gotten this far yet...')

	print('')