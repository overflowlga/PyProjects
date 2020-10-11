#!/usr/bin/python3
#Cracking a crypt password with a salt

import crypt
from termcolor import colored

def crackpass(cryptw):
    salt = cryptw[0:2]
    dictionary = open("dictionary.txt", 'r') #specify a dictionary here
    for word in dictionary.readlines():
        word = word.strip('\n')
        cryptpass = crypt.crypt(word, salt)
        if (cryptw == cryptpass):
            print(colored("[+] Password found: " + word, 'magenta'))
            return True

def main():
    passfile = open('passwd.txt', 'r')
    for line in passfile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptw = line.split(':')[1].strip(' ').strip('\n')
            print("[~] Cracking password for: " + user)
            crackpass(cryptw)

main()