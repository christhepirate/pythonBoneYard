#global and local scope examples
import sys

def globalVal():
    global checker, userPin
    while True:
        print ('Enter a 4 character value...')#Defines global value for variable userPin
        userPin = str(input())
        if len(userPin) == 4: #verifys 4 char value and stores it in userPin
            checker = userPin #sneaky little global variable to make sure users endet different values
            break
        
#example of changing local value of a same-named variable
def localVal():
    while True:
        print ('Enter a 4 character value other than ' + checker + '...')
        userPin = str(input())#redefines userPin in the local scope
        if len(userPin) == 4 and userPin != checker: #note the global scope variale is compared to the local variable userPin 
            break
    #displays value of local userPin to user to show importance of local v global
    print(userPin + ' is the local value of userPin.')    

#displays value of global userPin and calls tha localVal function or exits program. will loop as long as user wishes to continue    
def main():
    globalVal()
    while True:
        print(userPin + ' is the global value of userPin.')
        print('Would you like to run the localVal function to enter a different local value for userPin?')
        userInput = input('[y/n]...')
        if userInput.upper() == 'Y':
            localVal()
        elif userInput.upper() == 'N':
            while True:
                print('Would you like to run the globalVal function to enter a different global value for userPin?')
                userInput = input('[y/n]...')
                if userInput.upper() == 'Y':
                    main()
                elif userInput.upper() == 'N':
                    sys.exit()
main()
