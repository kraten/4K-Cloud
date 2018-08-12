#!/usr/bin/python36

import subprocess as sp

print("content-type: text/html")
print("")
print("""
<head>
      <title>Docker Manager</title>
      <meta http-equiv = "refresh" content ="3"/>
</head>
""")

#print("<iframe name='cframe' width='100%' height='25%'>container console</iframe>")

list = sp.getoutput("sudo docker ps -a")
flist = list.split("\n")

print("<table align='center' width='90%' border='1'>")

print("""
<tr>
<th>Status</th>
<th>Image Name</th>
<th>Container Name</th>
<th>CPU-Use</th>
<th>RAM</th>
<th>Net-Use</th>
<th>start</th>
<th>stop</th>
<th>Console</th>
</tr>
""")

for i in flist[1:]:
	j = i.split()
	print("<tr>")
	print("<td>")
	if "Exited" in i:
		print("down")
	elif "Up" in i:
		print("up")
	else:
		print("unknown")
	print("</td>")

	print("<td>")
	print(j[1])
	print("</td>")

	print("<td>")
	print(j[-1])
	print("</td>")

	print("<td>")
	stat_cmd = "sudo docker stats {} --no-stream".format(j[-1])
	stat_cmd += "| tail -n 1 | awk '{print $3} {print $4} {print $6} {print $7}'"
	o = sp.getoutput(stat_cmd)
	o=o.split("\n")
		
	print(o[0])
	print("</td>")


	print("<td>")
	print(o[1])
	print("</td>")

	print("<td>")
	print(o[3])
	print("</td>")

	print("<td>")
	print("<a href='doc-start.py?x={}'>start</a>".format(j[-1]))
	print("</td>")

	print("<td>")
	print("<a href='doc-stop.py?x={}'>stop</a>".format(j[-1]))
	print("</td>")


	print("<td>")
	print("<a target='cframe' href='http://192.168.43.19:4200'>console</a>")
	print("</td>")


	print("</tr>")


print("</table>")

print("<h4>Allowed RAM for This Demo ==>> 600MB </h4>")
