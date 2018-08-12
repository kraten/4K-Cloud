#!/usr/bin/python36
import cgi
import cookie
import subprocess as sp


def show_body_content():
	print('''
		<div class="alert alert-success">
            <div class="container">
                <div class="alert-icon">
                    <i class="material-icons">check</i>
                </div>
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true"><i class="material-icons">clear</i></span>
                </button>
                <b>Success:</b> Yuhuuu! Your Hadoop Map Reduce Cluster is ready.
                
            </div>
        </div>
        <br>
        <br>

		<a href="http://192.168.43.98:50070" class="btn btn-primary btn-lg">
	    <i class="material-icons">storage</i> Click here to manage Hadoop Cluster
	   	<div class="ripple-container"></div></a>
	   	<br>

		<a href="http://192.168.43.46:50030" class="btn btn-primary btn-lg">
	    <i class="material-icons">memory</i> Click here to manage Map Reduce Cluster
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