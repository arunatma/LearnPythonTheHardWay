print "Chapter 15 - Reading Files"

# The name of the file to be read in is passed as program argument!

from sys import argv

# Read the command line arguments and store in different variables
script, filename = argv

# open the file specified by the variable 'filename'
txt = open(filename)

print "Here's your file %r:" % filename
# Read the contents of the file (in object 'txt') and print out
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

# Note that the same file can be opened again (b4 closing)! This is simply ok!
txt_again = open(file_again)

# To see what read does try this: 'c:\>python -m pydoc file | more'
print txt_again.read()

# Close the file handles
txt.close()
txt_again.close()

# Execute this script in command line.