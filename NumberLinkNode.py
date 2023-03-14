
class NumberLinkNode:
    h = 0
    g = 0
    head = []
    endpoint = []
# state is the 2d board, parent is the Node with the preceding state, head is the head of the path, tail is the
    #point of origin of the path, i is the current number were trying to find the path between, endpoint is the second
    #occurence of the number in the board, ih is the inherited heuristic. it's the manhattan value for all the other
    #numbers other than the current i.
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