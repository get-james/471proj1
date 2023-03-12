import NumberLinkOperations as operations
import NumberLinkNode
initial_state = [[0,0,0,4,0,0,0],
                [0,3,0,0,2,5,0],
                [0,0,0,3,1,0,0],
                [0,0,0,5,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0],
                [2,0,0,0,4,0,0]]
open_list = []
closed_list = []
def state_generator(n):
    open_list.append(operations.path_up(n))


def search():
    while open_list:
        n = open_list.pop()
        closed_list.append(n)
        newNode = operations.path_down(n)
        if newNode is not None:
            open_list.append(newNode)
    print("done")



def main():
    head = operations.find_head(initial_state, 1)
    startNode = NumberLinkNode.NumberLinkNode(initial_state, None, head, 1)
    open_list.append(startNode)
    search()

if __name__ == '__main__':
    main()