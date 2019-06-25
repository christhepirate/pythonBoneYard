#time for some RNG gambling
import random, sys #imports the random module and the sys module
print('Choose a starting number...')
startNum = int(input())

print('Choose an ending number...')
endNum = int(input())
while endNum <= startNum:
    print('Please choose a number larger than ' + str(startNum))
    endNum = int(input())

print (str(random.randint(startNum, endNum)))

sys.exit()#kills system before it can exicute the print Goodbye
print('Gooodbye')
