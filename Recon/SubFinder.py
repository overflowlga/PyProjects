#!/usr/bin/python

from types import TracebackType
import requests
import sys

def request(url):
	try:
		requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass

target_url = input("[*] Enter Target URL: ")
filename = input("[*] Enter File to Use: ")
try:
	file = open(filename, "r")
	for line in file:
		word = line.strip()
		full_url = word + "." + target_url
		response = request(full_url)
		if response:
			print("[+] Found a Subdomain: " + full_url)
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()