print "Learn Python the Hard Way by Zed A. Shaw"
print "Chapter 07 - More Printing"

print "Mary had a little lamb"
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10  # This will print ten dots

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Watch that comma at the end.  Try removing it and see what happens!
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

# The comma at the end in the first print statement above will avoid newline!

dummy_variable = raw_input("Press Enter to Quit!")
