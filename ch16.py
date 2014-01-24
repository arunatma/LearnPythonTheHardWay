print "Chapter 16 - Reading and Writing Files"

# open - opens a file for operations (read / write) - default is read
# close - closes the file handle
# read - reads the entire contents of the file
# readline - reads a single line
# truncate - deletes the entire content of the file referenced by the filehandle
# write("...") - writes the quoted string into the given file handle 

# 'sys' is the module from which just 'argv' class is imported
from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you are okay with the erasing, hit ENTER"

raw_input("?")

# w for write, r for read and a for append
# Also there is w+, r+ and a+ to open in both read and write mode
print "Opening the file... (with write access)"
# Opening in write mode itself, would truncated the file
# target.truncate() is just redundant
target = open(filename, 'w')

print "Truncating the file."
target.truncate()
print "The file is now truncated - Contents Erased!"

print "Okay, let us write some new lines into the file."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "These three lines are to be written to %r" % filename

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# The following is another way of writing the same contents 
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# Okay, that was with concatenation, now this is with string formatting
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "Final Step: Close the file!"
target.close()

# Execute the script from the command line.  This script takes in 1 argument

