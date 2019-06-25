# This Program Says hello and asks for the user's Name
print ('Hello World!')
print ('What is your name?') #ask the user for their name
myName = input() #collects name and stores it into myName
if len(myName) == 0: #verifies that the user has entered a valid character based name
    print('Please enter your name.')
    myName = input() #ask the user for their name
    
print ('It is good to meet you, ' + myName)
print ('The length of you name is: ')
print (len(myName)) #counts the numer of charachters in the users name and displays it

print ('What is your age?') #asks the user for their age
myAge = input()
if myAge != int() or myAge > 120 or myAge <= 0 or len(str(myAge)) == 0:
    print ('Please enter a valid age')
    myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.') #adds one to the users year to let them how old they will be in one years time
