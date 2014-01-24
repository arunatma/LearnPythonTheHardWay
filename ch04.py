print "Handwritten by Arunram A"
print "Handwrite - Do not copy paste, is the most important rule of the book"

print "In case of trouble, read the code backwards, from last to first, one by one"
print "Reading code backwards helps in identifying potential problems"

print "Chapter 4 - Variables and Names"

distance	= 45		# km
time		= 30.0		# min
speed		= distance / time
print "The Speed is ", speed, "km/minute"

print "Okay, Now Equation of Motion"
u	= 0		# freefall; starting velocity is zero
t	= 10	# 10 seconds for a downfall
a	= 9.8	# acceleration due to gravity = 9.8 m/s2
s	= u * t + 1.0/2 * a * t * t
print "The height at which the object is left for a free fall is", s, "meter"

height = s
# The same statement as above using %s symbol for formatting
print "The height at which the object is left for a free fall is %s meter" % height

dummy_variable = raw_input("Press Enter Key to Quit")
