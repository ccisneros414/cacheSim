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
        self._tag_bits = 0;
        self._set_bits = int(math.log(self._setCount+1,2))

    

    def checkBlock(self, strAddr):
		#global misses
		#global hits
        # checkBlock checks for the given address in the cache.
        # Returns true if it finds the block, false if it does not
		tag = self.pullTag(strAddr)
		setNum = self.pullSet(strAddr)
                #print setNum
		set = self._lines[setNum]
		#print "new set:"
		for i in set:
			iTag = i.tag
			#print "iTag =", iTag, "tag =", tag, "i.valid =", i.valid
			if iTag == tag and i.valid == 1:
                #print iTag, tag
				#update LRU order
				self.adjustLRU(setNum, i)
				return True	
		newLine = Line()
		newLine.address = strAddr
		newLine.valid = 1
		newLine.dirty = 0
		newLine.tag = tag
		self._lines[setNum].appendleft(newLine) # Add it to our cache.
		return False
    def checkBlockWrite(self, strAddr):
		# checkBlockWrite handles the case where we need to write to
		tag = self.pullTag(strAddr)
		setNum = self.pullSet(strAddr)
		set = self._lines[setNum]
		for i in set:
			iTag = i.tag
			if iTag == tag and i.valid ==1:
			#update LRU order
				i.dirty = 1
				self.adjustLRU(setNum,i)
				return True
		newLine = Line()
		newLine.address = strAddr
		newLine.valid = 1
		newLine.dirty = 1
		newLine.tag = tag
		self._lines[setNum].appendleft(newLine)
		return False

    def pullSet(self, addr):
        # Gets the set in our cache based on address given
        # Returns index of address' set
        length = len(addr) * 4
        bAddr = bin(int(addr,16))
        bitStr = bAddr[2:].zfill(length)
        bitStr = ''.join(bitStr[i:i+4] for i in range(0,length, 4))
        bitStr = str(bitStr)
        bitStr = bitStr[self._tag_bits:self._tag_bits+self._set_bits]
        return int(bitStr,2)

    def setTag(self, addr):
        bitLen = len(addr)
        bitLen *= 4
        bitLen -= self._set_bits
        bitLen -= 6
        self._tag_bits = bitLen

    def pullTag(self, addr):
		# Gets the tag in our cache based on address given
		# returns tag
        length = len(addr) * 4
        bAddr = bin(int(addr,16))
        bitStr = bAddr[2:].zfill(length)
        bitStr = ''.join(bitStr[i:i+4] for i in range(0,length, 4))
        bitStr = str(bitStr)
        bitStr = bitStr[:self._tag_bits]
        return bitStr

    def adjustLRU(self, index, value):
		# Removes found block from deque and puts it on top
		self._lines[index].remove(value)
		self._lines[index].appendleft(value)
		

