
# Loops, note the 'enumerate' and 'zip' function

# Loop so as to counts up to 9 (inclusive).
count = 0

if count < 5:
    print "Hello, I am an if statement and count is", count
    
while count < 10:
    print "Hello, I am a while and count is", count
    count += 1
	
# Conditions
loop_condition = True

while loop_condition:
    print "I am a loop"
    loop_condition = False
	
#
num = 1

while num<=10:  # Fill in the condition
    # Print num squared
    print num**2
    # Increment num (make sure to do this!)
    num += 1

# A common application of a while loop is to check user input to see if it is valid. For example,
# if you ask the user to enter y or n and they instead enter 7, then you should re-prompt them for input.

# Fill in the loop condition so the user will be prompted for a choice over and over while choice 
# does not equal 'y' and choice does not equal 'n'.
choice = raw_input('Enjoying the course? (y/n)')

while choice!='y' and choice!='n':  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

# The break is a one-line statement that means "exit the current loop." An alternate way to make our 
# counting loop exit and stop executing is with the break statement.

# First, create a while with a condition that is always true. The simplest way is shown.
# Using an if statement, you define the stopping condition. Inside the if, you write break, meaning "exit the loop."
# The difference here is that this loop is guaranteed to run at least once.
count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break
		
# While / else
# while/else is similar to if/else, but there is a difference: the else block will execute 
# anytime the loop condition is evaluated to False. This means that it will execute if the loop 
# is never entered or if the loop exits normally. If the loop exits as the result of a break, 
# the else will not be executed.

# In below example, the loop will break if a 5 is generated, and the else will not execute. 
# Otherwise, after 3 numbers are generated, the loop condition will become false and the else will execute.
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"
# Result	
# Lucky Numbers! 3 numbers will be generated.
# If one of them is a '5', you lose!
# 6
# 5
# Sorry, you lose!
# Or
# Lucky Numbers! 3 numbers will be generated.
# If one of them is a '5', you lose!
# 4
# 2
# 3
# You win!

# Use a while loop to let the user keep guessing so long as guesses_left is greater than zero.
# Ask the user for their guess, just like the second example above.
# If they guess correctly, print 'You win!' and break.
# Decrement guesses_left by one.
# Use an else: case after your while loop to print You lose.
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if guess==random_number:
        print "you win!"
        break
    guesses_left -= 1 
else:
    print "you lose!"

# Make the loop print the numbers from 0 to 19 instead of 0 to 9.
print "Counting..."

for i in range(20):
    print i
   
# Create a for loop that prompts the user for a hobby 3 times, then appends each one to hobbies.
hobbies = []

# Add your code below!
for i in range(3):
    hobby=raw_input("Your hobby: ")
    hobbies.append(hobby)
print hobbies

# Add a second for loop so that each character in word is printed one at a time.
thing = "spam!"

for c in thing:
    print c

word = "eggs!"

# Your code here!
for w in word:
    print w
	
# 
word = "Marble"
for char in word:
    print char,

# The , character after our print statement means that our next print statement keeps printing on the same line.

# Let's filter out the letter 'A' from our string.
# Do the following for each character in the phrase.
# If char is an 'A' or char is an 'a', print 'X', instead of char. Make sure to include the trailing comma.
# Otherwise (else:), please print char, with the trailing comma.
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
    if char=="A" or char=="a":
        print "X",
    else:
        print char,

print

# Write a second for loop that goes through the numbers list and prints 
# each element squared, each on its own line.
numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
    print num

# Add your loop below!
for tmp in numbers:
    print tmp**2
	
# On line 5, print the key, followed by a space, followed by the value associated with that key.
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    print key + " " + str(d[key])
	
# A weakness of using this for-each style of iteration is that you don't know the index of the 
# thing you're looking at. Generally this isn't an issue, but at times it is useful to know how 
# far into the list you are. Thankfully the built-in enumerate function helps with this.
#
# enumerate works by supplying a corresponding index to each element in the list that you pass 
# it. Each time you go through the loop, index will be one greater, and item will be the next 
# item in the sequence. It's very similar to using a normal for loop with a list, except this 
# gives us an easy way to count how many items we've seen so far.
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index, item 
	
# We don't want the user to see things listed from index 0, since this looks unnatural. 
# Instead, the items should appear to start at index 1. Modify the print statement 
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index+1, item 
	
# It's also common to need to iterate over two lists at once. This is where the built-in zip function comes 
# in handy. zip will create pairs of elements when passed two lists, and will stop at the end of the shorter 
# list. zip can handle three or more lists as well!

# Compare each pair of elements and print the larger of the two.
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    if a<b:
        print b
    else:
        print a
  
# For / else
# Just like with while, for loops may have an else associated with them.
# In this case, the else statement is executed after the for, but only if the for ends 
# normally—that is, not with a break. This code will break when it hits 'tomato', so the 
# else block won't be executed.
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'
	
# Result:
# You have...
# A banana
# A apple
# A orange
# A tomato is not a fruit!

# Modify the code in the editor such that the for loop's else statement is executed.
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'cheese':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'
	
# Result:
# You have...
# A banana
# A apple
# A orange
# A tomato
# A pear
# A grape
# A fine selection of fruits!

