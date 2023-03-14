
class NumberLinkNode:
    h = 0
    g = 0
    head = []
    endpoint = []

    def __init__(self, state, parent, head, i, tail, endpoint, ih=0):
        self.state = state
        self.parent = parent
        self.head = head
        self.i = i
        self.tail = tail
        self.endpoint = endpoint
        self.h = ih #inherited heuristic. base heuristic for that i. so we don't need to calculate the overall manhattan distance every time
        self.ih = ih

    def __eq__(self, other):
        if self.state == other.state:
            return True
        else:
            return False


    def __str__(self):
        stringform = ""
        for y in range(len(self.state)):
            for x in range(len(self.state[y])):
                stringform += str(self.state[y][x]) + " "

            stringform += "\n"
        return stringform