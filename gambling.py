#time for some RNG gambling
import random, sys #imports the random module and the sys module

#returns whatever the number puts in and will not accept bad inputs
#startOrEnd changes the printed text depending on which number we are assigning
def numberInput(startEndGuess):
    while True:
        try:
            print(startEndGuess)
            value = int(input())
            return value
            break

        #except ValueError:
        except:
            print ('Thats not a valid number!')
            
#calls numberInput and places it inside startNum and endNum. also checks a valid range has been inputed
#it was easier for me to make Num variables global than to return them            
def defineVar():
    global startNum, endNum, tryNum, secretNumber
    
    startNum = numberInput('Choose a starting number...')
    endNum =numberInput('Choose an ending number...')
    
    while endNum <= startNum:
        endNum = numberInput('Please choose a number larger than ' + str(startNum) + '...')

    tryNum = 1 + numberInput('Please select how many tries you would like to have...')
    while tryNum <=1:
        tryNum = 1 + numberInput('You cannot have less than 1 try!')
    
    secretNumber = (random.randint(startNum, endNum))
    
def guessTicker(guessesTaken):
    if guessesTaken == tryNum -2:
        print('You have only 1 guess remaining!')
    else:
        print('You have ' + str(tryNum-1-guessesTaken) + ' guesses remaining.')
    

def main():
    print('Let\'s play a game where you try to guess what number I am thinking of in a range of your choosing.')
    print('First, let\'s pick some numbers.')
    defineVar()
    print('I am thinking of a number between ' + str(startNum) + ' and ' + str(endNum) + '.') 

    # Ask the player to guess x times.
    for guessesTaken in range(1, tryNum):
        while True:
            try:
                guess = int(input())
                break

            except ValueError:
                print ('Thats not a valid number!')
                
        if guess < secretNumber:
            print('Your guess is too low.')
            guessTicker(guessesTaken)
            
        elif guess > secretNumber:
            print('Your guess is too high.')
            guessTicker(guessesTaken)
        else:
            break    # This condition is the correct guess!
        
    if guess == secretNumber:
        print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber))
    while True:
        print('Would you like to play again?')
        userInput = input('[y/n]...')
        if userInput.upper() == 'Y':
            main()
        elif userInput.upper() == 'N':
            sys.exit()


main()
                    

