#!/usr/bin/python36
import sys
count=0
for i in sys.stdin:
       j=i.split("-")
       count=count+int(j[1])

print("Number of dowry cases reported:{}".format(count))  
