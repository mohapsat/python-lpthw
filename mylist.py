ten_things = ["ball","bar","cat","nes","xbox"]

print "%s" %ten_things[0]

more_stuff = ["ps2","ps3","ps4","soc","rot","wre","qaw","pot","erd"]

#for i in ten_things:
#	print ten_things[i]

while len(ten_things) != 10:
	tmp = more_stuff.pop()
	print "Adding: :", tmp
	ten_things.append(tmp)
	print "there are %d items now" %len(ten_things)

print ten_things
print ten_things[1]
print ten_things[-1]
print more_stuff.pop()
print '$'.join(more_stuff)
