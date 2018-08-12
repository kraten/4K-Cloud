#!/usr/bin/python36
import subprocess as sp
import cgi


def show_body_content():
	do_python_stuff()


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


def do_python_stuff():
	form=cgi.FieldStorage()
	size=form.getvalue('s')
	uname=form.getvalue('u')

	status = sp.getstatusoutput("cd ansible && sudo ansible-playbook -e 's={} u={}' ./playbooks/staas.yml".format(size,uname))
	print("<br>")
	
	if status[0] == 0 :
		print('''
		<div class="alert alert-success">
            <div class="container">
                <div class="alert-icon">
                    <i class="material-icons">check</i>
                </div>
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true"><i class="material-icons">clear</i></span>
                </button>''' + 
                "<b>Success:</b> Yuhuuu! You've got {} GB of cloud storage!".format(size) +
                '''
            </div>
        </div>
		''')

		#print(status[1])
		print("<br>")

		f = open('../html/downloads/4k_drive.bat', 'w')
		batch_commands = 'DISM /online /enable-feature /featurename:ServicesForNFS-ClientOnly\nDISM /online /enable-feature /featurename:ClientForNFS-Infrastructure\nmount     \\\\192.168.43.98\\wshare\\{}     z:'.format(uname)
		f.write(batch_commands)
		f.close()

		print('''
		<a href="/downloads/4k_drive.bat" class="btn btn-primary btn-lg" download>
	    <i class="fa fa-windows"></i> Download 4K drive
	   	<div class="ripple-container"></div></a>
	   	''')
	else:
		print('''
		<div class="alert alert-danger">
            <div class="container">
                <div class="alert-icon">
                    <i class="material-icons">error_outline</i>
                </div>
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true"><i class="material-icons">clear</i></span>
                </button>''' + 
                "<b>Failed:</b> Oops! There are some problems we are facing right now.." +
                '''
            </div>
        </div>
		''')

def main():
	print_headers()
	show_start_content()
	show_body_content()
	show_end_content()


main()