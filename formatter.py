from sys import argv


script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)









print "-" * 30
print "Script Name: ", argv[0]
print "-" * 30

# %r is for debugging
formatter = "%r %r %r %r"

demo = """this is a multi line text
lore ipsum dolor amet
l so msr assd erer asd
asd awrw sdolds sire sd
asdllkas srer fdlk df"""


print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True, False, True, False)
print formatter % (formatter,formatter,formatter,formatter)

print demo

#while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,

#print "what's your name?"
#name = raw_input("what's your name: ")
#print "what's your age?"
#age = int(raw_input("What's your age: "))

#print "Welcome, %s You were born %d years ago" % (name, age) 
#print "%s you will be 100 in %d years" % (name, 100-age)
