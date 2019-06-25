print('This is a calculator program that does basic math.')

def numSelection():
    global num1, num2
    while True:
        try:
            print('Please select two whole numbers...')
            num1 = int(input('First number: '))
            num2 = int(input('Second number: '))
            break
        except ValueError:
            print('That was not a whole number!')
            
def addition(add1, add2):
    return add1 + add2

def subtraction(sub1, sub2):
    return sub1 - sub2

def multiplication(mul1, mul2):
    return mul1 * mul2

def division(div1, div2):
    try:
        return div1 / div2
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')
        


def main ():
    global choice
    while True:
        print('Would you like to do addition, subtraction, multiplication, or division?')
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

        elif choice.upper() == 'MULTIPLICATION':
            numSelection()
            calculated = multiplication(num1, num2)
            print(calculated)
            break

        elif choice.upper() == 'DIVISION':
            numSelection()
            calculated = division(num1, num2)
            print(calculated)
            break
main()
