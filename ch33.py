print "Chapter 33 - While Loops"

def looped_counter(max_num, incr_step = 1):
	i = 0
	numbers = []

	while i < max_num:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i = i + incr_step
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		
	return numbers

up_limit = 7 #int(raw_input("Input a Number: "))
	
# Function Call to create the list	
nums = looped_counter(up_limit)

# Increment each number by 2
nums_2 = looped_counter(up_limit, 2)
	
print "The numbers: "

for num in nums:
	print num
	
print "The numbers (nums_2): "
	
for num in nums_2:
	print num	