import math
import collections
from line import Line

class Cache:
    
    # Class for cache 

    def __init__(self, size, block_size, assoc_pol):
        self._size = int(size)
        self._block_size = int(block_size)
        self._assoc_pol = int(assoc_pol)
        # Declare lines in cache
        self._lines = []
        for i in range(size // (self._block_size * self._assoc_pol)):
			ourSet = collections.deque('', maxlen=self._assoc_pol)
			for j in range(self._assoc_pol):
				ourSet.append(Line());
			self._lines.append(ourSet)
        
        self._setCount = (self._size // (self._block_size * self._assoc_pol)) - 1 # Highest set index

        self._tag_bits = int(math.log(self._size // self._assoc_pol, 2))
        self._set_bits = 8

    

    def checkBlock(self, strAddr):
		#global misses
		#global hits
        # checkBlock checks for the given address in the cache.
        # Returns true if it finds the block, false if it does not
		addr = int(strAddr, 16)	
		tag = self.pullTag(addr)
		setNum = self.pullSet(addr)
		set = self._lines[setNum]
		#print "new set:"
		for i in set:
			iTag = i.tag
			#print "iTag =", iTag, "tag =", tag, "i.valid =", i.valid
			if iTag == tag and i.valid == 1 and i.address == addr:
				#update LRU order
				if i.stale == 1:
					i.stale=0 # Adjust stale flag; Write fresh data to memory
				self.adjustLRU(setNum, i)
				return True	
		newLine = Line()
		newLine.address = addr
		newLine.valid = 1
		newLine.tag = tag
		self._lines[setNum].appendleft(newLine) # Add it to our cache.
		return False
	#def writeBlock(self, addr):
	# writeBlock handles the case where we need to write to
    def pullSet(self, addr):
        # Gets the set in our cache based on address given
        # Returns index of address' set
		return (addr >> self._set_bits) & self._setCount # Get the set bits of the address
        
    def pullTag(self, addr):
		# Gets the tag in our cache based on address given
		# returns tag	
		return addr >> self._tag_bits

    def adjustLRU(self, index, value):
		# Removes found block from deque and puts it on top
		self._lines[index].remove(value)
		self._lines[index].appendleft(value)
		

