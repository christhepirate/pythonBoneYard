numberzzz = list(range(101))
fizz = list(range(1, 101, 3))
buzz = list(range(1, 101, 5))
fizzBuzz = list(range(1, 101, 15))



for i in range(len(numberzzz)):
#    print('Letzzz count some numberzzz' + str(i) + '/' + str(numberzzz[i]))
    for j in fizz:
        numberzzz[j]= 'FIZZ'
    for k in buzz:
        numberzzz[k]= 'BUZZ'
    for l in fizzBuzz:
        numberzzz[l]= 'FIZZ-BUZZ'
    print(str(numberzzz[i]))
