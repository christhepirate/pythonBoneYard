#!/usr/bin/env python3
#Example PEXPECT script for FTP

import pexpect

def childExpectSendline(expectText, sendlineText):
    child.expect(expectText)
    child.sendline(sendlineText)

def main():
    #open connection and login
    child = pexpect.spawn('ftp ftp.redhat.com')
    childExpectSendline('Name.*:', 'ftp')
    childExpectSendline('Password:', 'ftp')


    #CD and download
    childExpectSendline('ftp>', 'cd /pub/redhat/linux/enterprise/7Server/en/Ansible')
    childExpectSendline('ftp', 'get ansible-2.5.7-1.el7ae.src.rpm')


    #quit
    childExpectSendline('ftp', 'quit')



main()






