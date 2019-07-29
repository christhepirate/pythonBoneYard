#!/usr/bin/env python3

#here we create the initial dictionary
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True: #while loop keeps asking for input until user enters an epty string into name
        name = input('\nEnter a name: (blank to quit)\n')
        if name == '' or name == 'blank': #or if the user entersm blank lmao
            break

        if name in birthdays: #checks to see if the name the user entered is in birth days
            print('%s has a birthday on %s' %(name, birthdays[name]))

        else:
            print('I dont have any birthday related information for %s' %name +\
                  '\nWhat is their birthday?')
            birthdays[name] = input('Format: Month abv. space date (i.e. Feb 2 )\n')

            if birthdays[name] == '':
                break
            breakprint('Birthday database updated')
