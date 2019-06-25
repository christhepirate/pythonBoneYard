spam = 0 #sets initial variable to 0
while spam < 5: #conditional while statment checks value of spam
    print('Hello World.') #prints spam on 5 new lines
    spam = spam + 1
    
print('Please enter a number: ')
userInputNumber = int(input())  
while userInputNumber < 5:
    userInputNumber = int(userInputNumber) + 1
    print(str(userInputNumber))

print('Please type \'up some sorcery\'.') #most effient way
while input() != ('up some sorcery'): #no variable is necessary, the loop will continue until 'up some sorcery' is inputed.
    print('Please type \'up some sorcery\'.')
    continue
    

name = '' 
while True: #as long as the name variable is not 'your name' it will prompt the user to enter a value for the variable 'name'
    print ('Please type \'your name\'.')
    name = input()
    if name != ('your name'):
        continue
    print('Thank You! Enter \'a password\'.')# if an incorrect input is placed here user is kicked back to the start of this blocks while loop
    password = input()
    if password == ('a password'):
        break

#as long as the name variable is not 'your dog's name' it will prompt the user to enter a value for the variable 'nameDog'
nameDog = ''
while nameDog != ('your dog\'s name'):
    print ('Please type \'your dog\'s name\'.')
    nameDog = input()
print('Thank You!')
