import operations
import Node
import PriorityQueue

goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
initialState = [4, 1, 3, 7, 0, 5, 8, 2, 6]
startNode = Node.Node(initialState, None)
openlist = PriorityQueue.PriorityQueue()
openlist.insert(startNode)
goal_list = []
closedlist = []

# adds states to open list if they aren't already a part of the open or closed list.
def perform_operations(n):
    newNode = Node.Node(operations.shift_left(n.state), n)
    check_for_goal_state(newNode)
    if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
        p_heuristic(newNode)
        openlist.insert(newNode)
    newNode = Node.Node(operations.shift_up(n.state), n)
    check_for_goal_state(newNode)
    if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
        p_heuristic(newNode)
        openlist.insert(newNode)
    newNode = Node.Node(operations.shift_down(n.state), n)
    check_for_goal_state(newNode)
    if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
        p_heuristic(newNode)
        openlist.insert(newNode)
    newNode = Node.Node(operations.shift_right(n.state), n)
    check_for_goal_state(newNode)
    if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
        p_heuristic(newNode)
        openlist.insert(newNode)


def perform_manhattan_operations(n):
        newNode = Node.Node(operations.shift_left(n.state), n)
        check_for_goal_state(newNode)
        if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
            p_heuristic(newNode)
            openlist.insert(newNode)
        newNode = Node.Node(operations.shift_up(n.state), n)
        check_for_goal_state(newNode)
        if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
            p_heuristic(newNode)
            openlist.insert(newNode)
        newNode = Node.Node(operations.shift_down(n.state), n)
        check_for_goal_state(newNode)
        if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
            p_heuristic(newNode)
            openlist.insert(newNode)
        newNode = Node.Node(operations.shift_right(n.state), n)
        check_for_goal_state(newNode)
        if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
            p_heuristic(newNode)
            openlist.insert(newNode)


def perform_astar_operations(n):
    parent_g = n.g
    newNode = Node.Node(operations.shift_left(n.state), n)
    check_for_goal_state(newNode)
    if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
        p_heuristic(newNode)
        newNode.g = newNode.g + parent_g
        newh = newNode.h + newNode.g
        newNode.h = newh
        openlist.insert(newNode)
    newNode = Node.Node(operations.shift_up(n.state), n)
    check_for_goal_state(newNode)
    if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
        p_heuristic(newNode)
        newNode.g = newNode.g + parent_g
        newh = newNode.h + newNode.g
        newNode.h = newh
        openlist.insert(newNode)
    newNode = Node.Node(operations.shift_down(n.state), n)
    check_for_goal_state(newNode)
    if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
        p_heuristic(newNode)
        newNode.g = newNode.g + parent_g
        newh = newNode.h + newNode.g
        newNode.h = newh
        openlist.insert(newNode)
    newNode = Node.Node(operations.shift_right(n.state), n)
    check_for_goal_state(newNode)
    if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
        p_heuristic(newNode)
        newNode.g = newNode.g + parent_g
        newh = newNode.h + newNode.g
        newNode.h = newh
        openlist.insert(newNode)

# checks to see if node is goal state and if it is it adds all its ancestors to a list then outputs all the succesive states
def check_for_goal_state(n):
    if n.state == goalState:
        while n.parent:
            goal_list.append(n)
            n = n.parent
        goal_list.append(n)  #append initial state
        while goal_list:
            print(goal_list.pop().state)
        print("goal state found woohoo")
        print("closed list:")
        z=1
        while closedlist:
            print(z)
            print(closedlist.pop(0).state)
            z+=1
        quit()



# calculates manhattan distance of each node and attributes it to its heuristic attribute
def m_heuristic(n):
    h = 0
    for i in range(len(n.state)):
        if n.state[i] != 0:
            h += abs((n.state[i]-1)-i)
    n.h = h

#calculates hamming distance
def h_heuristic(n):
    h = 0
    for i in range(len(n.state)):
        if n.state[i] != 0:
            if n.state[i]-1 != i:
                h = h+1
    n.h = h

#permutation inversion
def p_heuristic(n):
    h = 0
    for i in range(len(n.state)):
        for j in range(i + 1, len(n.state)):
            if n.state[i] > n.state[j]:
                h += 1
    n.h = h
#   depth first search
def dfs_search():
    while(openlist):
        n = openlist.pop()
        #print(n.state)
        closedlist.append(n)
        perform_operations(n)


#   breadth first search
def bfs_search():
    while(openlist):
        n = openlist.pop(0)
        closedlist.append(n)
        perform_operations(n)


#   best first search
def bestfs():
    while(openlist.queue):
        n = openlist.delete()
        closedlist.append(n)
        perform_manhattan_operations(n)


def astar_search():
    while(openlist.queue):
        n = openlist.delete()
        closedlist.append(n)
        perform_astar_operations(n)

#astar_search()
bestfs()
#bfs_search()
#dfs_search()