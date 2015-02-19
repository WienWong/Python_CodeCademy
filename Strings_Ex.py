
# Strings & Console Output

# Another useful data type is the string. A string can contain letters, numbers, and symbols.

# Create a new variable brian and assign it the string "Hello life!".
brian = "Hello life!"

# Set the following variables to their respective phrases:
caesar = "Graham"
praline = "John"
viking = "Teresa"
print caesar
print praline
print viking

# The string below is broken. Fix it using the escape backslash!
# 'This isn't flying, this is falling with style!' 
'This isn\'t flying, this is falling with style!' 

"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
# Assign the variable fifth_letter equal to the fifth letter of the string "MONTY".
# Remember that the fifth letter is not at index 5. Start counting your indices from zero.
fifth_letter = "MONTY"[4]
print fifth_letter
# Y

# String methods
parrot = "Norwegian Blue"
print len(parrot) 
# 14

# You can use the lower() method to get rid of all the capitalization in your strings. 
print parrot.lower()
# norwegian blue

# Now your string is 100% lower case! A similar method exists to make a string completely upper case.
print parrot.upper()
# NORWEGIAN BLUE

# The str() method turns non-strings into strings! 
pi = 3.14
print str(pi)

# Let's take a closer look at why you use len(string) and str(object), but dot notation 
# (such as "String".upper()) for the rest.
# Methods that use dot notation only work with strings. On the other hand, len() and str() can work on other data types.
ministry = "The Ministry of Silly Walks"
print len(ministry)
# 27
print ministry.upper()
# THE MINISTRY OF SILLY WALKS

# Printing Strings
print "Monty Python"

# Declare a variable called the_machine_goes and assign it the string value "Ping!"
the_machine_goes = "Ping!"
print the_machine_goes

# String Concatenation
# Print the concatenated strings "Spam ", "and ", "eggs"
print "Spam " + "and " + "eggs"
# Spam and eggs

# Explicit String Conversion
# The str() method converts non-strings into strings.
print "The value of pi is around " + str(3.14)

# String Formatting with %, Part 1
# The % operator after a string is used to combine a string with variables. The % operator will replace a %s 
# in the string with the string variable that comes after it.
string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)
# Let's not go to Camelot. 'Tis a silly place.

# String Formatting with %, Part 2
# Remember, we used the % operator to replace the %s placeholders with the variables in parentheses.
# You need the same number of %s terms in a string as the number of variables in parentheses:
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

