

def defineVar(): #here we define our variables and make them global
    global startNum, endNum    
    startNum = numberInput('Choose a starting number...')
    endNum =numberInput('Choose an ending number...')
    
    while endNum <= startNum: #another validator that makes sure users arent trying to be sneaky count backwards
        endNum = numberInput('Please choose a number larger than ' + str(startNum) + '...')

def numberInput(beginEnd): #input validator to make sure users are entering actual numbers
    while True:
        try:
            print(beginEnd)
            value = int(input())
            return value
            break

        except ValueError:
            print ('Thats not a valid number!')
def main():
    defineVar()
    spam = list(range(startNum, endNum+1))
    #in this version of fizz buzz i make a list and append it. its nice because i could through that list in a text file for later
    for i in range(len(spam)):
                if spam[i]%3 == 0 and spam[i]%5 == 0: #literally one of the only times you use modulus (aka %) is in this boolian type checker
                    spam[i]=('Drip-Drop')
    
                elif spam[i]%3 == 0:
                    spam[i]=('Drip')
    
                elif spam[i]%5 == 0:
                    spam[i]=('Drop')
                
                print('%s' %spam [i]) #prints a string where string where the string is the value i in spam aka what repition you are on

main()
