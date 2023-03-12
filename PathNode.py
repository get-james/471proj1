class PathNode:


    def __init__(self, pathnumber):
        self.pathnumber = pathnumber

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
