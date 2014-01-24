print "Learn Python the Hard way by Zed A. Shaw"
print "Chapter 10 - What was that?"

# Same print statement using single and double quotes
print "I am 5'11\" tall!"
# Escape the single quote inside single quote and double inside double
print 'I am 5\'11" tall!'

tabby_cat = "\tI'm tabbed in."  # Print with a tab at the beginning
persian_cat = "I'm split\non a line." #Introducing new line character \n
backslash_cat = "I'm \\ a \\ cat"  # Hey, there needs to be a way to print '\'!

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Sound a bell 10 times
for i in range(1, 10):
    print "\a\r"

dummy_var = raw_input("Press Enter to Continue printing Rotating Lines")

# Rotating Lines Code
while True:
    for i in ['/', '-', '|', '\\', '-', '|']:
        print "%s\r" %i,

# Code flow never comes here
dummy_var = raw_input("Press Enter to Quit")

