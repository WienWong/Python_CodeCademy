
# Day at the Supermarket

# Use a for loop to print out all of the elements in the list names.
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for nm in names:
    print nm
	
# You can also use a for loop on a dictionary to loop through its keys with the following:

# A simple dictionary
d = {"foo" : "bar"}

for key in d: 
    print d[key]  # prints "bar" 
# Note that dictionaries are unordered, meaning that any time you loop through a dictionary, 
# you will go through every key, but you are not guaranteed to get them in any particular order.

# Use a for loop to go through the webster dictionary and print out all of the definitions.
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for key in webster:
    print webster[key]

# Loop through each item in the list called a. If the number is even, print it out. 
# You can test if the item % 2 == 0 to help you out.
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for item in a:
    if item % 2 == 0:
        print item
	
# Lists + Functions
# Functions can also take lists as inputs and perform various operations on those lists.

def count_small(numbers):
    total = 0
    for n in numbers:
        if n < 10:
            total = total + 1
    return total

lost = [4, 8, 15, 16, 23, 42]
small = count_small(lost)
print small

# Write a function called fizz_count that takes a list x as input.
# Create a variable count to hold the ongoing count. Initialize it to zero.
# for each item in x:, if that item is equal to the string "fizz" then increment the count variable.
# After the loop, please return the count variable.
# For example, fizz_count(["fizz","cat","fizz"]) should return 2.
# Write your function below!

def fizz_count(x):
    count = 0
    for pp in x:
        if pp == "fizz":
            count += 1
    print count
    return count
    
fizz_count(["fizz","cat","fizz"])

# String Looping
# Strings are like lists with characters as elements. You can loop through strings the same way you loop through lists!
for letter in "Codecademy":
    print letter
    
# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter
		
# Create a new dictionary called prices using {} format like the example above.
# Put these values in your prices dictionary, in between the {}:
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Create a stock dictionary with the values below.
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

###
once  = {'a': 1, 'b': 2}
twice = {'a': 2, 'b': 4}
for key in once:
    print "Once: %s" % once[key]
    print "Twice: %s" % twice[key]

# In the above example, we create two dictionaries, once and twice, that have the same keys.
# Because we know that they have the same keys, we can loop through one dictionary and print values from both once and twice.
###
# Loop through each key in prices.
# Like the example above, for each key, print out the key along with its price and stock information. 
# Print the answer in the following format:
# apple
# price: 2
# stock: 0
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
	
# Create a variable called total and set it to zero.
# Loop through the prices dictionaries. For each key in prices, multiply the number in prices by the number in stock. 
# Print that value into the console and then add it to total. Finally, outside your loop, print total.
prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    
total = 0
for key in prices:
    print prices[key] * stock[key]
    total = total + prices[key] * stock[key]

print total

# In order for customers to order online, we are going to have to make a consumer interface. 
# First, make a list called groceries with the values "banana","orange", and "apple".
groceries = ["banana", "orange", "apple"]

# Define a function compute_bill that takes one argument food as input.
# In the function, create a variable 'total' with an initial value of zero.
# For each item in the food list, add the price of that item to total. 
# Finally, return the total.
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        total += prices[item]
    return total
	
# Make the following changes to your compute_bill function:
# While you loop through each item of food, only add the price of the item to total if the item's
# stock count is greater than zero. If the item is in stock and after you add the price to the total, 
# subtract one from the item's stock count. 
# Hint: If you're buying a banana, check if it's in stock (larger than zero). If it's in stock, add 
# the cost of a banana to your bill. Finally, decrement the stock of bananas by one!

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item] 
            stock[item] -= 1
    return total

# 	
