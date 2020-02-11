#!/usr/bin/env python3
#Random Password Generator

#imports and global
import random, sys, string

#validates that the user has entered a valid number
def intValidation(textToPrint):
    while True:
        try:
            print(textToPrint)
            value = int(input()
                        )
            return value
            break

        except ValueError:
            print ('Thats not a valid number!')
            
def bitLengthInput():
    #asks the user how many bits they would like the password to be
    bitLength = intValidation('Please select a bit length.')
    while bitLength <= 0:
        bitlength = intValidation('Please select positive integer')
    return bitLength

def entropyLevelInput():
    entropyLevel = intValidation('Please select your level of entropy from 1 to 4')
    while entropyLevel < 1 or entropyLevel > 4:
        entropyLevel = intValidation('Please select 1, 2, 3, or 4')
    return entropyLevel


def randomString(bitLength, entropyLevel):
    #Generate a random string of fixed length
    if entropyLevel == 1:
        characters = string.ascii_lowercase #lowercase letters only
    elif entropyLevel == 2:
        characters = string.ascii_letters #upper and lowecase letters
    elif entropyLevel ==3:
        characters = string.ascii_letters + string.digits #upper/lower plus digits
    elif entropyLevel ==4:
        characters = string.printable #all characters considered printable 
    
    return ''.join(random.choice(characters) for i in range(bitLength)
                   ) #joins a black space plus one of our characters and does it bitLength times

#flow of program
def main():
    print ("Your random password is ", randomString(bitLengthInput(), entropyLevelInput()
                                                    )
           )

#Calls the main function
if __name__ == "__main__":
        main()
