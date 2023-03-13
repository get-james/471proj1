import NumberLinkOperations as operations
import NumberLinkNode
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
open_list = []
closed_list = []
def state_generator(n):
    newNode = operations.path_up(n)
    if newNode is not None:
        open_list.append(newNode)
    newNode = operations.path_right(n)
    if newNode is not None:
        open_list.append(newNode)
    newNode = operations.path_left(n)
    if newNode is not None:
        open_list.append(newNode)
    newNode = operations.path_down(n)
    if newNode is not None:
        open_list.append(newNode)
def search():
    while open_list:
        n = open_list.pop()
        closed_list.append(n)
        state_generator(n)
    print("done")



def go():
    head = operations.find_head(initial_state2, 1)
    startNode = NumberLinkNode.NumberLinkNode(initial_state2, None, head, 1, head)
    open_list.append(startNode)
    search()

if __name__ == '__main__':
    go()