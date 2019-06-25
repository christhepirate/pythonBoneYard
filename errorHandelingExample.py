#error handeling practice
#NOTE: I have commented out the first example for the sake of having both a working and broken example available

    #simple funtion that returns whatever we put into it divided by 42.
#def div42by(divideBy):
    #return 42 / divideBy

#print(div42by(2))
#print(div42by(12))
#print(div42by(0))
    #python cannot handle dividing numbers by zero.
    #this  will spit out "ZeroDivisionError: division by zero"
    #since the program crashes print(div42by(1)) never has the opertunity to run 
#print(div42by(1))

def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError: #this will skip the part of the code that attempts to divide by zero and instead displays this message
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))#this part of the code now gets skiped.
print(div42by(1))
