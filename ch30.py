print "Chapter 30: Else and If"

people = 50
cars = 40
buses = 40

# Single elif
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide!"

# Multiple elif	
if buses > cars:
	print "There are too many buses."
elif buses < cars:
	print "There are more cars than buses."
elif people > buses:
	print "The second elif"
else:
	print "We still can't decide."
	
if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."
	