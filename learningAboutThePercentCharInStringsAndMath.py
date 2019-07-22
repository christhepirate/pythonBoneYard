spam = int(input('please enter a number... '))
ham = spam
print(spam)
spam %= 3
print(str(spam) + ' is the modulus of the number you chose divided by 3.')
print('The modulus is the remander left when you divide one number from another.')
print('Lets do some work with strings as well.')

spam = int(input('please enter another number... '))
print('I own %s computers but I seldom use more than 3' %(spam))
#the %s in this fuction acts as a variable. you can also use more than one variable in the fuction
#%d is digits i.e 1, 2, 3
#%s is strings
#%f is a float

print('I own %s computers but I seldom use more than %s' %(spam, ham))
#this is  a %d example
bitches = 99
print('I got %d problems.' %bitches)

#this is a %f example
print ('I like %f numbers' %100)#notice how this time i did not have to define 'Nice before hand'

#this will add 10 'space' characters before adding 'Nice to the end
print('I like %10s spacing' %'Nice')

#lets do some stuff with leadig zeroes
print('I like to skate %05d days a week' % spam)

