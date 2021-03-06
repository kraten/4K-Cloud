#!/usr/bin/python36
import cgi
import cookie
import subprocess as sp


def show_body_content():
	print('''

		<h2>Launch Software on Windows</h2><br><br>
		<a href="/downloads/firefox.bat" class="btn btn-primary btn-lg" download>
	    <i class="fa fa-firefox"></i> Launch Firefox
	   	<div class="ripple-container"></div></a><br><br>

	   	<a href="/downloads/sublime.bat" class="btn btn-primary btn-lg" download>
	    <i class="fa fa-text-width"></i> Launch Sublime
	   	<div class="ripple-container"></div></a>

	<!-- Add socket JS library -->
	<script src="/js/socket_speech.js"></script>

	<!-- Add speech synthesizer JS library -->
	<script src="/js/say.js"></script>

	<!-- Add speech recognition JS library -->
	<script src="/js/annyang.min.js"></script>

	<!-- Add speech recognition GUI JS library -->
	<script src="/js/speechkitt.min.js"></script>

	<!-- Add speech processor JS library -->
	<script src="/js/speech.js"></script>
	''')


def show_start_content():
	f = open('../html/start_content.txt', 'r')
	print(f.read())
	f.close()


def show_end_content():
	f = open('../html/end_content.txt', 'r')
	print(f.read())
	f.close()


def print_headers():
	print("content-type: text/html \n")

def redirect_login():
	print("""
		<script>window.location = "/login.html";</script>
		""")


def auth_user():
	ck_usr = cookie.auth_client()
	if ck_usr == True:
		pass
	else: 
		redirect_login()


def main():
	print_headers()
	auth_user()
	
	show_start_content()
	show_body_content()
	show_end_content()


main()