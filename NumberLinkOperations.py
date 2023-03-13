import PathNode
import NumberLinkNode
def path_down(n):
    if n.head[0] < 7 and n.state[n.head[0] + 1][n.head[1]] == 0:
        successor = list(n.state)
        next_head = list(n.head)
        next_head[0] = n.head[0]+1
        successor[n.head[0] + 1] [n.head[1]] = PathNode.PathNode(n.i)
        return NumberLinkNode.NumberLinkNode(successor, n, next_head, n.i)
    if n.head[0] > 0 and n.state[n.head[0] + 1][n.head[1]] == n.i:
        successor = list(n.state)
        i = n.i + 1
        if i == 8:
            print("goal state found")
            print(n)
            return
        head = find_head(successor,i)
        return NumberLinkNode.NumberLinkNode(successor, n, head, i)

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
