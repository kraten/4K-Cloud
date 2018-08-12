#!/usr/bin/python36
import os
import cgi
import subprocess
print("content-type: text/html")
print("")
ip="192.168.43.98"
ipj="192.168.43.46"
ipn="192.168.43.98"

#os.system('sudo ansible-playbook ansilvm2.yml --extra-vars="s={0} , n={1}"'.format(size,name))
subprocess.getoutput("cd ansible && sudo ansible-playbook ./playbooks/ansi_hadoopService.yml")
print("<a href='hadoop12.py'>Starting Map-reduce Setup..</a>")
#subprocess.getoutput("sudo ansible-playbook mr.yml --extra-vars='ipj={0} , ipn={1}'".format(ipj,ipn))
#print("successfully run") 

print("""
	<script>window.location = "hadoop12.py";</script>
	""")

