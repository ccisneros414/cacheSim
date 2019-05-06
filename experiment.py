import sys
import subprocess

sizevalues = [1,2,4,8,16,32,64,128,256,512]
assocvalue = sys.argv[1]
tracefile = sys.argv[2]

print ("B Set:")

for j in sizevalues:
    subprocess.call(["python2", "simulator.py", "-s", str(j) + "B", "-a", str(assocvalue), "-f", tracefile])

print ("KB Set:")

for j in sizevalues:
    subprocess.call(["python2", "simulator.py", "-s", str(j) + "KB", "-a", str(assocvalue), "-f", tracefile])

print ("MB Set:")

for j in sizevalues:
    subprocess.call(["python2", "simulator.py", "-s", str(j) + "MB", "-a", str(assocvalue), "-f", tracefile])
