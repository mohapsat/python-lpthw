states = {
	'Oregon': 'OR',
	'Florida':'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI'
}

cities = {
	'CA':'San Fran',
	'MI':'Detroit',
	'FL':'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '_' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print '_' * 10
print "Michigan\'s abbreviation is: ", states['Michigan']
print "Florida\'s abbreviation is: ", states['Florida']

# print every state's abbv
print '_' * 10
for state, abbv in states.items():
	 print "For State: %s, abbv is %s " %(state, abbv)

# print every city in each state

print '_' * 10
for city, state in cities.items():
	print "City: %s, State: %s" %(state, city)

print '_' * 10
for state, abbv in states.items():
	print "State: %s, Abbv: %s, City: %s" %(state, abbv, cities[abbv])

state = states.get('California')

if not state:
	print "Sorry, Texas is not on the list"
else:
	print "Yay!, %s is on the list" %state	

