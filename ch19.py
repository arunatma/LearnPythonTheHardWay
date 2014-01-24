print "Chapter 19 - Functions and Variables"

# This script is just to differentiate the scope of the variables

def cats_and_rats(cats_count, rats_count):
	print "There are %d cats!" % cats_count
	print "There are %d rats!" % rats_count
	print "So much of cats and rats!"
	
def calc_cats():
	return 30	

print "The numeric arguments to the function can be passed on directly"
cats_and_rats(20, 40)  # This is a function call!

print "Or, can be passed via variables"

cats_count = 20  # This var. is different from cats_count inside cats_and_rats
rats_count = 40

cats_and_rats(cats_count, rats_count)

print "Math or other operations could be done on arguments!"
cats_and_rats(40 + 20, 30 - 10)

print "Function call (with return) can be done too in the place of argument"
# Python is interpreted language; so calc_cats() fn to be def. before the call
cats_and_rats(calc_cats(), 40)
	
print "Combining all three above: numeral + variable + fn_call"
cats_and_rats(cats_count + 10 + calc_cats(), 23)	