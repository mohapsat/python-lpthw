from sys import argv
script = argv

print "File to open?"

fl = raw_input("> ")
fopn = open(fl,'r+')

#fopn.write("\n#This is a comment" )

print fopn.read()


fopn.close()
