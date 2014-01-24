print "Learn Python the Hard Way by Zed A. Shaw"
print "Chapter 09 - Printing, Printing, Printing"

#Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days

# You do not need to give a space at the end of the string, as above
# Python automatically puts a space in.
print "Here are the months:", months

# Ok, now trying it out with the format string
print "Here are the months: %s" % months

# Raw formatting
print "Raw format print of the months: %r" % months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
Even with a 'single quote' or a "double quote" inside!!
"""

dummy_variable = raw_input("Press Enter to Quit.")