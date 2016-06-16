intlist = [1,2,3,4]
charlist = ['a','b','c','d']
mixed = [1,2,3,'a','b','c']


#for i in intlist:
#	print "i = %d" %i

#for j in mixed:
#	print "%r" %j

elements = []

for i in range(10,15):
	elements.append(i)

elements.reverse()
#print "%d" % elements.index(lenght)

for i in elements:
	print "value  %d" %i

i = 0
meList = []
while i < 6:
	meList.append(i)
	i+=1

for i in meList:
	print "%d" %i	

print "%d" %elements[0];
print "%d" %meList[1];
