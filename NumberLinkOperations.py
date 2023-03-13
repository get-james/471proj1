import PathNode
import NumberLinkNode
import copy

def path_up(n):
    next_head = copy.deepcopy(n.head)
    next_head[0] = n.head[0] - 1
    if n.head[0] > 0 and n.state[n.head[0] - 1][n.head[1]] == 0:
        successor = copy.deepcopy(n.state)
        successor[n.head[0] - 1] [n.head[1]] = PathNode.PathNode(n.i)
        return NumberLinkNode.NumberLinkNode(successor, n, next_head, n.i, n.tail)
    if n.head[0] > 0 and next_head != n.tail and n.state[n.head[0] -1 ][n.head[1]] == n.i:
        successor = copy.deepcopy(n.state)
        i = n.i + 1
        if i == 8:
            print("goal state found")
            print(n)
            return
        head = find_head(successor,i)
        newNode = NumberLinkNode.NumberLinkNode(successor, n, head, i, head)

        return newNode


def path_right(n):
    next_head = copy.deepcopy(n.head)
    next_head[1] = n.head[1] + 1
    if n.head[1] < 6 and n.state[n.head[0]][n.head[1]+1] == 0:
        successor = copy.deepcopy(n.state)
        successor[n.head[0]] [n.head[1]+1] = PathNode.PathNode(n.i)
        return NumberLinkNode.NumberLinkNode(successor, n, next_head, n.i, n.tail)
    if n.head[1] < 6 and next_head != n.tail and n.state[n.head[0]][n.head[1]+1] == n.i:
        successor = copy.deepcopy(n.state)
        i = n.i + 1
        if i == 8:
            print("goal state found")
            print(n)
            return
        head = find_head(successor,i)
        newNode = NumberLinkNode.NumberLinkNode(successor, n, head, i, head)
        return newNode


def path_left(n):
    next_head = copy.deepcopy(n.head)
    next_head[1] = n.head[1] - 1
    if n.head[1] > 0 and n.state[n.head[0]][n.head[1]-1] == 0:
        successor = copy.deepcopy(n.state)
        successor[n.head[0]] [n.head[1]-1] = PathNode.PathNode(n.i)
        return NumberLinkNode.NumberLinkNode(successor, n, next_head, n.i, n.tail)
    if n.head[1] > 0 and next_head != n.tail and n.state[n.head[0]][n.head[1]-1] == n.i:
        successor = copy.deepcopy(n.state)
        i = n.i + 1
        if i == 8:
            print("goal state found")
            print(n)
            return
        head = find_head(successor,i)
        newNode = NumberLinkNode.NumberLinkNode(successor, n, head, i, head)

        return newNode

def path_down(n):
    next_head = copy.deepcopy(n.head)
    next_head[0] = n.head[0] + 1
    if n.head[0] < 6 and n.state[n.head[0] + 1][n.head[1]] == 0:
        successor = copy.deepcopy(n.state)
        successor[n.head[0] + 1] [n.head[1]] = PathNode.PathNode(n.i)
        return NumberLinkNode.NumberLinkNode(successor, n, next_head, n.i, n.tail)
    if n.head[0] < 6 and next_head != n.tail and n.state[n.head[0] + 1][n.head[1]] == n.i:
        successor = copy.deepcopy(n.state)
        i = n.i + 1
        if i == 8:
            print("goal state found")
            print(n)
            return
        head = find_head(successor,i)
        newNode = NumberLinkNode.NumberLinkNode(successor, n, head, i, head)
        newNode.tail = head
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
