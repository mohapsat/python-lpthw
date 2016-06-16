#!/usr/bin/python

########## Class hierarchy lvl 1
#Map
#Engine
#Scene
#	Death
#	Central Corridor
#	Laser Weapon Armory
#	The Bridge
#	Escape Pod

########### Class hierarchy pass 2

#Map
#	- next_scene
#	- opening_scene
#Engine
#	- play
#Scene
#	- enter
#	Death
#	Central Corridor
#	Laser Weapon Armory
#	The Bridge
#	Escape Pod

class Scene(object):
	
	def enter(self):
		pass

class Engine(object):
	
	def __init__(self, scene_map):
		pass
	
	def play(self):
		pass

class Death(Scene):
	 def enter(self):
		pass

class CentralCorridor(Scene):

	def enter(self):
		pass

class LaserWeaponArmory(Scene):
	
	def enter(self):
		pass

class TheBridge(Scene):
	
	def enter(self):
		pass

class EscapePod(Scene):
	
	def enter(self):
		pass


class Map(object):
	
	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass

a_map = Map('Central Corridor')
a_game = Engine(a_map)
a_game.play()
