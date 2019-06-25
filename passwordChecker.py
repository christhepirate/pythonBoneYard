
print('please enter the password')
password = input() #prompts the user for a password

if password == 'swordfish': #if input holds correct password
    print('Access granted')
    
elif password == 'password': #else if the input holds a poor password 
    print('that is a poor password')
    print('Access Denied')
    
else: #else access is simply denied if all prev statments are false
    print('Access Denied') 
