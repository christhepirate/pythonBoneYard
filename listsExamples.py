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

#the following will slice the end values into a None or null value
spam[0] = None
print(spam)
#nothing inputed at the end here means it will start at 1 and go to the end 
spam[1:] = None, None, None
print(spam)

#prints a slice from value 2 (note 3rd in list) to value 4
print(spam[2:])



#To actually delet stuff you need to use del
#will delete first 2 values of spam
del spam[:2]
print(spam)

#will delete last 2 values of spam
del spam[2:]
#del is the unassignment of statements

spam[:4]= 'meme1', 'meme2', 'meme3', 'meme4'
print(spam)

spam[4:]= 'meme5', 'meme6', 'meme7', 'meme8'
print(spam)
#see the diff between

bigMeme = [spam[0]]*3
print(bigMeme)

biggestMeme =[spam]*3
print(biggestMeme)

#will return each character as a sigle value in a list 
print(list('Hello'))

if 'meme1' in spam:
    print('MEEEEEEMMMMMMEEEEEESS')

if 'emem' not in spam:
    print('aaaaaaaahhhh')

#to recap
    #A list is a value that contains multiple valiues
    #the values in a list are also called 'items'
    #you can access items in a list with it's integer index
    #the indexes trat at Zero not 1
    #you can also use negative indexes, such as -1 or -2 etc...
    #negative indexes dont start at zero
    #you can get multiple items from the list using a slice
    #a slice has 2 indexes. the new lists items start at the first index and go up to (but do NOT include) the second index
    #the len() function, concatentation (+), and replication (*) work the sam way with lists as they do with strings
    #you can convert a value into a list by passing it to the list() function.









