cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenegers_per_car = passengers / cars_driven

print "There are ", cars , " cars available."
print "There are only", drivers , " drivers available."
print "There will be ", cars_not_driven , " empty cars today."
print "We can transport ", carpool_capacity , " people today."
print "We have " , passengers , " to carpool today."
print "We need to put about ", average_passenegers_per_car , " in each car"

my_name = "Binu"
my_aga = 36
my_height = 5.7
my_weight = 88
my_eyes = "Black"
my_teeth = "White"
my_hair = "Black"

print "Let's talk about %s." % my_name
print "He's %r feet tall" % my_height
print "He's %i kilo heavy" % my_weight
print "He's got %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth is %s usually" % my_teeth

print "If I add %d, %d and %d I get %d" % (my_aga, my_height, my_weight, my_aga + my_height + my_weight)
