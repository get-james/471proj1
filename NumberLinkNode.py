class NumberLinkNode:
    h = 0
    g = 1
    head = []
    def __init__(self, state, parent, head, i, tail):
        self.state = state
        self.parent = parent
        self.head = head
        self.i = i
        self.tail = tail
    def __eq__(self, other):
        if self.state == other.state:
            return True


    def __str__(self):
        stringform = ""
        for y in range(len(self.state)):
            for x in range(len(self.state[y])):
                stringform += str(self.state[y][x]) + " "

            stringform += "\n"
        return stringform