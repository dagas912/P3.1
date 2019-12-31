from Heuristic import heuristic
import queue
import time

def a_star(root):
    start_time = time.time()
    open = queue.PriorityQueue()
    open_put=open.put
    open_get=open.get
    open_empty=open.empty
    generated = 1
    open_put((0,generated,root))
    expanded = 0
    explored = dict()
    while not open_empty() :
        node = open_get()[2]
        if node.__hash__() not in explored:
            if node.testgoal():
                total_time = time.time() - start_time
                return [expanded,node.cost]
            sucessors = node.expand()
            expanded += 1
            for suc in sucessors:
                open_put((suc.cost + heuristic(suc), generated,suc))
                generated += 1
            explored[node.__hash__()] = node.state
    return [-1,-1]
