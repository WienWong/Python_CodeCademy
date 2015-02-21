# Pig Latin is a language game, where you move the first letter of the word to the end and add "ay." So "Python" becomes
# "ythonpay."

print 'Welcome to the Pig Latin Translator!'

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:len(word)] + first + pyg
    print new_word
else:
    print 'empty'
