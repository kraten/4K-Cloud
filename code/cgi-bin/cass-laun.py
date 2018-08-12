#!/usr/bin/python36

import  cgi
import subprocess as sp

print("content-type: text/html")
print("")

form = cgi.FieldStorage()
cname = form.getvalue('cname')
imgname = form.getvalue('imgname')

#print(cname , imgname)

docker_launch_output = sp.getstatusoutput("sudo docker run -dit --name  {c} {i}".format(c=cname, i=imgname))

if docker_launch_output[0]  == 0:
	print("Container {c} launched successfully..".format(c=cname))
	print("Redirecting to docker manager..")
	print("<script>window.location = 'container_manager.py';</script>")
else:
	
	print("container named {c} failed ..".format(c=cname))






