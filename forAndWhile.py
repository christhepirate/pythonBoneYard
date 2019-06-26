print('My name is')
for i in range(5): #will print Bogged Five Times 5 times
    print ('Bogged Five Times ' + str(i+1)) #note count starts at 0 so the i+1 is neccessary to start the count a '1'
#different version of ^
variable = 0
while variable < 5:
    print('Bogged Five More Times ' + str(variable))#notice how this count starts at 0
    variable = variable + 1

while True:
    try:
        print('Please select a natural number...')
        userNumInput = int(input())    
        break
    
    except ValueError:
        print('That was not a natural number!')
        
     
for num in range (userNumInput+1): #adds 1+2+3+4+5+6+...etc given an input
    total = 0
    total = total + num
    print(str(total))
	
#more range stuff
print('Time to explore Ranges a Bit')
print('Enter a starting value to begin a count')
while True:
    try:
        print('Please select a natural number...')
        startPoint = int(input())    
        break
    
    except ValueError:
        print('That was not a natural number!')

print('Enter an ending Value.')
print('Note: This ending value will not be included in the count')
while True:
    try:
        print('Please select a natural number...')
        endPoint = int(input())    
        break
    
    except ValueError:
        print('That was not a natural number!')
        
print('Enter an increment to count by')
print('Note: if a negative number is included, the step will count down')

while True:
    try:
        print('Please select a natural number besides zero...')
        increment = int(input())
        if increment !=0:
            break
    
    except ValueError:
        print('That was not a natural number!')

for z in range(startPoint, endPoint, increment):
    print('counting ' + str(z))
    
