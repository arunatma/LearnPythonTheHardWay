print "Chapter 13 - Parameters, Unpacking, Variables"

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "The first variable is:", first
print "The second variable is:", second
print "The third variable is:", third

# To run in notepad++, Press Run and give the following 
# C:\Python27\python.exe "$(FULL_CURRENT_PATH)" arg1 arg2 ... argN 

raw_input("Press Enter to Quit")
