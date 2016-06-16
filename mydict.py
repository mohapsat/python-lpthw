games = {
	'Adventure':'FC4',
	'Stealth':'FC1',
	'Fantasy':'FC2'

}

cost = {
	'FC1':10,
	'FC2':20,
	'FC3':30,
	'FC4':40
}

print games['Adventure']
print cost['FC2']

for genre, game in games.items():
	print "%s is an %s game" %(game, genre)

for genre, game in games.items():
	print "%s is an %s game and costs %d" %(game, genre, cost[game])
