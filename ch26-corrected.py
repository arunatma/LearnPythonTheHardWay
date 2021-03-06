# Need to import the module, before using the functions within
import ch25

print "Chapter 26 - Congratulations, Take a Test"

# The objective is to find bugs and fix the broken code below
# ch26-given.py contains the original script
# ch26-corrected.py (this file) contains the error corrected script

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# Missed the colon for function definition. Fixed	
def print_first_word(words):
    """Prints the first word after popping it off."""
	# words.pop, and not words.poop
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
	# Missed a closing parenthesis in the below line
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

# Subtract 6 to get five
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
	# Forward slash for division
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# Single Equal symbol for assignment. No hyphen in variable names
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
# Crates - spelling, and start_point variable spelling, closing parenthesis
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

# good and not god; Wait and not weight
sentence = "All good things come to those who wait."

words = ch25.break_words(sentence)
sorted_words = ch25.sort_words(words)

print_first_word(words)
print_last_word(words)
# Remove the leading dot
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ch25.sort_sentence(sentence)
# 't' missing in print
print sorted_words

# Function call being misspelt, and needs to be called with module
ch25.print_first_and_last(sentence)
# No initial tab, should start at the line beginning; 'sentence' name misspelt
ch25.print_first_and_last_sorted(sentence)
