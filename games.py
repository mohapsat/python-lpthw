#!/usr/bin/python

class Games(object):	
	def __init__(self):
		self.name = "game name"
		self.genre = "game genre"
	def timesplayed(self, days, hours):
		print days*hours

fc4 = Games()
fc4.timesplayed(5,6)
list_games = ["Far Cry 4", "Far Cry Primal"]

for i in list_games:
	fc4.name = i
	print fc4.name 

