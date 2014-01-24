print "Learn Python the Hard Way by Zed A. Shaw"
print "Chapter 5 - More variables and printing"

my_name = "Arunram A"
my_city = "Bangalore"
my_state = "Karnataka"
my_sport = "Cricket"

# This is how a format string is written, note that there is no comma
print "Let's talk about %s" % my_name

# If more than one variables are to be used, put all in a list and pass on
print "%s lives in %s" % (my_name, my_city)
print "%s knows that %s is the capital of %s" % (my_name, my_city, my_state)

area_code 	= 91
tsp_code  	= 9443  	# Telecom provider id
sub_num		= 123456	# Subscriber id

print "Combining Area Code %s, Telecom Service Provider Code %s and Subscriber \
	Number %s, the mobile number is %s" % (area_code, tsp_code, sub_num, 
	area_code + tsp_code + sub_num)
	
print "Oh! I got that wrong. I needed to have concatenated the strings"

print "Combining Area Code %s, Telecom Service Provider Code %s and Subscriber \
	Number %s, the mobile number is %s" % (area_code, tsp_code, sub_num, 
	str(area_code) + str(tsp_code) + str(sub_num))	

# Note below the %d formatter instead of %s - %d for Numbers %s strings	
print "The scores in SA-Ind first Test Match at Johannesburg Nov 2013 are %d \
	and %d" % (280, 244)
	
# Use %f formatter for floating point numbers
pi = 3.141593
print "Pi with value %.4f when rounded to three digits become %.3f" %(pi, pi)
	
dummy_variable = raw_input("Enter to Quit")