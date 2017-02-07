from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_nextline(lNumber, f):
    print lNumber, f.readline()

def add(a, b):
    return a + b


current_file = open(input_file)

print "Let's print the whole file\n"
print_all(current_file)

print "Go back to begining"
rewind(current_file)

print "read the first line"
line_number = 1
print_nextline(line_number, current_file)

print "second line"
line_number += 1
print_nextline(line_number, current_file)

print "next line"
line_number += 1
print_nextline(line_number, current_file)

print "next line"
line_number += 1
print_nextline(line_number, current_file)

x = add(10,5)
print x
