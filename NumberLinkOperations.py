import PathNode
import NumberLinkNode
import copy

def path_up(n):
    next_head = copy.deepcopy(n.head)
    next_head[0] = n.head[0] - 1
    if n.head[0] > 0 and n.state[n.head[0] - 1][n.head[1]] == 0:#making sure there's no path node in the way
        successor = copy.deepcopy(n.state)
        successor[n.head[0] - 1] [n.head[1]] = PathNode.PathNode(n.i)
        newNode = NumberLinkNode.NumberLinkNode(successor, n, next_head, n.i, n.tail, n.endpoint, n.ih)
        h = manhattan_distance(newNode)
        newNode.h += h
        return newNode
    if n.head[0] > 0 and next_head != n.tail and n.state[n.head[0] -1 ][n.head[1]] == n.i:
        successor = copy.deepcopy(n.state)
        i = n.i + 1
        if i == 6:
            n.i = 6
            return n
            #quit()
        head = find_head(successor,i)
        ep = find_endpoint(successor, i)

        newNode = NumberLinkNode.NumberLinkNode(successor, n, head, i, head, ep)
        ih = all_manhattan_distance(newNode)
        h = manhattan_distance(newNode)
        newNode.ih = ih #when a subgoal is found, ih is recalculated so we have the h value for all other i except the new current i
        newNode.h = h + ih
        return newNode


def path_right(n):
    next_head = copy.deepcopy(n.head)
    next_head[1] = n.head[1] + 1
    if n.head[1] < 6 and n.state[n.head[0]][n.head[1]+1] == 0:
        successor = copy.deepcopy(n.state)
        successor[n.head[0]] [n.head[1]+1] = PathNode.PathNode(n.i)
        newNode = NumberLinkNode.NumberLinkNode(successor, n, next_head, n.i, n.tail, n.endpoint, n.ih)
        h = manhattan_distance(newNode)
        newNode.h += h
        return newNode
    if n.head[1] < 6 and next_head != n.tail and n.state[n.head[0]][n.head[1]+1] == n.i:
        successor = copy.deepcopy(n.state)
        i = n.i + 1
        if i == 6:
            n.i = 6
            return n
        head = find_head(successor,i)
        ep = find_endpoint(successor, i)
        newNode = NumberLinkNode.NumberLinkNode(successor, n, head, i, head, ep)
        ih = all_manhattan_distance(newNode)
        h = manhattan_distance(newNode)
        newNode.ih = ih  # when a subgoal is found, ih is recalculated so we have the h value for all other i except the new current i
        newNode.h = h + ih
        return newNode


def path_left(n):
    next_head = copy.deepcopy(n.head)
    next_head[1] = n.head[1] - 1
    if n.head[1] > 0 and n.state[n.head[0]][n.head[1]-1] == 0:
        successor = copy.deepcopy(n.state)
        successor[n.head[0]] [n.head[1]-1] = PathNode.PathNode(n.i)
        newNode = NumberLinkNode.NumberLinkNode(successor, n, next_head, n.i, n.tail, n.endpoint, n.ih)
        h = manhattan_distance(newNode)
        newNode.h += h
        return newNode
    if n.head[1] > 0 and next_head != n.tail and n.state[n.head[0]][n.head[1]-1] == n.i:
        successor = copy.deepcopy(n.state)
        i = n.i + 1
        if i == 6:
            n.i = 6
            return n
           # quit()
        head = find_head(successor, i)
        ep = find_endpoint(successor, i)
        newNode = NumberLinkNode.NumberLinkNode(successor, n, head, i, head, ep)
        h = manhattan_distance(newNode)
        ih = all_manhattan_distance(newNode)
        newNode.ih = ih  # when a subgoal is found, ih is recalculated so we have the h value for all other i except the new current i
        newNode.h = h + ih

        return newNode

def path_down(n):
    next_head = copy.deepcopy(n.head)
    next_head[0] = n.head[0] + 1
    if n.head[0] < 6 and n.state[n.head[0] + 1][n.head[1]] == 0:
        successor = copy.deepcopy(n.state)
        successor[n.head[0] + 1] [n.head[1]] = PathNode.PathNode(n.i)
        newNode = NumberLinkNode.NumberLinkNode(successor, n, next_head, n.i, n.tail, n.endpoint, n.ih)
        h = manhattan_distance(newNode)
        newNode.h += h
        return newNode
    if n.head[0] < 6 and next_head != n.tail and n.state[n.head[0] + 1][n.head[1]] == n.i:
        successor = copy.deepcopy(n.state)
        i = n.i + 1
        if i == 6:
            n.i = 6
            return n
          #  quit()
        head = find_head(successor, i)
        ep = find_endpoint(successor, i)
        newNode = NumberLinkNode.NumberLinkNode(successor, n, head, i, head, ep)
        h = manhattan_distance(newNode)
        ih = all_manhattan_distance(newNode)
        newNode.ih = ih  # when a subgoal is found, ih is recalculated so we have the h value for all other i except the new current i
        newNode.h = h + ih

        return newNode


# finds first index of starting number
def find_head(state, i):
    head = [-1,-1]
    for y in range(len(state)):
        try:
            if state[y].index(i) != None:
                head[0] = y
                head[1] = state[y].index(i)
                return head
        except ValueError:
            continue

# finds second occurrence of number in the state
def find_endpoint(state, i):
    endpoint = [-1,-1]
    count = 0
    for y in range(len(state)):
        try:
            if state[y].index(i) != None and count == 1:
                endpoint[0] = y
                endpoint[1] = state[y].index(i)
                return endpoint
            if state[y].index(i) != None and count == 0:
                count = count + 1
        except ValueError:
            continue

def manhattan_distance(n):
    h = abs(n.head[0] - n.endpoint[0])
    h += abs(n.head[1] - n.endpoint[1])
    return h

def all_manhattan_distance(n):
    i = n.i +1
    h = 0
    while i < 6:
        head = find_head(n.state, i)
        endpoint = find_endpoint(n.state, i)
        h += abs(head[0] - endpoint[0])
        h += abs(head[1] - endpoint[1])
        i += 1
    return h


