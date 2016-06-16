class MyNewStuff(object):
	
	def __init__(self):
		self.tangerines = "this is a var"

	def apples(self):
		print "take some apples"



class OpenWorldSim(object):
	
	def __init__(self):
		self.gameplay = "Awesome"
		self.graphics = 10
		self.story = "Long"
		self.hours = 4

	def timePlayedInMin(self):
		return self.hours * 60 


thing = MyNewStuff()
thing.apples()
print thing.tangerines

fc4 = OpenWorldSim()
print "Gameplay = %s" %fc4.gameplay
fc4.graphics = 9
print "Story = %s" %fc4.story
print "Time Played in Min = %d" %fc4.timePlayedInMin()
print "Graphics = %s" %fc4.graphics
