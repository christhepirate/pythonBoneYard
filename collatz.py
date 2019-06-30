while True:
    try:
        userNum =int(input('Please enter a number'))
        break
    except ValueError:
        print ('Thats not a valid number!')

def collatz(userNum):
    if userNum != 1: #if not 1
        
        if userNum % 2 ==0: #if even
            userNum=userNum//2
            print(str(userNum))
            collatz(userNum)
            
        elif userNum % 2 == 1: #if odd
            userNum = 3 * userNum + 1
            print(str(userNum))
            collatz(userNum)       

collatz(userNum)


    
