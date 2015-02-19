
# The Datetime Library

from datetime import datetime

# We can use a function called datetime.now() to retrieve the current date and time.

# Create a variable called now and store the result of datetime.now() in it. Then, print the value of now.

now = datetime.now()
print now   
# 2015-02-19 22:57:00.108056

# On a new line, print now.year. 
print now.year   
# 2015

# Then, print out now.month.
print now.month   
# 2

# Finally, print out now.day.
print now.day   
# 19

# What if we want to print today's date in the following format mm/dd/yyyy?
print '%s/%s/%s' % (now.month, now.day, now.year)   
# 2/19/2015

# Similar to the last exercise, print the current time in the pretty form of hh:mm:ss.
print '%s:%s:%s' % (now.hour, now.minute, now.second)   
# 23:4:15

# Print the date and time together in the form: mm/dd/yyyy hh:mm:ss.
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)   
# 2/19/2015 23:5:58


