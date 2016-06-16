from sys import argv

def fn_readF(f):
	var = open(f)
	print var.read()	

def fn_truncF(f):
	f.truncate()

def fn_rewindF(f):
	f.seek(0)


print "Enter file:"
in_f = raw_input("> ")

fn_readF(in_f)

