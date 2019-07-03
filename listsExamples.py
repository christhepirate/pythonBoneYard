#lists of things
#lists values are seperated/delimited w/ comma
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
print('That last one was bacon')

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
print(spam[0:3])

#a slice goes up to, but will not include, the value at the second index

print(bacon [0] [1:4])

#short cut for 0 in the index can be blank
print(bacon [0] [:4])
print(bacon [0] [:3])


print(bacon [1] [:])


#make a list from contents of a list
eggs = bacon[1]
print(eggs)
print('That was eggs...')

#math from list values
print(str(eggs[1]+eggs[2]))

#len of a list displays how many items are within it
print(str(len(spam)))

print('------------------------------------------')

print(spam)
#lets change the values inside of the list
spam[1] = 'aardvark'
print(spam)

#changes rat to aardvark
spam[2] = spam[1]
print(spam)

#we can also use negative indexes
spam[-1] = spam[2]
print(spam)

#lets get a little more complex
#this will change the value at the start of the list 'cat'
#cat becomes a list within a list that contains the slice of spam that contains 3 ardvarks
spam[0] = spam[1:4]
print(spam)




