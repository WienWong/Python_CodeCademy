
# Print out the second element in the list.
n = [1, 3, 5]
# Add your code below
print n[1]

# Multiply the second element of the n list by 5
# Overwrite the second element with that result.
n = [1, 3, 5]
# Do your multiplication here
n[1] = n[1]*5
print n

# Append the number 4 to the end of the list n.
n = [1, 3, 5]
# Append the number 4 here
n.append(4)
print n

# n.pop(index) will remove the item at index from the list and return it to you.
# n.remove(item) will remove the actual item if it finds it.
# del(n[1]) is like .pop in that it will remove the item at the given index, but it won't return it.
# Remove the first item from the list n using either .pop(), .remove(), or del.
n = [1, 3, 5]
# Remove the first item in the list here
n.pop(0)
# n.remove(1)
print n

# You pass a list to a function the same way you pass any other argument to a function.
def list_function(x):
    return x

n = [3, 5, 7]
print list_function(n)

# Make list_function returns only the item stored in index one of x.
def list_function(x):
    return x[1]

n = [3, 5, 7]
print list_function(n)

# Add 3 to the item at index one of the list.
# Store the result back into index one.
# Return the list.
def list_function(x):
    x[1] = x[1] + 3
    return x
n = [3, 5, 7]
print list_function(n)

# Define a function called list_extender that has one parameter lst.
# Inside the function, append the number 9 to lst.
# Then return the modified list.
n = [3, 5, 7]
# Add your function here
def list_extender(lst):
    lst.append(9)
    return lst
print list_extender(n)

# Define a function called print_list that has one argument called x.
# Inside that function, print out each element one by one. 
# Then call your function with the argument n.
n = [3, 5, 7]
    
def print_list(x):
    for tmp in range(0, len(x)):
        print x[tmp]
        
print_list(n)

# Create a function called double_list that takes a single argument x (which 
# will be a list) and multiplies each element by 2 and returns that list. 
# Don't forget to return your new list!
n = [3, 5, 7]

# Don't forget to return your new list!
def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i]*2
    return x

print double_list(n)

# The Python range() function is just a shortcut for generating a list, so you can 
# use ranges in all the same places you can use lists.

range(6) # => [0,1,2,3,4,5]
range(1,6) # => [1,2,3,4,5]
range(1,6,3) # => [1,4]

# In all cases, the range() function returns a list of numbers from start up to 
# (but not including) stop. Each item increases by step.
# Make range() that returns a list containing [0, 1, 2].
def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(0,3)) # Add your range between the parentheses!

# Iterating over a list in a function
# Method 1 - for item in list:

for item in list:
    print item
	
# Method 2 - iterate through indexes:

for i in range(len(list)):
    print list[i]

# Method 1 is useful to loop through the list, but it's not possible to modify 
# the list this way. Method 2 uses indexes to loop through the list, making it 
# possible to also modify the list if needed. 

# Define a function called total that accepts one argument called numbers. It will be a list.
# Inside the function, create a variable called result and set it to zero.
# Using one of the two methods above, iterate through the numbers list.
# For each number, add it to result. Finally, return result.
n = [3, 5, 7]

def total(numbers):
    result = 0
    for nm in numbers:
        result += nm
    return result

n = [3, 5, 7]

def total(numbers):
    result = 0
    for nm in range(0, len(numbers)):
        result += numbers[nm]
    return result
	
# Using strings in lists in functions
# Define a function called join_strings accepts an argument called words. It will be a list.
# Inside the function, create a variable called result and set it to "", an empty string.
# Iterate through the words list and append each word to result.
# Finally, return the result.
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for word in words:
        result += word 
    return result

print join_strings(n)

# or
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for word in range(0, len(words)):
        result += words[word] 
    return result

print join_strings(n)

# Using two lists as two arguments in a function
# Define a function called join_lists that has two arguments, x and y. They will both be lists.
# Inside that function, return the result of concatenating x and y together.
m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x, y):
    return x + y

print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]

# Finally, this exercise shows how to make use of a single list that contains 
# multiple lists and how to use them in a function.
list_of_lists = [[1,2,3], [4,5,6]]

for lst in list_of_lists:
    for item in lst:
        print item

# We end up printing out:
# 1
# 2
# 3
# 4
# 5
# 6

# Define a function called flatten with one argument called lists.
# Make a new, empty list called results.
# Iterate through lists. Call the looping variable numbers.
# Iterate through numbers.
# For each number, .append() it to results.
# Finally, return results from your function.
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

# Add your function here

def flatten(lists):
    results = []
    for numbers in lists:
        for nm in numbers:
            results.append(nm)
    return results        

print flatten(n)

# We end up printing out: [1, 2, 3, 4, 5, 6, 7, 8, 9]


