#!/usr/bin/env python3
#dictionaryTime
#a dictionarty is similar to a list in that they are a collection of values
#in a dictionary you do not need to use a integer for your index
import sys
myCat={'size': 'THICC', 'color': 'gray', 'disposition': 'loud'}
print('%s%s\n'%('My cat is ', myCat['size']))

#you can also use integer values as keys or values in a dictionary
spam = {12345: 'Luggage Combo', 'The Answer': 42}
print(spam)


ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
if ham == eggs:
    print('Dictionarys are unorderd,' +\
          '\nThis means they cannot be sliced!')
try:
    spam['color']
except KeyError:
	print('Trying to access a key that does not exist in a dictionary will result in a "KeyError" error message')

#here we a new dictionary key 'color' with a value 'red' to spam
spam['color'] = 'red'

#the for loop will itorate over each value

for i in spam.items():
    print(i)
    print('These are the items in the Dictionary')

for v in spam.values():
    print(v)
    print('these are the values in the dictionary')


for k in spam.keys():
    print(k)
    print('These are the keys in the Dictionary')
sys.clear()
