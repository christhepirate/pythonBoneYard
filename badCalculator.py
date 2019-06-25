print('This is a calculator program that does basic math.')

def numSelection():
    global num1, num2
    print('Please select two whole numbers...')
    num1 = int(input('First number: '))
    num2 = int(input('Second number: '))

def addition(add1, add2):
    return add1 + add2

def subtraction(sub1, sub2):
    return sub1 - sub2

def main ():
    global choice
    while True:
        print('would you like to do addition or subtraction?')
        choice = input ()
        if choice.upper() == 'ADDITION':
            numSelection()
            calculated = addition(num1, num2)
            print(calculated)
            break
            
        elif choice.upper() == 'SUBTRACTION':
            numSelection()
            calculated = subtraction(num1, num2)
            print(calculated)
            break
main()
