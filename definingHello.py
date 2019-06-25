
name = ''
while True:
        print('Please enter your name...')
        name = input ()
        if name != (''):
            break
#nameVar is a Parameter
def hello(nameVar):
    print('Hello ' + nameVar)
#the value of 'name' inside of hello() function is a argument
hello(name)

