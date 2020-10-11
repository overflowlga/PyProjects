#!/usr/bin/python3
#Checks if a server is vulnerable when provided with a banner list

import socket
import os
import sys
from termcolor import colored

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(4)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVulns(banner, filename):
    f = open(filename, "r")
    for line in f.readlines():
        if line.strip("\n") in banner:
            print(colored('[+] Server is vulnerable: ' + banner.strip("\n"), 'yellow'))

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print(colored("[-] File Doesn't Exist.", 'red'))
            exit(0)
        if not os.access(filename, os.R_OK):
            print(colored('[-] Access Denied.', 'red'))
            exit(0)
    else:
        print(colored('[+] Usage: ' + str(sys.argv[0]) + " <vuln filename>", 'cyan'))
        exit(0)
    portlist = [21,22,25,80,110,443,445]
    for x in range(4,6):
        ip = "xx.xx.xx.xx" + str(x) #Change IP
        for port in portlist:
            banner = retBanner(ip,port)
            if banner:
                print(colored('[+] ' + ip + "/" + str(port) + " : " + banner, 'cyan'))
                checkVulns(banner, filename)

main()