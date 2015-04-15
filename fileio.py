#!/usr/bin/python

import os.path
import subprocess
import sys

print(sys.platform)
proc = subprocess.Popen(["pwd"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
out = out.rstrip() 
str = raw_input("Enter input file path:")
if not os.path.exists(out + "/" + str):
    print "File ", out + "/" + str, " does not exist. Exiting..."
    exit()
print "Reading ", str , ".....\n\n\n", "###Start File"
file = open(str,'r',0)
lines = file.read()
file.close()
print lines, "###End File"
