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
        #Intends slaughter massive amounts of Toa and human life to achieve godhood
        #needs to gain magical jewel to channel soals into the natural toa god death ability
        #will also need to convince or capture enough toa and toa spawn to slaughter.
    #Vasir
        #leader of the Thieves guild on the Isle of Mikaar
        #wants the JEwel to sell for a fortune to the highest bidder (or maybe will sell selectavly to keep the island safe)

