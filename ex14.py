from sys import argv

script,user_name = argv
prompt = '------>'

print "Hi %s, I'm the %s script." % (user_name,script)
print "I would like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
live = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about like me.
You live in %r.
You have a %r computer.
""" % (likes,live,computer)
