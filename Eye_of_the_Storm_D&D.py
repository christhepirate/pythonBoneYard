#Coastal themed D&D adventure module/text based adventure
#lets start by Giving our character a name based on the users choice.
def nameGen():
    global adventurerName
    print('Hello adventurer!')
    while True:
        print('Please enter your name...')
        adventurerName = input ()
        if adventurerName != (''):
            break
    

        
nameGen()

def welcome(adventurerName):
    print('Welcome ' + str(adventurerName) + ', to the Island\'s of Kaliem!')

welcome(adventurerName)

#Places
    #Kaliem
        #Main Land that icludes a subset of islands detailed below.
    #Island's of Kaliem
        #Tirawesh
#Characters
    #Auntie Freon
        #Leader of Hag Coven, and 'captain?' of the bastard Ice-berg Vessel "The Shatterd Jewel"
        #Worshiper of Sea Demon/Demi-god?
    #Vasir
        #leader of the Thieves guild on the Isle of Mikaar
