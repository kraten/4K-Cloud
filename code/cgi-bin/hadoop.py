#!/usr/bin/python36
import os
import cgi
import subprocess
print("content-type: text/html")
print("")
ip="192.168.43.98"
ipj="192.168.43.46"
ipn="192.168.43.98"
form=cgi.FieldStorage()
name=form.getvalue('name')
size=form.getvalue('size')
print("Configuring...<br>")
#os.system('sudo ansible-playbook ansilvm2.yml --extra-vars="s={0} , n={1}"'.format(size,name))
subprocess.getoutput("cd ansible && sudo ansible-playbook ./playbooks/ansi_hadoop.yml --extra-vars='ip={}'".format(ip))
print("<a href='hadoop11.py'>Starting Services...</a>")
#subprocess.getoutput("sudo ansible-playbook ansi_hadoopService.yml")
#subprocess.getoutput("sudo ansible-playbook mr.yml --extra-vars='ipj={0} , ipn={1}'".format(ipj,ipn))
#print("successfully run") 

print("""
	<script>window.location = "hadoop11.py";</script>
	""")

