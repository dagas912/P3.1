from time import time
from Maze import getProblemInstance
from Node import Node
from random import random
from HillClimbing import hillClimbing
from copy import deepcopy
from ShowResults import showResult

def iteratedLocalSearch(size, seed, nWalls, maxIterations,perturbation=0.25):
    startTime = time()
    solution = [[-1,-1],None]
    evaluated=0
    maze = getProblemInstance(size, seed, nWalls)
    x = Node(None, None, None, 0, "", 0, size)
    x.filler(maze)
    for i in range(int(maxIterations)):
        perturbate(x,perturbation)
        y = hillClimbing(x)
        evaluated+=y[2]
        if y[0][0] > solution[0][0]:
            solution=y
        x=deepcopy(y[1])
        print("I{};{}".format(i,y[0][0])) 
        showResult(solution[:-2]+[evaluated,time()-startTime],"ITERATIVELOCALSEARCH",size)

    return solution[:-2]+[evaluated,time()-startTime]

def perturbate(node,perturbation):
    localsize=node.size
    localwalls=node.walls
    localwallspop=node.walls.pop
    localwallsupdate=node.walls.update
    for i,j in enumerate(range(localsize)):
        if i!=0 and i != localsize-1 and random()<perturbation:
            if (i,j) in localwalls:
                localwallspop((i,j))
            else:
                localwallsupdate({(i,j):-1})
            
if __name__ == "__main__":
    sol=iteratedLocalSearch(5,2020,0,40,0.2)
    print("Sol maze:")
    sol[1].show_maze()
    print("Score: {}".format(sol[0]))
    print("Time: {}".format(sol[2]))
