#!/usr/bin/python36
import cgi
import cookie
import subprocess as sp


def show_body_content():
	print('''
		<div class="section">
		      <div class="container text-center">
		        <div class="row">
		          <div class="col-md-8 ml-auto mr-auto text-center">
		            <div class="card card-nav-tabs text-center">
		              <div class="card-header card-header-primary">
		                Setup Hadoop Cluster
		              </div>
		            <div class="card-body">
		            	<br>
						<form action='hadoop.py'>
							<div class="form-group">
							    <label for="username">Name</label>
							    <input type="text" class="form-control" id="username" name='name'>
							 </div>
							  <div class="form-group">
							    <label for="size">Size of Cluster in GB</label>
							    <input type="text" class="form-control" id="size" name='size' placeholder="2G">
							  </div>
							<button type="submit" class="btn btn-primary">Submit</button>
						</form> 


		            </div>
				  </div>
		        </div>
		      </div>
		    </div>
		  </div>
		





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