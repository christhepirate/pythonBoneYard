#makes a 4x4 or 8x8 patern
while True:
    userInput = str(input('please enter a 4 or 8 character pin: '))
    if len(userInput) == 8:
        break
    if len(userInput) == 4:
        break
def printOut():
    print(userInput, userInput, sep= '|')#seperates the input of the user w/ pipe

for i in range (len(userInput)):
    printOut()

