
# Conditionals & Control Flow

def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

# Comparators
# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False

# (20 - 10) > 15
bool_one = False    # We did this one for you!

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
bool_two = False

# 1**2 <= -1
bool_three = False

# 40 * 4 >= -4
bool_four = True

# 100 != 10**2
bool_five = False

# Create comparative statements as appropriate on the lines below!

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = 3 > 5

# Make me true!
bool_three = 100 == 2*50

# Make me false!
bool_four = 1 != 1

# Make me true!
bool_five = 5 - 3 > 0

"""
     Boolean Operators
------------------------      True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""

# Set bool_one equal to the result of False and False
bool_one = False

# Set bool_two equal to the result of -(-(-(-2))) == -2 and 4 >= 16**0.5
bool_two = False

# Set bool_three equal to the result of 19 % 4 != 300 / 10 / 10 and False
bool_three = False

# Set bool_four equal to the result of -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2
bool_four = True

# Set bool_five equal to the result of True and True
bool_five = True

# Set bool_one equal to the result of 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'
bool_one = True

# Set bool_two equal to the result of True or False
bool_two = True

# Set bool_three equal to the result of 100**0.5 >= 50 or False
bool_three = False

# Set bool_four equal to the result of True or True
bool_four = True

# Set bool_five equal to the result of 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1
bool_five = False

# not is evaluated first;
# and is evaluated next;
# or is evaluated last.

# Set bool_one equal to the result of False or not True and True
bool_one = False

#Set bool_two equal to the result of False and not True or True
bool_two = True

#Set bool_three equal to the result of True and not (False or False)
bool_three = True

#Set bool_four equal to the result of not not True or False and not True
bool_four = True

#Set bool_five equal to the result of False or not (True and True)
bool_five = False

# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = (2 <= 2) and "Alpha" == "Alpha" 

# Make me false!
bool_three = (4 <= 2) and "Alpha" == "Alpha" 

# Make me true!
bool_four = (4 <= 2) or "Alpha" == "Alpha"

# Make me true!
bool_five = (4 <= 4) and "Alpha" == "Alpha"

# Will the below print statement print to the console? Set response to 'Y' if you think so, and 'N' if you think not.

response = 'Y'

answer = "Left"
if answer == "Left":
    print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    
# 
def using_control_once():
    if 6 < 8:
        return "Success #1"

def using_control_again():
    if 1 != 0:
        return "Success #2"

print using_control_once()
print using_control_again()

# 
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False       # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False        # Make sure this returns False

#
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

#
# Make sure that the_flying_circus() returns True
# Make sure that the_flying_circus() returns True
def the_flying_circus():
    if (44 < 55):    # Start coding here!
        # Don't forget to indent
        return True
        print "it's true"
    elif (not 1 == 1):
        # You'll want to add the else statement, too!
        return False
        print "it's false"
    else:
        return False
		
#

