#!/usr/bin/python3
#Cracking a SHA1 hash with an online dictionary

from urllib.request import urlopen
import hashlib
from termcolor import colored

sha1hash = input(colored("[*] Enter Sha1 Hash Value: ", 'cyan'))

#take the list of passwords from the internet
passlist = str(urlopen('https://raw.githubusercontent.com/skyzyx/bad-passwords/master/raw.txt').read(), 'utf-8')
for password in passlist.split('\n'):
    #turn the password string into sha1
    hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
    if hashguess == sha1hash:
        print(colored("[+] The Password is: " + str(password), 'magenta'))
        quit()

print("Password is not in the passwordlist.")