#!/usr/bin/python

import requests
import sys

def request(url):
	try:
		requests.get("https://" + url)
	except requests.exceptions.ConnectionError:
		pass

target_url = input("[*] Enter Target URL: ")
filename = input("[*] Enter File to Use: ")

try:
	file = open(filename, "r")
	for line in file:
		word = line.strip()
		full_url = target_url + "/" + word
		response = request(full_url)
		if response:
			print("[+] Found a Directory: " + full_url)
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()