from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copy from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "does the output file exists? %r" % exists(to_file)
print "Ready, hit return to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, "a")
out_file.write(indata)

print "Completed!"

out_file.close()
in_file.close()
