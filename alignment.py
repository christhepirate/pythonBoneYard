#Initiating Variable
import random
#random only needs to imported one time for the duration of the program.
#this way the computer doesnt need to process the import random every time the user fucks up
#credit G Chin

print('Roll alignment?')
roll = input()

while roll == 'yes':

    lawChaos = ['Lawful ','Neutral ','Chaotic ']
    goodEvil = ['Good','Neutral','Evil']

    r1 = random.randint(0,2)
    r2 = random.randint(0,2)

    rollAlignment = str(lawChaos[r1]) + str(goodEvil[r2])

    if rollAlignment == 'Neutral Neutral':
        print('True Neutral')

    else:
        print(rollAlignment)
                                           

    print('Reroll?')

    roll = input()
    
