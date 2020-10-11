#!/usr/bin/python3
#Usage: -H <target host> -P <taget port>

import argparse
from socket import *
from threading import *
from termcolor import colored


def connection(tHost, tPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tHost, tPort))
        print(colored(f"[=>] {tPort}/tcp Open", 'magenta'))
    except:
        print(colored(f"[=>] {tHost}/tcp Closed", 'yellow'))
    finally:
        sock.close()


def portscan(tHost, tPorts):
    try:
        tIP = gethostbyname(tHost)
    except:
        print(f"Unknown Host {tHost} ")
    try:
        tName = gethostbyaddr(tIP)
        print(colored("[=>] Scan results for:" + tName[0], 'cyan'))
    except:
        print(colored("[=>] Scan results for: " + tIP, 'cyan'))
    setdefaulttimeout(4)
    for tPort in tPorts:
        t = Thread(target = connection, args=(tHost, int(tPort)))
        t.start()


def main():
    parser = argparse.ArgumentParser(description="Usage of program: -H <target host> -P <taget port>")
    #parser add argument #name    #help description         #variable type
    parser.add_argument('-H', help = 'specify target host', type = str)
    parser.add_argument('-P', help = 'specify target ports separated by comma', type = str)
    #must set args = parser arguments before creating tHost and tPort = to arguments in parser
    args = parser.parse_args()
    #setting variables to argument
    tHost = args.H
    tPorts = str(args.p).split(',')
    #checking if tHost or tPort are == to empty string, if so print description
    if tHost == None or tPorts[0] == None:
        print(parser.description)
        exit(0)
    else:
        print(colored(f"Host Entered: {tHost}  Port Entered: {tPorts}", 'cyan'))
    #calling portscan function
    portscan(tHost,tPorts)


if __name__ == '__main__':
    main()