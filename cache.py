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

        self._set_bits = log(self._size // self._assoc_pol, 2)
        self._tag_bits = 8

    def checkBlock(addr):
        # checkBlock checks for the given address in the cache.
        # Returns true if it finds the block, false if it does not

        tag = addr >> self._tag_bits
        set = addr >> self._set_bits 


