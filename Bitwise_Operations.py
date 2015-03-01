
# Bitwise Operations

# Bitwise operations are operations that directly manipulate bits.
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT

# result
0
10
0
13
38
-89

# In Python, you can write numbers in binary format by starting the number with 0b. 
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11

# result
1 2 3 4 5 6 7
******
4
9

# One to Twelve
one    = 0b1
two    = 0b10
three  = 0b11
four   = 0b100
five   = 0b101
six    = 0b110
seven  = 0b111
eight  = 0b1000
nine   = 0b1001  
ten    = 0b1010  
eleven = 0b1011
twelve = 0b1100 

# The bin() function. bin() takes an integer as input and returns the binary representation of 
# that integer in a string. (Keep in mind that after using the bin function, you can no longer 
# operate on the value like a number.) You can also represent numbers in base 8 and base 16 
# using the oct() and hex() functions. 

print bin(2)
print bin(3)
print bin(4)
print bin(5)
0b10
0b11
0b100
0b101

# What you might not know is that the int function actually has an optional second parameter.

int("110", 2)
# ==> 6
# When given a string containing a number and the base that number is in, the function will 
# return the value of that number converted to base ten.
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001", 2)
#
1
2
7
4
5
201

# Left and right shift bitwise operators
