
directions = ['north', 'south', 'east', 'west', 'down', 'up', 'down', 'right']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'at', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']
#numbers =['3','1234']

def scan(thewords):
	
	thewords = thewords.split()
	sentence = []
	
	
	for i in thewords:
		
		if i in directions:
			sentence.append(('direction',i))
		elif i in verbs:
			sentence.append(('verb',i))
		elif i in stops:
			sentence.append(('stop',i))
		elif i in nouns:
			sentence.append(('noun',i))
		elif i in isdigit():
			sentence.append(('number',convert_number(i)))
		else:
			sentence.append(('error',i))

	return sentence
#	print sentence

#scan("3 91234")
#scan("princess stop this bear")
#scan("this is so north west of the eat to kill the bear princess")

def convert_number(s):
	try:
		return int(s)
	except ValueErrors:
		return None

		
		
