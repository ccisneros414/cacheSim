class Line:

    # Class for line in cache

    def __init__(self):
        self.valid = 0
        self.tag = bin(-1)
        self.address = 0
        self.dirty = 0
