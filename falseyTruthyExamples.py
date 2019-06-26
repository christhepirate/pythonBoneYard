#falsey Truthy examples
name = ''
while not name: #If the user enters a blank string for name, then the while statement’s condition will be True
    print('Enter your name please: ')
    name = input()

while True:
    try:
        print ('How many guests will you have?')
        numOfGuests = int(input())    
        if numOfGuests >= 0:
            break
        elif numOfGuests < 0:
            print('You can\'t have fewer than zero guests!')
    
    except ValueError:
        print('That was not a number!')
if numOfGuests: #if zero is inputed the following print statment will not be displayed
    print('Be sure to have enough room for all your guests.')
print('Done')#this will always be displayed
