from sys import argv

script,fl = argv

print "Opening file %r " %fl

fopn = open(fl)
print fopn.read()
fopn.close()
