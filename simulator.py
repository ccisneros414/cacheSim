import argparse
import sys
import math
import logging
import gzip
import collections
from cache import Cache
from line import Line

######## constants ##############
cache_line_size = 64
offset_bits = int(math.log(64, 2))

######## user interface #########
parser = argparse.ArgumentParser(description='Cache Simulator.')
parser.add_argument('-s', '--size', metavar='N', type=str, dest='size',
		help='the size of the cache in B, KB or MB', required=True)
parser.add_argument('-a', '--assoc', dest='assoc', type=int, metavar='s',
		help='the set associativity of the cache or 0 for full associativity', required=True)
parser.add_argument('-f', '--file', metavar='FILENAME', type=str, dest='file',
		help="name of the input memory trace file; if the file is "
		"in gzip format, the file name must end with .gz",
		required=True)
parser.add_argument('--debug', dest='debug', action='store_const',
		const=True, default=False,
		help='enable debugging logs')
parser.add_argument('--print', dest='enable_print', action='store_const',
		const=True, default=False,
		help='enable cache content output')
args = parser.parse_args()
if args.debug:
	logging.basicConfig(level=logging.DEBUG)



######## helper functions ########

# parse the user-input size string, returns the size in bytes
def parse_size(size):
	try:
		if size.endswith('KB'): 
			s = int(size[:-2]) * 1024
		elif size.endswith('MB'):
			s = int(size[:-2]) * 1024 * 1024
		elif size.endswith('B'):
			s = int(size[:-1])
		else: # just the integer
			s = int(size);
	except ValueError:
		print("Invalid cache size")
		sys.exit(1)
	return s

#read from file
if ".gz" in args.file:
	f = gzip.open(args.file,"r")
else:
	f = open(args.file,"r")

assoc = int(args.assoc)
cacheSize = parse_size(args.size)
cacheList = collections.deque([], maxlen=(cacheSize // cache_line_size))

if assoc != 0:
	cache = Cache(cacheSize, cache_line_size, assoc)
elif assc == 0 or assoc >= (cacheSize //cache_line_size):
	for i in range(cacheSize//cache_line_size):
		cacheList.append(Line())

total = 0
i=0
blockSize = 0 
misses = 0
hits = 0
hmFlag = 0
for line in f:
	sepLine = line.split()
	if len(sepLine) != 3:continue
	sepLine[0] = sepLine[0][:-1]
<<<<<<< HEAD
	sepLine[2] = sepLine[2].strip("\n")
	cache.setTag(sepLine[2])
	newLine = Line()
	newLine.address = sepLine[2]	
=======
        sepLine[2] = sepLine[2].strip("\n")
	cache.setTag(sepLine[2])
        #print(sepLine)
>>>>>>> 12b98770aa2f29481d970ff7b7181de9ee199da0
	total+=1
	if sepLine[1] == "R":
		if assoc == 0 or assoc >= (cacheSize // cache_line_size) : # Full associative
			hmFlag = 0
			for l in cacheList:
				if newLine.address == l.address and l.valid == 1:
					cacheList.remove(l)
					newLine.valid == 1
					cacheList.appendleft(newLine)
					hmFlag = 1
					break
			if(hmFlag == 1):
				hits += 1
			else:
				#never found match
				misses +=1
				newLine.valid == 1
				newLine.dirty == 0
				cacheList.appendLeft(newLine)
		elif assoc >= 1: # N-Way associative
			if cache.checkBlock(sepLine[2]):
				hits += 1
			else:
				misses += 1
	else:
		if assoc == 0 or assoc >= (cacheSize // cache_line_size):
			hmFlag = 0
			for l in cacheList:
				if newLine.address == l.address and l.valid==1:
					cacheList.remove(l)
					newLine.valid == 1
					newLine.dirty == 1
					cacheList.appendleft(newLine)
					hmFlag = 1
					break
			if(hmFlag == 1):
				hits +=1
			else:
				misses +=1
				newLine.valid == 1
				newLine.dirty == 1
				cacheList.appendLeft(newLine)
		elif assoc>=1:# N-Way assoc
			if cache.checkBlockWrite(sepLine[2]):
				hits += 1
			else:
				misses += 1
		


<<<<<<< HEAD
print misses, total
print "Cache miss rate: ",round((float(misses)/float(total)*100),2),"% "
=======
#for c in cacheList:
#	print(c)
print misses, total
print "Cache miss rate: ",(float(misses)/float(total))*100,"% "
>>>>>>> 12b98770aa2f29481d970ff7b7181de9ee199da0

