print "Learn Python The Hard Way by Zed A. Shaw"
print "Chapter 06 - Strings and Text"

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

# It is observed that %r is same as '%s' (see single quotes)
# In this and previous chapter, %s, %d, %f, %r are discussed!
print "I said: %r." % x
print "I also said '%s'." % y

hilarious = False  # This is a boolean value that got assigned
joke_evaluation = "Isn't that joke so funny?! %r"

# This looks like a modulo division (finding reminder), but it is not!!
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e #Concatenation here!

dummy_variable = raw_input("Press Enter to Quit!")
