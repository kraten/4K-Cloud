#!/usr/bin/python36
import sys
 
for i in sys.stdin:
         j=i.split(",")
         if j[0]=='Rajasthan':
           print(j[1]+"-"+j[5]),
