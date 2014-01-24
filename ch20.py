print "Chapter 20 - Functions and Files"

from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	rewind(f)
	i = 1
	while(i < line_count):
		f.readline()
		i = i + 1
	print line_count, f.readline()
	
# Open the input file
current_file = open(input_file)

print "The following are the whole contents of the file!"
print_all(current_file)

print "The file pointer has reached end; Bring it back to the start!"
rewind(current_file)

file_length = len(current_file.readlines())
# Again rewind!!
rewind(current_file)

print "We shall print a few lines"
print "There are totally %d lines in the file" % file_length

while(1):
	# Careful: Keyboard inputs are strings; Needed to be converted into integers
	line_to_print = int(raw_input("Which line do you need to print?"))
	print_a_line(line_to_print, current_file)
	further_option = raw_input("Proceed with further printing?")
	if(further_option != 'y' and further_option != 'Y'):
		break