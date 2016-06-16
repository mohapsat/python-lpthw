from sys import argv

print "Enter two vals"
x=int(raw_input("> "))
y=int(raw_input("> "))

def sumz(x,y):
	return x+y

def diffz(x,y):
	return x-y


print "values entered x = %d , y = %d " % (x,y)
print "sum of x(%d) and y(%d) is %d" %(x,y,sumz(x,y))
print "diff of x(%d) and y(%d) is %d" %(x,y,diffz(x,y))
print "crazy output is %d" % sumz(sumz(x,y),diffz(x,y))


