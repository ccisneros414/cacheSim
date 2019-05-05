class Line:

    # Class for line in cache

    def __init__(self):
        self.valid = 0
        self.tag = 0
        self.data = [0] * 64
        self.recentPos = 0
