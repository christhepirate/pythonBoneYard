#!/usr/bin/env python3
startNum = None
endNum = None
def defineVar(): #here we define our variables and make them global
    global startNum, endNum    
    startNum = numberInput('Choose a starting number...')
    endNum =numberInput('Choose an ending number...')

def numberInput(beginEnd): #input validator to make sure users are entering actual numbers
    while True:
        try:
            print(beginEnd)
            value = int(input())
            return value
            break

        except ValueError:
            print ('Thats not a valid number!')


def power(num,power=2,result = 1): #assigns power a default value of 2 and result a default value of 1
     for i in range(power):
         result = result * num
     print(result)

def main():   
    defineVar()
    power(startNum, endNum)
    print (multi_add(startNum, endNum))
    print (multi_add(startNum, endNum, 1, 2, 3, 4, 5))

    
    
power(5)
power(5, 2)
power(5, 3)


#function that adds variable number of numbers
def multi_add(*args): #variable number of arguments
    result = 0
    for x in args:
        result = result + x
    return result



main()
