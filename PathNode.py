class PathNode:

    # used to mark a point in the board with a path. has an integer attribute which denotes which path it is.
    def __init__(self, pathnumber):
        self.pathnumber = pathnumber




    def __str__(self):
        return str(self.pathnumber)