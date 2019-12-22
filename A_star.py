from TestGoal import *
from RecoverPath import *
from Heuristic import *
from Expand2 import *
import queue
import time

def a_star(root):
    start_time = time.time()
    open = queue.PriorityQueue()
    generated = 1
    open.put((0,generated,root))
    expanded = 0
    explored = dict()
    while not open.empty() :
        node = open.get()[2]
        if node.__hash__() not in explored:
            if node.testgoal():
                #(node)
                total_time = time.time() - start_time
                recovered = node.recoverpath()
                print("Solution length: ", len(recovered))
                print("Solution cost: ", node.cost)
                print("Solution path: ", recovered)
                print()
                print("Generated nodes: ", generated)
                print("Expanded nodes: ", expanded)
                print("--- %s seconds ---" % total_time)
                return [len(recovered),node.cost,generated,expanded,total_time]
            sucessors = node.expand()
            expanded += 1
            for suc in sucessors:
                open.put((suc.cost + heuristic(suc), generated,suc))
                generated += 1
            explored[node.__hash__()] = node.state
    print("Something went wrong")
    return [-1,-1,-1,-1,-1]
