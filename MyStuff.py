class MyStuff(object):
	
	def __init__(self):
		self.tangerine = "this is a class variable"

	def apple(self):
		print "love to learn this"

thing = MyStuff()
thing.apple()
print thing.tangerine
