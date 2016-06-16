print "this is cool"
print "this is \"the colest\" thing to \'say\'"

print "-_" * 50
print "Hello"
print "-_" * 50

five = 10 - 2 + 3 - 6
print "Five = %d" % five

def fn(arg):
	x=10;y=20;z=30
	x=x/int(arg)
	y+=int(arg)
	z+=int(arg)
	print "%d,%d,%d" %(x,y,z)

fn(10)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


beans, jars, crates = secret_formula(100)
#beans = secret_formula(1000)
#jars = secret_formula(1000)
#crates = secret_formula(1000)

#print "With a starting point of: %d" % start_point
#print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

print "We'd have %d beans." % (beans)

#start_point = start_point / 10

#print "We can also do that this way:"
#print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))
