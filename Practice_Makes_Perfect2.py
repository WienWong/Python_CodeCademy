
# # Practice Makes Perfect 2 includes question 8 to 14.

# 8. scrabble_score
# Scrabble is a game where players get points by spelling words. Words are scored by adding 
# together the point values of each individual letter (we'll leave out the double and triple 
# letter and word scores for now).

# Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word.
# Assume your input is only one word containing no spaces or punctuation.
# As mentioned, no need to worry about score multipliers!
# Your function should work even if the letters you get are uppercase, lowercase, or a mix.
# Assume that you're only given non-empty strings.
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    word = word.lower()
    tot = 0
    for lt in word:
        print score[lt]
        tot += score[lt]
    return tot
    
print scrabble_score("Helix")
# 4
# 1
# 1
# 1
# 8
# 15

# 9. censor
# Write a function called censor that takes two strings, text and word, as input. 
# It should return the text with the word you chose replaced with asterisks.
# For example:
# censor("this hack is wack hack", "hack") 
# should return
# "this **** is wack ****"

# Assume your input strings won't contain punctuation or upper case letters.
# The number of asterisks you put should correspond to the number of letters in the censored word.

# You can use
# string.split()
# and 
# " ".join(list)
# to help you here.
# Remember:
# "*" * 4 equals "****"
# After splitting the string with string.split(), you can loop through the indices in the list and replace the 
# words you are looking for with their asterisk equivalent. Join the list at the end to get your sentence!
def censor(text, words):
    textsplited=text.split()
    print text
    lst=[]
    for ch in textsplited:
        if ch==words:
            ch="*"*len(words)
        print ch
        lst.append(ch)
    print lst
    return " ".join(lst)       

print censor("this hack is wack hack", "hack") 

# result:
# this hack is wack hack
# this
# ****
# is
# wack
# ****
# ['this', '****', 'is', 'wack', '****']
# this **** is wack ****

# 10. count
# Define a function called count that has two arguments called sequence and item.
# Return the number of times the item occurs in the list.
# For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).
def count(sequence, item):
    acc=0
    for nm in sequence:
        if nm==item:
            acc+=1
    return acc
    
print count([1,2,1,1], 1)
print count(['1','2','1','1'], '1')

# 11. purify
# Define a function called purify that takes in a list of numbers, removes all odd numbers 
# in the list, and returns the result. For example, purify([1,2,3]) should return [2].
def purify(lst):
    newlst=[]
    for nm in lst:
        if nm%2==0:
            newlst.append(nm)
    return newlst
print purify([1,2,3])

# 12. product
# Define a function called product that takes a list of integers as input and returns the 
# product of all of the elements in the list. For example: product([4, 5, 5]) should return 100.

def product(lst):
    outcome=1
    for nm in lst:
        outcome *= nm 
    return outcome
print product([4, 5, 5])

# 13. remove_duplicates
# Write a function remove_duplicates that takes in a list and removes elements of the list that 
# are the same. For example: remove_duplicates([1,1,2,2]) should return [1,2].
# Don't remove every occurrence, since you need to keep a single occurrence of a number.
# The order in which you present your output does not matter. So returning [1,2,3] is the same as returning [3,1,2].
# Do not modify the list you take as input! Instead, return a new list.
# The easiest way to approach this problem is to create a new list in your function, loop through
# your input list, and add items from your input list to your new list if the current item is not 
# already contained in your new list. Using the a not in b syntax might help you here.
#
# Also, note that destructively modifying a list while you are looping through it is bad practice
# and will likely lead to bugs somewhere down the line! That's why we always make a fresh copy to work on.
def remove_duplicates(lst):
    newlst=[]
    for nm in lst:
        if nm not in newlst:
            newlst.append(nm)
    return newlst
print remove_duplicates([1,1,2,2]) 

# 14. median
# The median is the middle number in a sorted sequence of numbers.
# Finding the median of [7,12,3,1,6] would first consist of sorting the sequence into 
# [1,3,6,7,12] and then locating the middle value, which would be 6.

# If you are given a sequence with an even number of elements, you must average the two 
# elements surrounding the middle. For example, the median of the sequence [7,3,1,4] is 3.5, 
# since the middle elements after sorting the list are 3 and 4 and (3 + 4) / (2.0) is 3.5.

# You can sort the sequence using the sorted() function, like so:
# sorted([5, 2, 3, 1, 4]) gives [1, 2, 3, 4, 5]
print round(5/2)
def median(lst):
    lstsorted=sorted(lst)
    if (len(lstsorted)%2 != 0):
        return lstsorted[ (len(lstsorted)+1) /2 - 1] 
    else:
        return (lstsorted[len(lstsorted)/2] \
        + lstsorted[len(lstsorted)/2 - 1])/2.0

print median([7,3,1,4])          #3.5
print median([6, 8, 12, 2, 23])  #3.0

