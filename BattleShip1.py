
# Battleshipe1 -- step by step

# The first thing we need to do is to set up the game board.
# Create a variable board and set it equal to an empty list.
board = []

# Create a 5 x 5 grid initialized to all 'O's and store it in board.
# Use range() to loop 5 times. Inside the loop, .append() a list 
# containing 5 "O"s to board, just like in the example above.
# Use the print command to display the contents of the board list.
print ["O"] * 5
board = []
for t in range(0, 5):
    board.append(["O"] * 5)
print board

# [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 
# 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]

# We could print the board out like a grid with each row on its own line.
# We can use the fact that our board is a list of lists to help us do this.
# First, delete your existing print statement.
# Then, define a function named print_board with a single argument, board.
# Inside the function, write a for loop to iterates through each row in board and print it to the screen.
# Call your function with board to make sure it works.
board = []
for t in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print row
print_board(board)
# the board's layout
#['O', 'O', 'O', 'O', 'O']
#['O', 'O', 'O', 'O', 'O']
#['O', 'O', 'O', 'O', 'O']
#['O', 'O', 'O', 'O', 'O']
#['O', 'O', 'O', 'O', 'O']

# We're getting pretty close to a playable board, but wouldn't it be nice 
# to get rid of those quote marks and commas? We're storing our data
# as a list, but the player doesn't need to know that!

letters = ['a', 'b', 'c', 'd']
print " ".join(letters)
print "---".join(letters)

# In the example above, we create a list called letters.
# Then, we print a b c d. The .join method uses the string to combine the items in the list.
# Finally, we print a---b---c---d. We are calling the .join function on the "---" string.
# We want to turn each row into "O O O O O".

# Inside your function, inside your for loop, use " " as the separator to 
# .join the elements of each row.
board = []
for t in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)
print_board(board)

# Now, let's hide our battleship in a random location on the board.
# Since we have a 2-dimensional list, we'll use two variables to 
# store the ship's location, ship_row and ship_col.

from random import randint
coin = randint(0, 1)
dice = randint(1, 6)

# In the above example, we first import the randint(low, high) function from the random module.
# Then, we generate either zero or one and store it in coin.
# Finally, we generate a number from one to six inclusive.

# Define two new functions, random_row and random_col, that each take board as input.
# These functions should return a random row index and a random column index 
# from your board, respectively. Use randint(0, len(board) - 1).
# Call each function on board.
from random import randint 

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

# Add your code below!
def random_row(board):
    return randint(0, len(board) - 1)
    
def random_col(board):
    return randint(0, len(board) - 1)
    
random_row(board)
random_col(board)

# For now, let's store coordinates for the ship in the variables ship_row 
# and ship_col. Now you have a hidden battleship in your ocean! 
# Let's write the code to allow the player to guess where it is.
number = raw_input("Enter a number: ")
if int(number) == 0:
    print "You entered 0"
	
# raw_input asks the user for input and returns it as a string. But we're going to want to use 
# integers for our guesses! To do this, we'll wrap the raw_inputs with int() to convert the string to an integer.

# Create a new variable called guess_row and set it to int(raw_input("Guess Row: ")).
# Create a new variable called guess_col and set it to int(raw_input("Guess Col: ")).
board = []

for x in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Add your code below!
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

# While we're writing and debugging this part of the program, it will be helpful to know where 
# that battleship is hidden. Let's add a print statement that displays the location of the hidden ship.

# Print the value of ship_col.
# Print the value of ship_row.
board = []

for x in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Add your code below!
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))
print ship_col
print ship_row

##
# For a guess to be right, guess_col should be equal to ship_col and 
# guess_row should be equal to ship_row.
if guess_col == 0 and guess_row == 0:
    print "Top-left corner."
# The example above is just a reminder about if statements.

# Add an if guess_row equals ship_row and guess_col equals ship_col.
# If that is the case, please print out "Congratulations! You sank my battleship!"
def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

print ship_row
print ship_col

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
	
# Of course, the player isn't going to guess right all the time, 
# so we also need to handle the case where the guess is wrong.
print board[2][3]
# The example above prints out "O", the element in the 3rd row and 4th column.

# Add an else under the if we wrote in the previous step.
# Print out "You missed my battleship!"
# Set the list element at guess_row, guess_col to "X".
# As the last line in your else statement, call print_board(board) again so you can see the "X".
# Make sure to enter a col and row that is on the board!
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

print ship_row
print ship_col

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
else:
    print "You missed my battleship!"
    #guess_row = "X"
    #guess_row = "X"
    board[int(guess_row)][int(guess_row)] = "X"
    print_board(board)

# Now we can handle both correct and incorrect guesses from the user. 
# But now let’s think a little bit more about the "miss" condition.
# They can enter a guess that's off the board.
# They can guess a spot they’ve already guessed.
# They can just miss the ship.
# We'll add these tests inside our else condition. Let's build the first case now!
if x not in range(8) or \
   y not in range(3):
        print "Outside the range"
# The example above checks if either x or y are outside those ranges. 
# The \ character just continues the if statement onto the next line.

# Add a new if: statement that is nested under the else.
# Like the example above, it should check if guess_row is not in range(5) or guess_col is not in range(5).
# If that is the case, print out "Oops, that's not even in the ocean."
# After your new if: statement, add an else: that contains your existing handler for an incorrect guess. 
from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

print ship_row
print ship_col

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
else:
    if guess_row not in range(5) or guess_col not in range(5):
        print "Oops, that's not even in the ocean."
    else:
        print "You missed my battleship!"
        board[int(guess_row)][int(guess_row)] = "X"
        print_board(board)
	
# 
# Now let's handle the second type of incorrect guess: the player guesses a location 
# that was already guessed. How will we know that a location was previously guessed?
print board[guess_row][guess_col]
# The example above will print an 'X' if already guessed or an 'O' otherwise.

# Add an elif to see if the guessed location already has an 'X' in it.
# If it has, print "You guessed that one already."

from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

print ship_row
print ship_col

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
else:
    if guess_row not in range(5) or guess_col not in range(5):
        print "Oops, that's not even in the ocean."
    elif guess_row == guess_row and guess_col == guess_col:
        print "You guessed that one already."
    else:
        print "You missed my battleship!"
        board[int(guess_row)][int(guess_row)] = "X"
        print_board(board)

#
# Make sure you play it a couple of times and try different kinds of incorrect guesses. 
# This is a great time to stop and do some serious debugging.
# In the next step, we'll move on and look at how to give the user 4 guesses to find the battleship.

# to allow the player to make up to 4 guesses before they lose.

for turn in range(4):
    # Make a guess
    # Test that guess
# We can use a for loop to iterate through a range. Each iteration will be a turn.

# Add a for loop that repeats the guessing and checking part of your game for 4 turns, like the example above.
# At the beginning of each iteration, print "Turn", turn + 1 to let the player know what turn they are on.
# Indent everything that should be repeated.
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should go in your for loop!
for turn in range(4):
    # Be sure to indent four spaces!
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
    	else:
    	    print "You missed my battleship!"
    	    board[guess_row][guess_col] = "X"        
    	# Print (turn + 1) here!
    	print "Turn", turn + 1
    	print_board(board)
	
# Add an if statement that checks to see if the user is out of guesses.

# Put it under the else that accounts for misses.
# Put it after the if/elif/else statements that check for the reason 
# the player missed. We want "Game Over" to print regardless of the reason.
# If turn equals 3, print "Game Over".
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should go in your for loop!
for turn in range(4):
    # Be sure to indent four spaces!
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
    	# Print (turn + 1) here!
    	print "Turn", turn + 1
    	print_board(board)
    	if turn == 3:
    	    print "Game Over"
	
# Add a break under the win condition to end the loop after a win.
# Your break should go inside your if statement, right after your "Congratulations!" message.
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

for turn in range(4):

    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        # Print (turn + 1) here!
        print "Turn", turn + 1
        print_board(board)
        if turn == 3:
            print "Game Over"
			
# You may want to take some time to clean up and document your code as well.
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    # Everything from here on should go in your for loop!
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        # Print (turn + 1) here!
        print "Turn", turn + 1
        print_board(board)
        if turn == 3:
            print "Game Over"
            print "The ship hides at: "
            print ship_row
            print ship_col
	
