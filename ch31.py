print "Chapter 31: Making Decisions"

print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake.  What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear does not give you the cake."
	elif bear == "2":
		print "The bear screams back at you"
	else:
		print "Well, doing %s is probably better.  Bear runs away." % bear
		
elif door == "2":
	print "You start into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello.  Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

else:
	print "Whatever. Does not really bother!"
	
print "All done, let us get to number range checking"

num_input = int(raw_input("Enter a number:> "))

if 0 <= num_input < 10:
	print "The number is between 0 and 9 (both inclusive)"
else:
	print "The number is outside the (0-9) range"
	
# The same if-else block could be written as below
# range(0, 10) produces a list of 10 numbers from 0 to 9
if num_input in range(0, 10):
	print "The number is between 0 and 9 (both inclusive)"
	