print "Chapter 12 - Prompting people"

age = raw_input("What is your age?")
height = raw_input("What is your height?")

print "Your age is", age, "and your height is", height

print "Your age is %r and your height is %r" % (age, height)

raw_input("Press Enter to Quit")