#global and local scope examples
import sys

#verifys 4 char value and stores it in userPin
while True:
    print ('Enter a 4 character value...')
    userPin = str(input())
    if len(userPin) == 4:
        checker = userPin #sneaky little global variable to make sure users endet different values
        break
#defining the main function to be called later
def main():
    while True:
        print ('Enter a 4 character value other than ' + checker + '...')
        userPin = str(input())
        if len(userPin) == 4 and userPin != checker:
            break
    #displays value of local userPin to user to show iportance of local v global
    print(userPin + ' is the local value of userPin.')    

#displays value of global userPin and calls tha main function or exits program. will loop as long as user wishes to continue
    
while True:
    print(userPin + ' is the global value of userPin.')
    print('Would you like to run the main function to enter a different local value for userPin?')
    userInput = input('[y/n]...')
    if userInput.upper() == 'Y':
        main()
    elif userInput.upper() == 'N':
        sys.exit()
