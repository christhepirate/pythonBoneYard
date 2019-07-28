
import random
spam = ['Hello', 'Hi', 'howdie', 'heyas']
print(spam.index('Hello'))
print(spam.index('howdie'))
spam.append('Hokely') #adds 'Hokely to the end of spam.
print(spam)
spam.insert(0, 'YEEHAA')#adds 'YEEHAA' the begining of spam
print('%s' %spam[0])
print('%s' %spam[spam.index('howdie')]) #case sensitive Howdie HOWDIE hOWDIE will not work
print('%s' %spam)
for i in range (2):
    spam.append('YEAAAAA BUUUUUDDDY')

print('%s' %spam.index('YEAAAAA BUUUUUDDDY')) # will only the fisrt instance
print('%s' %spam)
spam.remove('YEAAAAA BUUUUUDDDY') #will remove the First instance of YEAH BUDDY
spam.sort() #sorts spam ASCIIbetically AAAABBBBZZZZaaaabbbbzzzz
print('%s' %spam)
spam.sort(key=str.lower)#sorts in true alphebetical
print('%s' %spam)


numbers = list(range(1,11))
for i in range(10):
        numbers[i]=(random.randint(1,9))

print('%s' %numbers) #prints a list of random numbers
numbers.sort() #sorts the list of random numbers
print('%s' %numbers) #notice that even though these are int values since i a calling a list i need to make it a string instead of digits
numbers.sort(reverse=True) #reverses the sorted order
print('%s' %numbers) #you cannot use sort if the list contains int and str values
for i in range(10):
        numbers[i]=(str(random.randint(1,9))) #but if you convert to str
        numbers.append('A')
print('%s' %numbers)
numbers.sort()
print('%s' %numbers)

        

