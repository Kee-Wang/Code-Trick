#!/usr/bin/env python
import subprocess
import os
import shlex
def cl(command):
    #ip::string, command line as string input
    #op::string, return value is the output of command line
    #Notice, each time when change directly, cl starts from currect directory.
    #Use three \' if you want to input multiple line
    arg = shlex.split(command)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    return output


#Test
p = cl('''
mkdir test
cd test
echo 'this is test' >> test.txt
echo 'this is second line' >> test.txt
head -n 2 test.txt | tail -n 1
echo 'end of test'
''')
print (p)
