from sys import argv

script, filename = argv

print "we are going to erace %r" % filename
print "If you don't want that, hit CTRL + C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "opening the file...."
# 'w' To write to the file, will erase the existing data first
target = open(filename,'w')
#target = open(filename,'a') # 'a' To Append to the file

#print "Truncating the file"
#target.truncate()

print "Going to write next three lines"
line1 = raw_input("Line 1")
line2 = raw_input("Line 2")
line3 = raw_input("Line 3")


print "Writing ...."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Finally, close the file."
target.close()
