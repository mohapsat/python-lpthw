class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print '-' * 10
			print line

happy_bday = Song(["Happy bday to you","This is la la","Thank you song for you"])

bulls_on_a_parade = Song(["You da bull", "go on a parade", "dont call again"])

#for i in happy_bday.lyrics:
#	print i

happy_bday.sing_me_a_song()

bulls_on_a_parade.sing_me_a_song()

