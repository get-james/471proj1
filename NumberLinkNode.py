class NumberLinkNode:
    h = 0
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent


    def __eq__(self, other):
        if self.state == other.state:
            return True
