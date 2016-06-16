from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "this scene is not implemented yet, subclass and implement enter()"
		exit(1)


class Engine(object):
	
	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
		
		current_scene.enter()


class Death(Scene):
	
	quips = [
        "You died.  You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this."
	]

	def enter(self):
		print Death.quips[ randint( 0, len(self.quips) - 1 )]	
		exit(1)

class CentralCorridor(Scene):
	
	def enter(self):

	        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
	        print "your entire crew.  You are the last surviving member and your last"
	        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
	        print "put it in the bridge, and blow the ship up after getting into an "
	        print "escape pod."
	        print "\n"
	        print "You're running down the central corridor to the Weapons Armory when"
	        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
	        print "flowing around his hate filled body.  He's blocking the door to the"
        	print "Armory and about to pull a weapon to blast you."
		
		action = raw_input("> ")
		
		if action == "shoot!":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim.  Your laser hits his costume but misses him entirely.  This"
            		print "you are dead.  Then he eats you."
			return 'death'

		elif action == "dodge!":
                        print "Quick on the draw you yank out your blaster and fire it at the Gothon."
                        print "His clown costume is flowing and moving around his body, which throws"
                        print "off your aim.  Your laser hits his costume but misses him entirely.  This"
                        print "you are dead.  Then he eats you."
                        return 'death'

		elif action == "tell a joke!":
                        print "Quick on the draw you yank out your blaster and fire it at the Gothon."
                        print "His clown costume is flowing and moving around his body, which throws"
                        print "off your aim.  Your laser hits his costume but misses him entirely.  This"
                        print "you are dead.  Then he eats you."
                        return 'laser_weapon_armory'
		else:
			print "Does not compute"
			return 'central_corridor'


