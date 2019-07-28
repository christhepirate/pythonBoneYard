spam = 0 #sets initial variable to 0
while spam < 5: #conditional while statment checks value of spam
    print('Hello World.') #prints spam on 5 new lines
    print(str(spam))
    spam = spam + 1
 

while True:
    try:
        print ('Please enter a natural number less than 100: ')
        userInputNumber = int(input())
        while userInputNumber < 100:
            userInputNumber = int(userInputNumber) + 1
            print(str(userInputNumber))
        break

    except ValueError:
        print ('Thats not a natural number!')

        

#while userInputNumber < 100:
    

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
for i in name:
    print('**** %s ****' %i)



#as long as the name variable is not 'your dog's name' it will prompt the user to enter a value for the variable 'nameDog'
nameDog = ''
while nameDog != ('your dog\'s name'):
    print ('Please type \'your dog\'s name\'.')
    nameDog = input()
print('Thank You!')
