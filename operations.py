
#creates a new list with succesor state and returns it


def shift_left(state):
    if state == None or state.index(0) % 3 == 0:  #if blank is on left side return none
        return None
    else:
        successor = list(state)
        tempindex = successor.index(0)
        successor = swap(successor, tempindex-1, tempindex)
        return successor


def shift_down(state):
    if state == None or state.index(0) > 5 :
        return None
    else:
        successor = list(state)
        successor = swap(successor, successor.index(0)+3, successor.index(0))
        return successor


def shift_up(state):
    if state == None or state.index(0) < 3:
        return None
    else:
        successor = list(state)
        successor = swap(successor, successor.index(0) - 3, successor.index(0))
        return successor

def shift_right(state):
    if state == None or state.index(0) % 3 == 2:  #if blank is on right side return none
        return None
    else:
        successor = list(state)
        successor = swap(successor, successor.index(0)+1, successor.index(0))
        return successor

def swap(positionlist, index1, index2):
    placeholder = positionlist[index1]
    positionlist[index1] = positionlist[index2]
    positionlist[index2] = placeholder
    return positionlist


