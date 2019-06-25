print('My name is')
for i in range(5): #will print nogged 5 times
    print ('Nogged Five Times ' + str(i+1)) #note count starts at 0 so the i+1 is neccessary to start the count a '1'
#different version of ^
variable = 0
while variable < 5:
    print('Nogged Five More Times ' + str(variable))#notice how this count starts at 0
    variable = variable + 1
    
print('Enter a  number:')
userNumInput = int(input())
total = 0    
    
for num in range (userNumInput+1): #adds 1+2+3+4+5+6+...etc given an input
	total = total + num
	print(str(total))
#more range stuff
print('Time to explore Ranges a Bit')
print('Enter a starting value to begin a count')
startPoint = int(input())
print('Enter an ending Value.')
print('Note: This ending value will not be included in the count')
endingPoint = int(input())
print('Enter an increment to count by')
print('Note: if a negative number is included, the step will count down')
increment = int(input())

for z in range(startPoint, endingPoint, increment):
    print('counting ' + str(z))
    
