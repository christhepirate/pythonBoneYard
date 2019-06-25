spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue #3 will not print because it will be execcuting continue
    
    print ('spam is ' + str(spam))
