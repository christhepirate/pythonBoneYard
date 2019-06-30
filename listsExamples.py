#lists of things
spam = ['cat', 'bat', 'rat', 'eliphant',]

#prints the entire contents of the list spam.
print(spam)

#prints the first value from the left in the list spam
print(spam[0])

#prints the last value in a list or the first value from the right
print(spam[-1])

#lists inside of a list
bacon = [spam, [10, 20, 30, 40]]

#prints the entire contents of the list bacon, which inludes the list spam.
print(bacon)

#prints the first value in bacon which is the entire list spam
print(bacon[0])

#prints 2nd value of the first list spam
print(bacon[0] [1])

#prints the last value of the last list in bacon
print(bacon[-1] [-1])

#concatinate into print statment. notice for the int value in the list i must convert to str in order to concat
print('The ' + bacon[0] [-1] + ' is afraid of the ' + str(bacon[1] [2]) + ' ' + bacon[-2] [-2] + 's.')

#these are all single value indexes
#a list of values is a slice
#notice the seperation w/ a colon
print(spam[0:2])
print(bacon [0] [0:2])

#make a list from contents of a list
eggs = bacon[1]
print(str(eggs))

#math from list values
print(str(eggs[1]+eggs[2]))







