#!/usr/bin/env python3
#mutable vs immutable data objects
#list are mutable
spam =['a', 'b', 'c']
print(spam)
spam[1]='x'
print('%s\n%s\n' %(spam, 'Lists are mutable'))

name = 'Zophie a cat'
try:
    name[7] = 'the'
except TypeError:
    print('Strings are also immutable')
#but we can slice them around
newName = name[0:7] + 'the' + name[8:12]
print('%s\n%s\n' %(name, newName))
name=newName
print('%s\n%s\n' %(name, newName))
#We used [0:7] and [8:12] to refer to the characters that we don’t want to replace

print(type(('hello',)))
#they are identified by () unlike [] for lists. also if you oonly have one value in a tuble include the trailing "," like above
#Tuples cannot have their values modified, appended, or removed
ham = ('a', 'b', 'c')
try:
    ham[1]='x'
except TypeError:
    print('tuples are immutable')
#use tuples if you never want the values changed, list if you do.

spam.append(ham)
print('%s\n%s' %(spam, 'Mutable objects can contain immutable objects'))

bacon = (1, 2, 3, spam)
print('%s\n%s' %(bacon, 'Immutable objects can contain mutable objects'))

spam.remove(ham)
print('%s\n%s' %(bacon, 'Immutable objects can contain mutable objects that change'))




    
