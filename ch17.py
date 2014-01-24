print "Chapter 17 - More Files"


from sys import argv
from os.path import exists

# This script takes in two arguments, one for the source and another for dest.
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too!!
in_file = open(from_file)
in_data = in_file.read()

print "The input file is %d bytes long" % len(in_data)

print "Does the output file %s exist? %r" % (to_file, exists(to_file))
print "Ready, hit ENTER to continue, ^C to abort."
raw_input()		# dummy input for getting command from user

out_file = open(to_file, 'w')
out_file.write(in_data)		# Write the contents of in_file to out_file


print "Task Accomplished!"
print "Copied the contents from %s to %s" % (from_file, to_file)

out_file.close()
in_file.close()