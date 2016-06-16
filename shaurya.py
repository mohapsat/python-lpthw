from sys import argv

print "daddy, how many apples do you have?"
daddy = raw_input("> ")

print "Shaurya, how many apples do you have?"
shaurya = raw_input("> ")

mama = int(daddy) + int(shaurya)

print "_" * 50
print "Oh no! Mama took all your apples!!"
print "_" * 50

print "Mama has %d apples!" %mama
