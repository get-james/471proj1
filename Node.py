class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.h = 0

    def __eq__(self, other):
        if self.state == other.state:
            return True


    def set_h(self, heuristic):
        h = heuristic
