class NumberLinkNode:
    h = 0
    g = 1
    head = []
    def __init__(self, state, parent, head, i):
        self.state = state
        self.parent = parent
        self.head = head
        self.i = i

    def __eq__(self, other):
        if self.state == other.state:
            return True
