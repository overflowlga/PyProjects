#!/usr/bin/python3
#Getting a password from md5 hash

from termcolor import colored
import hashlib

#openning a wordlist
def tryOpen(wordlist):
    global passfile
    try:
        passfile = open(wordlist, "r")
    except:
        print(colored("[!] No such file at the specified path!", 'red'))
        quit()

#user input
passhash = input(colored("[*] Enter MD5 hash value: ", 'cyan'))
wordlist = input(colored("[*] Enter the path to the password file: ", 'cyan'))
tryOpen(wordlist)

#read the words from the passwd file, encode to utf-8, then to md5 hash
for word in passfile:
    encode_wd = word.encode('utf-8')
    #first create md5 object, then generate hex digest
    md5digest = hashlib.md5(encode_wd.strip()).hexdigest()
    #compare the created hash to the user provided value, and print if it's a match
    if md5digest == passhash:
        print(colored("[+] Password found: " + word, 'magenta'))
        exit(0)

print(colored("[!] Password not in the list.", 'red'))