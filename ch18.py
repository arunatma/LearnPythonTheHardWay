print "Chapter 18 - Names, Variables, Codes, Functions"

# this one is like scripts with argv
def print_two(*args):
	# The following command is very risky, it could cause error if more than
	# 2 arguments are given!
	# arg1, arg2 = args
	
	print "Total arguments = %s" % len(args)
	
	# For safety, check for number of arguments and pass on
	if (len(args) == 2):
		arg1, arg2 = args
	else:
		print "Number of arguments not compatible"
		return
	
	print "The code flow came here; Means only 2 arguments"
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# *args takes any number of arguments; we shall take only two
def print_only_two(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# This takes only one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	print "arg1: %r" % (arg1,)   # using tuples
	
# No arguments now
def print_none():
	print "I got nothing!"
	
print_two("arun", "ram")
print_two("here", "comes", "more than", "2 arguments")
print_only_two("arun", "ram")
print_one("Just one!")
print_none()
