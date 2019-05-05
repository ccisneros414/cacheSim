import argparse
import sys
import math
import logging
import gzip
import collections
from cache import Cache

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

cache = Cache(args.size, cache_line_size, assoc) 

######## helper functions ########

def replaceLRU(toCheck):
	if toCheck in cacheList:
		cacheList.remove(toCheck)
		cacheList.appendleft(toCheck)
	else:
		cacheList.appendleft(toCheck)

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
print("Start of Cache")
print(args.file)
f = open(args.file,"r")
assoc = args.assoc
cacheSize = parse_size(args.size)

cacheList = collections.deque([], maxlen=cacheSize)
hitCount = 0
missCount = 0
total = 0
i=0
blockSize = 0

'''
if assoc > 1:
	while i<:
		block = collections.deque([],maxlen=(cacheSize/assoc))
		cacheList.appendleft(block)
		i+=1
'''
for c in cacheList:
	print(c)

for line in f:
	sepLine = line.split()
	sepLine[0] = sepLine[0][:-1]
	#print(sepLine)
	total+=1
	
	if assoc == 0:
		if sepLine[2] in cacheList:
			#print("hit")
			cacheList.remove(sepLine[2])
			cacheList.appendleft(sepLine[2])
			hitCount+=1
			continue
		else:
			#print("miss")
			missCount +=1
			cacheList.appendleft(sepLine[2])

	#elif assoc > 1:
	#	print("set associativity")
	#elif assoc == 1:
	#	print("full associativity")


for c in cacheList:
	print(c)

print("Cache miss rate: ",(float(missCount)/float(total))," % ")

