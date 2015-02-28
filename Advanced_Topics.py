
# Advanced Topics -- List Comprehension, Lambda Expressions

# Iterators for Dictionaries
# Let's start with iterating over a dictionary. Recall that a dictionary is just a collection of keys and values.

d = {
    "Name": "Guido",
    "Age": 56,
    "BDFL": True
}
print d.items()
# => [('BDFL', True), ('Age', 56), ('Name', 'Guido')]
# Note that the items() function doesn't return key/value pairs in any specific order. 

# keys() and values()
# Whereas items() returns an array of tuples with each tuple consisting of a key/value pair from the dictionary:
# The keys() function returns an array of the dictionary's keys, and
# The values() function returns an array of the dictionary's values.
# Again, these functions will not return the keys or values from the dictionary in any specific order.

# You can think of a tuple as an immutable (that is, unchangeable) list (though this is an oversimplification); 
# tuples are surrounded by ()s and can contain any data type.

# Remove your call to items() and replace it with a call to keys() and a call to values(), each on its own line. 
# Make sure to print both!
my_dict={
    "Name": "Guido",
    "Age": 56,
    "Gender": True
    };
    
print my_dict.keys()
print my_dict.values()

# result
['Gender', 'Age', 'Name']
[True, 56, 'Guido']

# The 'in' Operator
# For iterating over lists, tuples, dictionaries, and strings, Python also includes 
# a special keyword: in. You can use in very intuitively, like so:

for number in range(5):
    print number,

d = { "name": "Eric", "age": 26 }
for key in d:
    print key, d[key],

for letter in "Eric":
    print letter,  # note the comma!

# Building Lists
# Let's say you wanted to build a list of the numbers from 0 to 50 (inclusive). We could do this pretty easily:
my_list = range(51)
# But what if we wanted to generate a list according to some logic—for example, a list of all 
# the even numbers from 0 to 50? Python's answer to this is the list comprehension. List comprehensions
# are a powerful way to generate lists using the for/in and if keywords we've learned.
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

# List Comprehension Syntax
# Here's a simple example of list comprehension syntax:

new_list = [x for x in range(1,6)]
# => [1, 2, 3, 4, 5]
# This will create a new_list populated by the numbers 1 to 5. If you want those numbers doubled, you could use:

doubles = [x*2 for x in range(1,6)]
# => [2, 4, 6, 8, 10]
# And if you only wanted the doubled numbers that are evenly divisible by three:

doubles_by_3 = [x*2 for x in range(1,6) if (x*2)%3 == 0]
# => [6]

# Use a list comprehension to build a list called even_squares in the editor.
# Your even_squares list should include the squares of the even numbers between 1 to 11. 
# Your list should start [4, 16, 36...] and go from there.

doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]
# Complete the exercise. Use the example above for help.
even_squares = [nm**2 for nm in range(1,12) if nm % 2 == 0]
print even_squares

# 
c = ['C' for x in range(5) if x < 3]
print c
# The example above creates and prints out a list containing ['C', 'C', 'C'].

# Use a list comprehension to create a list, cubes_by_four.
# The comprehension should consist of the cubes of the numbers 1 through 10 
# only if the cube is evenly divisible by four.
# Finally, print that list to the console.
cubes_by_four=[num**3 for num in range(1,11) if num%2==0]
print cubes_by_four
# result:
[8, 64, 216, 512, 1000]

# List Slicing Syntax
# [start:end:stride]
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l[2:9:2]
[9, 25, 49, 81]

# Omitting Indices
# If you don't pass a particular index to the list slice, Python will pick a default.

to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E'] 

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']

# The default starting index is 0.
# The default ending index is the end of the list.
# The default stride is 1.

# Use list slicing to print out every odd element of my_list from start to finish.
my_list = range(1, 11) # List of numbers 1 - 10

# Add your code below!
print my_list[::2]

# Reversing a List
# letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]
# In the example above, we print out ['E', 'D', 'C', 'B', 'A'].

# Create a variable called backwards and set it equal to the reversed version of my_list.
my_list = range(1, 11)

# Add your code below!
backwards=my_list[::-1]

print backwards

# Stride Length
# Create a variable, backwards_by_tens, and set it equal to the result of going backwards 
# through to_one_hundred by tens. Go ahead and print backwards_by_tens to the console.

to_one_hundred = range(101)
# Add your code below!

backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

# Practice Makes Perfect
# Create a list, to_21, that's just the numbers from 1 to 21, inclusive.
# Create a second list, odds, that contains only the odd numbers in the to_21 list 
# (1, 3, 5, and so on). Use list slicing for this one instead of a list comprehension.
# Create a third list, middle_third, that's equal to the middle third of to_21, from 8 to 14, inclusive.
to_21=range(1,22)
print to_21
odds=to_21[0::2]
print odds

odds2=[num for num in to_21 if num%2==1]
print odds

print len(to_21)/3 
print 2*len(to_21)/3 
middle_third=to_21[(len(to_21)/3): (2*len(to_21)/3) :1]
print middle_third
# result
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
7
14
[8, 9, 10, 11, 12, 13, 14]

# 12. Anonymous Functions
# One of the more powerful aspects of Python is that it allows for a style of programming called 
# functional programming, which means that you're allowed to pass functions around just as if they 
# were variables or values. Sometimes we take this for granted, but not all languages allow this!

# Check out the code at the right. See the lambda bit? Typing

lambda x: x % 3 == 0
Is the same as

def by_three(x):
    return x % 3 == 0
# Only we don't need to actually give the function a name; it does its work and returns a value 
# without one. That's why the function the lambda creates is an anonymous function.

# When we pass the lambda to filter, filter uses the lambda to determine what to filter, and the 
# second argument (my_list, which is just the numbers 0 – 15) is the list it does the filtering on.
 
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

# [0, 3, 6, 9, 12, 15]

# 13. Lambda Syntax
# Lambda functions are defined using the following syntax:

my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)
# Lambdas are useful when you need a quick function to do some work for you.
# If you plan on creating a function you'll use over and over, you're better off 
# using def and giving that function a name.

# Fill in the first part of the filter function with a lambda. The lambda should ensure 
# that only "Python" is returned by the filter.
# Fill in the second part of the filter function with languages, the list to filter.
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x=="Python", languages)

# ['Python']

# 14. Try It
cubes = [x**3 for x in range(1, 11)]
filter(lambda x: x % 3 == 0, cubes)
# The example above is just a reminder of the syntax.

# Create a list, squares, that consists of the squares of the numbers 1 to 10. 
# A list comprehension could be useful here!
# Use filter() and a lambda expression to print out only the squares that are between 30 and 70 (inclusive).
squares=[num**2 for num in range(1,11)]
print filter(lambda xx: 30<=xx<=70, squares)

# [36, 49, 64]

# 15. Iterating Over Dictionaries
# Call the appropriate method on movies such that it will print out all the items (hint, hint) 
# in the dictionary—that is, each key and each value.
movies = {
    "Monty Python and the Holy Grail": "Great",
    "Monty Python's Life of Brian": "Good",
    "Monty Python's Meaning of Life": "Okay"
}

print movies.items()

# [("Monty Python's Life of Brian", 'Good'), ("Monty Python's Meaning of Life", 'Okay'), \
#  ('Monty Python and the Holy Grail', 'Great')]

# 16. Comprehending Comprehensions
# Use a list comprehension to create a list, threes_and_fives, that consists only of the numbers 
# between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.
threes_and_fives=[x for x in range(1,16) if x%3==0 or x%5==0]

# 17. List Slicing
# The string in the editor is garbled in two ways:
# First, our message is backwards;
# Second, the letter we want is every other letter.
# Use list slicing to extract the message and save it to a variable called message.

# The string in the editor is garbled in two ways:
# First, our message is backwards;
# Second, the letter we want is every other letter.
# Use list slicing to extract the message and save it to a variable called message.
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
print garbled
message=[ch for ch in garbled if ch!="X"]
print message
print "".join(message)
message="".join(message)[::-1]
print message

# 18. Lambda Expressions
# Create a new variable called message.
# Set it to the result of calling filter() with the appropriate lambda that will filter 
# out the "X"s. The second argument will be garbled.
# Finally, print your message to the console.
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message=filter(lambda x: x!="X", garbled)
print message

# I am another secret message!
