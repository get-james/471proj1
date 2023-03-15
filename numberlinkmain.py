import NumberLinkOperations as operations
import NumberLinkNode
import PriorityQueue
initial_state = [[0,0,0,4,0,0,0],
                [0,3,0,0,2,5,0],
                [0,0,0,3,1,0,0],
                [0,0,0,5,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0],
                [2,0,0,0,4,0,0]]

initial_state2 =[[1,2,3,4,5,6,7],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [1,2,3,4,5,6,7]]
open_list = PriorityQueue.PriorityQueue()
closed_list = []
def listcheck(n):
    for x in open_list.queue:
        if n.state == x.state:
            return True
    for x in closed_list:
        if n.state == x.state:
            return True
    else:
        return False
def clistcheck(n):
    for x in closed_list:
        if n.state == x.state:
            return True
        else:
            return False
def state_generator(n):

    newNode = operations.path_up(n)
    if newNode is not None and newNode.i == 6:
        print("goal state found!!")
        print(newNode)
        goal_state_found()
    if newNode is not None and not listcheck(newNode):
        open_list.insert(newNode)
    newNode = operations.path_right(n)
    if newNode is not None and newNode.i == 6:
        print("goal state found!!")
        print(newNode)
        goal_state_found()
    if newNode is not None and not listcheck(newNode):
        open_list.insert(newNode)
    newNode = operations.path_left(n)
    if newNode is not None and newNode.i == 6:
        print("goal state found!!")
        print(newNode)
        goal_state_found()
    if newNode is not None and not listcheck(newNode):
        open_list.insert(newNode)
    newNode = operations.path_down(n)
    if newNode is not None and newNode.i == 6:
        print("goal state found!!")
        print(newNode)
        goal_state_found()
    if newNode is not None and not listcheck(newNode):
        open_list.insert(newNode)

def Astar_state_generator(n):

    newNode = operations.path_up(n)
    if newNode is not None and newNode.i == 6:
        print("goal state found!!")
        print(newNode)
        goal_state_found()
    if newNode is not None and not listcheck(newNode):
        newNode.g += n.g
        newNode.h += newNode.g
        open_list.insert(newNode)
    newNode = operations.path_right(n)
    if newNode is not None and newNode.i == 6:
        print("goal state found!!")
        print(newNode)
        goal_state_found()
    if newNode is not None and not listcheck(newNode):
        newNode.g += n.g
        newNode.h += newNode.g
        open_list.insert(newNode)
    newNode = operations.path_left(n)
    if newNode is not None and newNode.i == 6:
        print("goal state found!!")
        print(newNode)
        goal_state_found()
    if newNode is not None and not listcheck(newNode):
        newNode.g += n.g
        newNode.h += newNode.g
        open_list.insert(newNode)
    newNode = operations.path_down(n)
    if newNode is not None and newNode.i == 6:
        print("goal state found!!")
        print(newNode)
        goal_state_found()
    if newNode is not None and not listcheck(newNode):
        newNode.g += n.g
        newNode.h += newNode.g
        open_list.insert(newNode)
def search():
    while open_list:
        n = open_list.delete()
        closed_list.append(n)
        state_generator(n)
        #Astar_state_generator(n)
    print("done")



def go():
    head = operations.find_head(initial_state, 1)
    endpoint = operations.find_endpoint(initial_state, 1)
    startNode = NumberLinkNode.NumberLinkNode(initial_state, None, head, 1, head, endpoint)
    ih = operations.all_manhattan_distance(startNode)
    startNode.ih = ih
    startNode.h = ih
    open_list.insert(startNode)
    search()

def goal_state_found():
    print(len(closed_list))
    quit()
if __name__ == '__main__':
    go()

