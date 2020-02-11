#!/usr/bin/env python3
#sample script that gets host names

import pexpect

def childExpectSendline(expectText, sendlineText):
    child.expect(expectText)
    child.sendline(sendlineText)

def main():
    #open connection and login
    child = pexpect.spawn('ssh 192.168.0.111')
    childExpectSendline('.*password:', 'Password01')



    #run hostname command
    childExpectSendline('\[.*~\]\$','hostname')
    print(child.before)

    #logout
    childExpectSendline('\[.*~\]\$','exit')




main()





#Run host names command

#logout
