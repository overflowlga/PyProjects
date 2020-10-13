#!/usr/bin/python

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator
		if result == 0:
			print("Port {} is open".format(port))

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
