print "Chapter 21 - Functions can return something"

def add(a, b):
	print "Addition of %d and %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "Subtract %d from %d i.e (%d - %d)" % (b, a, a, b)
	return a - b
	
def multiply(a, b):
	print "Multiplication: %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "Division: %d / %d" % (a, b)
	return a / b
	
print "Now, the fuction calls for the defined functions!"

sum = add(3, 4)
difference = subtract(6, 2)
product = multiply(3, 7)
quotient = divide(19, 8)

print "Sum: %d, Difference: %d, Product: %d, Quotient: %d" % (sum, difference,
	product, quotient)	# Going above 80 characters, so cutting it out
	
# Using all the functions together!
final_value = add(sum, subtract(difference, multiply(product, 
	divide(quotient, 2))))

print "The final value is: ", final_value

	