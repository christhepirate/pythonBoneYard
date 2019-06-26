#hello spam
while True:
    try:
        print('Please enter a number')
        userNum = int(input())  
        break
    
    except ValueError:
        print('That was not a number!')


if userNum == 2:
    print ('Howdy')
else:
    print('Greetings!')

for i in range (10):
    print(str(i+1))
x = 0

while x < 10:
    x = x +1
    print(str(x))
    
