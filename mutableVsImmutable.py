#!/usr/bin/env python3
#mutable vs immutable data objects
#list are mutable
spam =['a', 'b', 'c']
print(spam)
spam[1]='x'
print('%s\n%s' %(spam, 'Lists are mutable'))

try:
    name = 'Zophie a cat'
    name[7] = 'the '
except TypeError:
    print('Strings are also immutable')
ham = ('a', 'b', 'c')
try:
    ham[1]='x'
except TypeError:
    print('tuples are immutable')

spam.append(ham)
print('%s\n%s' %(spam, 'Mutable objects can contain immutable objects'))

bacon = (1, 2, 3, spam)
print('%s\n%s' %(bacon, 'Immutable objects can contain mutable objects'))

spam.remove(ham)
print('%s\n%s' %(bacon, 'Immutable objects can contain mutable objects that change'))




    
