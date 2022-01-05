#Main file

#imported .pys
import character

charLoaded = 0

#character creation/loading loop
while charLoaded == 0:
	reply = input('[N]ew or [R]eturning character?')
	if reply == 'stop' : break
	elif reply.lower() == 'n':
		character.characterMaker()
		charLoaded = character.characterMaker()
	elif reply.lower() == 'r':
		#load character somehow
		print('TODO: load character somehow')
		charLoaded = 1
	else:
		print('Bad Input, Try again')

reply = input('Yeah I havent gotten this far yet...')

print('')