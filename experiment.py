from os import subprocess
import sys

sizevalues = [1,2,4,8,16,32,64,128,256,512]
assocvalue = sys.argv[1]
tracefile = sys.argv[2]

print "B Set:"

for j in sizevalues:
    subprocess.run("python2", "simulator.py", "-s", str(j).join + "B", "-a", str(assocvalue), "-f", tracefile)

print "KB Set:"

for j in sizevalues:
    subprocess.run("python2", "simulator.py", "-s", str(j).join + "KB", "-a", str(assocvalue), "-f", tracefile)

print "MB Set:"

for j in sizevalues:
    subprocess.run("python2", "simulator.py", "-s", str(j).join + "MB", "-a", str(assocvalue), "-f", tracefile)
