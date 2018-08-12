#!/usr/bin/python36
import random
import string
from http import cookies
import os


# Generate and save cookie on server
def set_cookie(username):
	# Generate random string of length 32 and store it in cookie
	cookie_auth = username + '_'
	cookie_auth += ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])	

	# Add user cookie entry to cookies.txt on server
	# Read all user cookies
	f = open('cookies/cookies.txt', 'r')
	lines = f.readlines()
	f.close()

	# Update the already existing user cookie
	found_user = False
	f = open('cookies/cookies.txt', 'w')
	for line in lines:
		if username in line.split(':')[0]:
			f.write(username + ':' + cookie_auth + '\n')
			found_user = True
		else:
			f.write(line)

	# Add user cookie to server if it does not already exist
	if found_user == False:
		f.write(username + ':' + cookie_auth + '\n')
	f.close()

	# Create the cookie 
	ck = cookies.SimpleCookie()

	# Assign value to cookie
	ck['secret'] = cookie_auth

	# Set expiry time to 3hr
	ck['secret']['expires'] = 1*1*3*60*60
	return ck


# Get cookie value stored on client browser
def get_cookie():
	if 'HTTP_COOKIE' in os.environ:
		cookie_string = os.environ.get('HTTP_COOKIE')
		ck = cookies.SimpleCookie()
		ck.load(cookie_string)

		# Return cookie value if found, else return -1 
		try:
			data=ck['secret'].value
			return data
		except KeyError:
			return -1
	return -1


# Authenticate user if server side cookie matches client side cookie
def auth_client():
	# Fetch client cookie from browser
	client_cookie = str(get_cookie())
	
	# Fetch client cookie from server
	server_cookies = open('cookies/cookies.txt', 'r')
	
	# Search for client cookie line by line 
	for server_cookie in server_cookies:
		# If client cookie matches server cookie, return True
		if client_cookie in server_cookie:
			server_cookies.close()	
			# Return username if cookie found			
			#return (server_cookies.split(':')[0])	
			return True
	server_cookies.close()

	# If client cookie not matches any server cookie, return False
	return False