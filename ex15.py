from sys import argv

script, filename = argv

txt = open(filename)

print "Here is the file %s" % filename
print txt.read()


print "type the filename again:"
filename_again = raw_input("-->")

txt_again = open(filename_again)

print txt_again.read()
