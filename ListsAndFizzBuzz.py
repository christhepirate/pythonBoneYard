numberzzz = list(range(0, 101, 1))
fizz = list(range(0, 101, 3))
buzz = list(range(0, 101, 5))
fizzBuzz = list(range(0, 101, 15))



for i in range(len(numberzzz)):
#    print('Letzzz count some numberzzz' + str(i) + '/' + str(numberzzz[i]))
    for j in fizz:
        numberzzz[j]= 'FIZZ'
    for k in buzz:
        numberzzz[k]= 'BUZZ'
    for l in fizzBuzz:
        numberzzz[l]= 'FIZZ-BUZZ'
    print(str(numberzzz[i]))
