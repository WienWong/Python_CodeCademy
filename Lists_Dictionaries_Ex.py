
zoo_animals = ["pangolin", "cassowary", "sloth", "panda"];
# One animal is missing!

if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print "The third animal at the zoo is the " + zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]
	
# Write a statement that prints the result of adding the second and fourth items of the list.
numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
print numbers[1] + numbers[3]

# 
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
zoo_animals[3] = "panda"

#
suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("notebook")
suitcase.append("pencil")
suitcase.append("cellphone")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

#
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]  # Third and fourth items (index two and three)
last   = suitcase[-2:]  # The last two items (index four and five)

# Slicing Lists and Strings
animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]  # The fourth through sixth characters
frog = animals[6:]   # From the seventh character to the end

# Use the .index(item) function to find the index of "duck". Assign that result to a 
# variable called duck_index. Then .insert(index, item) the string "cobra" at that index.
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")   # Use index() to find "duck"

# Your code here!
animals.insert(duck_index, "cobra")

print animals # Observe what prints after the insert operation

# Write a statement in the indented part of the for-loop that prints a number equal to 2*number for every list item.
my_list = [1,9,3,8,5,7]

for number in my_list:
    # Your code here
    print 2*number

# Write a for-loop that iterates over start_list and .append()s each number squared (x**2) to square_list.
# Then sort square_list!
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for num in start_list:
    square_list.append(num**2)

square_list.sort()
print square_list

# A dictionary is similar to a list, but you access values by looking up a key instead of an index. 
# A key can be any string or number. Dictionaries are great for things like phone books 
# (pairing a name with a phone number), login pages (pairing an e-mail address with a username)
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

# Your code here!
print residents['Sloth']
print residents['Burmese Python']

# Like Lists, Dictionaries are "mutable". This means they can be changed after they are created. One 
# advantage of this is that we can add new key/value pairs to the dictionary after it is created like so:
# dict_name[new_key] = new_value
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Beef'] = 20.5
print menu['Beef']
menu['rice'] = 2.50
print menu['rice'] 
menu['milk'] = 1.00
print menu['milk'] 

print "There are " + str(len(menu)) + " items on the menu."
print menu

# Items can be removed from a dictionary with the del command:
# del dict_name[key_name]
# A new value can be associated with a key by assigning a value to the key, like so:
# dict_name[key] = new_value
# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Jungle House'

print zoo_animals

# Remove 'dagger' from the list of items stored in the backpack variable.
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')
print backpack

# Created a dictionary that holds many types of values.
my_dict = {
    "fish": ["c", "a", "r", "p"],
    "cash": -4483,
    "luck": "good"
}
print my_dict["fish"][0]

# Add a key to inventory called 'pocket'. Set the value of 'pocket' to be a list 
# consisting of the strings 'seashell', 'strange berry', and 'lint'.
# .sort() the items in the list stored under the 'backpack' key
# Then .remove('dagger') from the list of items stored under the 'backpack' key
# Add 50 to the number stored under the 'gold' key
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint'] 
inventory['backpack'].sort()
del inventory['backpack'][2] # not del inventory['backpack'[2]]
inventory['gold'] += 50


