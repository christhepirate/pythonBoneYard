#falsey Truthy examples
name = ''
while not name: #If the user enters a blank string for name, then the while statement’s condition will be True
    print('Enter your name please: ')
    name = input()
print ('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough room for all your guests.')
print('Done')
