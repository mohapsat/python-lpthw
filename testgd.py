#!/usr/bin/python
from sys import exit
from random import randint


# Engine class with play function
class Engine(object):
	
	def __init__(self, stage_map):
		self.stage_map = stage_map
		
	def play(self):
		current_stage = self.stage_map.opening_stage()
		last_stage = self.stage_map.next_stage('finished')

		while current_stage != last_stage:
			next_stage_name = current_stage.enter()
			current_stage = self.stage_map.next_stage(next_stage_name)
			
		current_stage.enter()
			

# stage parent class
class Stage(object):
	
	def enter(self):
		pass

# individual stages as subclasses
class MainCorridor(Stage):
	
	def enter(self):
#		pass
		print "You enter the main corridor"
		print "Guess combination to open airlock"
		secret = "%d%d%d" %(randint(0,9),randint(0,9),randint(0,9))
		guess = raw_input("[Keypad]> ")
		guesses=10
		count=0
		
		while count < guesses :
			count+=1
			guess = raw_input("[Keypad]> ")
			
		if guess == secret:
			print "Success! You exit the airlock"
			return 'finished'
		else:
			return 'death'	
		

class Death(Stage):

	quips = ["not cool", "boo"]

	def enter(self):
		print "You're a dead duck!!, %s" %Death.quips[randint(0,1)]
		exit(1)

class Finished(Stage):
	
	def enter(self):
		#pass
		print "You won!"

# Map class
class Map(object):

	stages = {
		'main_corridor': MainCorridor(),
		'death': Death(),
		'finished':Finished()
	}

	
	def __init__(self, start_stage):
		self.start_stage = start_stage
		#print "map is %s" %self.stage_map

	def next_stage(self, stage_name):
		val = Map.stages.get(stage_name)
		return val

	def opening_stage(self):
		return self.next_stage(self.start_stage)





#----------Main--------#

a_map = Map('main_corridor')

print "Value of a_map.start_stage = %s" %a_map.start_stage
#print "Value of a_map.next_stage = %s" %a_map.next_stage(a_map.start_stage)
#print "Value of a_map.opening_stage = %s" %a_map.opening_stage()

a_game = Engine(a_map)

a_game.play()

