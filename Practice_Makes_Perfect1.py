
# Practice Makes Perfect 1 includes question 1 to 7.

# 1. Define a function is_even that will take a number x as input.
# If x is even, then return True.
# Otherwise, return False.
def is_even(x):
    return x%2==0
	
# 2. For the purpose of this lesson, we'll also say that a number with a decimal part that 
# is all 0s is also an integer, such as 7.0.

# Define a function is_int that takes a number x as an input.
# Have it return True if the number is an integer (as defined above) and False otherwise.

# If the difference between a number and that same number rounded down is greater than zero, 
# what does that say about that particular number?
def is_int(x):
    return (x - round(x) == 0)
print is_int(7.0)
print is_int(7.1)
print is_int(7)
print is_int(0.0)

# Result:
# True
# False
# True
# True

# 3. Try summing the digits of a number.
# Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits.
# For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4.
# (Assume that the number you are given will always be positive.)

# I solved the 'reverse' question first so the code seems weird.
def digit_sum(number):
    text = str(number)
    n=0
    tot=0
    while(n<len(text)):
        print text[len(text)-n-1],
        tot+= int(text[len(text)-n-1])
        n+=1
    print
    return tot

# same idea but added in sequence
def digit_sum(number):
    text = str(number)
    n = 0
    tot = 0
    while(n<=len(text)-1):
        print text[n],
        tot += int(text[n])
        n += 1
    return tot

print "digit sum is " + str(digit_sum(1234))

# Below method copied from the internet
	
def digit_sum(n):
    return sum(map(int,str(n)))

	# But, a more intuitive and procedural approach you'll understand better is this:

def digit_sum(n):
    sum = 0
    for x in str(n):
        sum += int(x)
    return sum
    
print digit_sum(1234)

# A challenge solution could try like this: to get the rightmost digit of a number, you 
# can modulo (%) the number by 10. To remove the rightmost digit you can floor divide (//) the number by 10. 
def digit_sum(n):
    summ = 0
    while n:
        summ += n%10
        n/=10
        print n 
    return summ
print digit_sum(1234)

# result:
# 123
# 12
# 1
# 0
# 10

# 4. Define a function factorial that takes an integer x as input.
# Calculate and return the factorial of that number.
# Consider having factorial() call itself. When the input is 1, your function could just return 1.
# Otherwise, it could return the number multiplied by factorial(n - 1).
# Note that mathematically, factorial(0) is 1.
def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
        
print factorial(5)

# 5. is_prime
# A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.
# In other words, if you want to test if a number in a variable x is prime, then no other number should go 
# into x evenly besides 1 and x.

# Define a function called is_prime that takes a number x as input.
# For each number n from 2 to x - 1, test if x is evenly divisible by n.
# If it is, return False.
# If none of them are, then return True. 
# Remember: all numbers less than 2 are not prime numbers!
def is_prime(x):
    if x < 2 :
        return False
		
    elif x == 2:
        return True  

    for numbers in range(2, x):
            if x%numbers == 0:
                return False
    return True 

# 6. Reverse a text
# method 1
print 'hello world'[::-1]

# method 2
backwards = ''.join(reversed('hello world'))
print backwards

# (Note that without the ''.join(), you'd get a <reversed object at 0x7f0839728d10> instead.)
# method 3
def reverse(text):
    print range(0,len(text)) # check items of using range()
    lst1=[None]*len(text)    # creat empty list same size as the text
    print lst1
	
    lst2 = []
    for item in range(len(text)):
        lst2.append(text[len(text)-1-item])
    return ''.join(lst2)
	
print reverse('hello')

# same idea by using while loop

def reverse(text):
    n=0
    lst=[]
    while(n < len(text)):
        print text[len(text)-n-1],
        lst.append(text[len(text)-n-1]),
        n+=1        
    print n
    return ''.join(lst)
print reverse("abcd") 

# 7. anti_vowel 
# Define a function called anti_vowel that takes one string, text, 
# as input and returns the text with all of the vowels removed.
# For example: anti_vowel("Hey You!") should return "Hy Y!".
# Don't count Y as a vowel.
# Make sure to remove lowercase and uppercase vowels.
VOWELS=["a","e","i","o","u","A","E","I","O","U"]

def anti_vowel(text):
    new = ''
    for ch in text:
        if ch not in VOWELS:
            new += ch
    return new
    
print anti_vowel("Hey You!")

# Or:
VOWELS=["a","e","i","o","u","A","E","I","O","U"]

def anti_vowel(text):
    lst=[]
    for ch in text:
        if ch not in VOWELS:
            lst.append(ch)
    return "".join(lst)
	# return lst # this results in ['H', 'y', ' ', 'Y', '!']
    
print anti_vowel("Hey You!")

# Or even:
VOWELS=["a","e","i","o","u","A","E","I","O","U"]

def anti_vowel(text):
    return "".join(ch for ch in text if ch not in VOWELS)
    
print anti_vowel("Hey You!")

