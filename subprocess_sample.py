#!/usr/bin/env python
#This code shows how to interact with terminal.
#Noticed the first line makes python code an excutable, of course that is after chmode +x name.py. Then, instead of python name.py every #time, now need to do ./name.py


#Use subprocess to interact with terminal
import subprocess

p = subprocess.Popen("head -n 8 basis.f90 | tail -n 1", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
print "The 8th line is  \n", output
