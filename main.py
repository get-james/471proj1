import operations
import Node
import PriorityQueue

goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
initialState = [2, 3, 6, 1, 4, 0, 7, 5, 8]
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
        h_heuristic(newNode)
        openlist.insert(newNode)
    newNode = Node.Node(operations.shift_up(n.state), n)
    check_for_goal_state(newNode)
    if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
        h_heuristic(newNode)
        openlist.insert(newNode)
    newNode = Node.Node(operations.shift_down(n.state), n)
    check_for_goal_state(newNode)
    if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
        h_heuristic(newNode)
        openlist.insert(newNode)
    newNode = Node.Node(operations.shift_right(n.state), n)
    check_for_goal_state(newNode)
    if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
        h_heuristic(newNode)
        openlist.insert(newNode)


def perform_manhattan_operations(n):
        newNode = Node.Node(operations.shift_left(n.state), n)
        check_for_goal_state(newNode)
        if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
            m_heuristic(newNode)
            openlist.insert(newNode)
        newNode = Node.Node(operations.shift_up(n.state), n)
        check_for_goal_state(newNode)
        if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
            m_heuristic(newNode)
            openlist.insert(newNode)
        newNode = Node.Node(operations.shift_down(n.state), n)
        check_for_goal_state(newNode)
        if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
            m_heuristic(newNode)
            openlist.insert(newNode)
        newNode = Node.Node(operations.shift_right(n.state), n)
        check_for_goal_state(newNode)
        if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
            m_heuristic(newNode)
            openlist.insert(newNode)


def perform_astar_operations(n):
    parent_h = n.h
    newNode = Node.Node(operations.shift_left(n.state), n)
    check_for_goal_state(newNode)
    if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
        m_heuristic(newNode)
        newh = newNode.h + parent_h
        newNode.h = newh
        openlist.insert(newNode)
    newNode = Node.Node(operations.shift_up(n.state), n)
    check_for_goal_state(newNode)
    if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
        m_heuristic(newNode)
        newh = newNode.h + parent_h
        newNode.h = newh
        openlist.insert(newNode)
    newNode = Node.Node(operations.shift_down(n.state), n)
    check_for_goal_state(newNode)
    if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
        m_heuristic(newNode)
        newh = newNode.h + parent_h
        newNode.h = newh
        openlist.insert(newNode)
    newNode = Node.Node(operations.shift_right(n.state), n)
    check_for_goal_state(newNode)
    if newNode.state != None and openlist.queue.count(newNode) < 1 and closedlist.count(newNode) < 1:
        m_heuristic(newNode)
        newh = newNode.h + parent_h
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
        quit()


def dfs_search():
    while(openlist):
        n = openlist.pop()
        #print(n.state)
        closedlist.append(n)
        perform_operations(n)


def bfs_search():
    while(openlist):
        n = openlist.pop(0)
        closedlist.append(n)
        perform_operations(n)

# calculates hamming distance of each node and attributes it to its heuristic attribute
def m_heuristic(n):
    h = 0
    for i in range(len(n.state)):
        if n.state[i] != 0:
            h += abs((n.state[i]-1)-i)
    n.h = h


def h_heuristic(n):
    h = 0
    for i in range(len(n.state)):
        if n.state[i] != 0:
            if n.state[i]-1 != i:
                h = h+1
    n.h = h



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

astar_search()
