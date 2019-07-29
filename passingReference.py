#!/usr/bin/env python3

import copy

def eggs(someParameter):
    print('%s spam before'%spam)
    someParameter.append('Hello')
    print('%s spam after (NOT BACON)'%spam)
    print('%s whatever was thrown in eggs\n'%someParameter)
#notice how the list is modified in place and no return statment is necessary.

spam = [1, 2, 3]
eggs(spam)

#notice how this time it was the bacon that was modified by eggs but both spam and bacon where changed
bacon = spam
eggs(bacon)

#this copies the origional list without passing the refrence thus keeping the origional intact if the other refrence is chenged

cheese = copy.copy(spam)
cheese[1]=42
print('%s\n%s' %(spam, cheese))

