from sys import argv

script,first, second, third = argv

print "The script is called ", script
print "your first variable is ", first
print "your third variable is ", third
print "your second variable is ", second
print "Provide your name here to complete the program : ",
name = raw_input()
print "Thank you %s !" %name
