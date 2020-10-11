#!/usr/bin/python3
#Checks if anonymous login is possible

import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'anonymous')
        print("[*] " + hostname + " FTP anonymous logon succeeded.")
        ftp.quit()
        return True
    except Exception:
        print("[-] " + hostname + " FTP anonymous logon failed.")

host = input("Enter the IP Address: ")
anonLogin(host)
