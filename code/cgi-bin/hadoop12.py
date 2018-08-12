#!/usr/bin/python36
import os
import cgi
import subprocess
print("content-type: text/html")
print("")
ipj="192.168.43.46"
ipn="192.168.43.98"
print("Setting up map-reduce cluster...")
subprocess.getoutput("cd ansible && sudo ansible-playbook ./playbooks/mr.yml --extra-vars='ipj={0} , ipn={1}'".format(ipj,ipn))
print("Success! Redirecting to Hadoop Cluster Manager webpage..") 
print("""
	<script>window.location = "hadoop_manager.py";</script>
	""")

