from sys import argv
from os.path import exists

script, from_f, to_f = argv

print "Copying from %s to %s" % (from_f,to_f)
from_data = open(from_f).read()
#print from_data
print "the file %s is %d bytes long" % (from_f,len(from_data))

print "does the output file %s exist? %r" % (to_f,exists(to_f))

out_file = open(to_f,'w')

out_file.write(from_data)


out_file.close()
