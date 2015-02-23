
# Example 1
def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %f" % bill
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With tip: %f" % bill
    return bill
    
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

# The header, which includes the def keyword, the name of the function, and any parameters the function requires. 
# Go ahead and create a function, spam, that prints the string "Eggs!" to the console. 
# Don't forget to include a comment of your own choosing. 
def spam():
    """Prints 'Eggs!' to the console."""
    print "Eggs!"

# Define the spam function above this line.
spam()

# Call and Response
# After defining a function, it must be called to be implemented.
# We've set up a function, square. Call it on the number 10
def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared
    
# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.

square(10)

# Parameters and Arguments
# Check out the function in the editor, power. It should take two arguments, a base and an exponent.
def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)  # Add your arguments here!

# Functions Calling Functions
# Change the body of deserves_another so that it always adds 2 to the output of one_good_turn.
def one_good_turn(n):
    return n + 1
    
def deserves_another(m):
    return one_good_turn(m) + 2
	
# Practice Makes Perfect
def cube(number):
    return number*number*number
    
def by_three(number):
    if number%3 == 0:
        return cube(number)
    else:
        return False
        
# Ask Python to print sqrt(25) on line 3.
import math
print math.sqrt(25)

# 
def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

# Set maximum to the max value of any set of numbers.

maximum = max(10, 11, 34, 43, 2)

print maximum

# Set minimum to the min value of any set of numbers.

minimum = min(10, 11, 34, 43, 2)

print minimum

# Set absolute equal to the absolute value of -42
absolute = abs(-42)

print absolute

# Print out the types of an integer, a float,
# and a string on separate lines below.

print type(10)
print type(10.1)
print type("10.1")
# <type 'int'>
# <type 'float'>
# <type 'str'>

# Review: Functions
def shut_down(s):
    if s=="yes":
        return "Shutting down"
    elif s=="no":
        return "Shutdown aborted"
    else:
        return "Sorry"

# Review: Modules
from math import sqrt
print sqrt(13689)

# Review: Built-In Functions
# First, def a function called distance_from_zero, with one argument. If the type of the argument is either int or float, 
# the function should return the absolute value of the function input. Otherwise, the function should return "Nope".
def distance_from_zero(s):
    if type(s) == int or type(s) == float:
        return abs(s)
    else:
        return "Nope"

#



