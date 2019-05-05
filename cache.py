import math
from line import Line

class Cache:
    
    # Class for cache 

    def __init__(self, size, block_size, assoc_pol):
        self._size = size
        self._block_size = block_size
        self._assoc_pol = assoc_pol
        
        # Declare lines in cache
        self._lines = [Line(block_size) for i in range(size // block_size)]
        self._setCount = (self._size // (self._block_size * self._assoc_pol)) - 1 # Highest set index

        self._set_bits = log(self._size // self._assoc_pol, 2)
        self._tag_bits = 8

    

    def checkBlock(self, set):
        # checkBlock checks for the given address in the cache.
        # Returns true if it finds the block, false if it does not

        tag = addr >> self._tag_bits
        set = self._pullSet(addr)

        for i in set:
            iTag = i >> self._tag_bits
            if iTag == tag and i.valid == 1:
                return true
        return false



    def pullSet(self, addr):
        # Gets the set in our cache based on address given
        # Returns list

        setBits = (addr >> self._set_bits) & self._setCount # Get the set bits of the address
        toReturn = setBits * self._assoc_pol # Get the index in the line array of the first member of set
        return self._lines[toReturn:toReturn + self._assoc_pol] # Return parts of line array that address is a member of

   def adjustLRU(self, set, index):
        set[index].recentPos = self._assoc_pol
        for line in set:
            if line is not set[index] and 
