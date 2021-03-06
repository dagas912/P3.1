from time import time
from Maze import getProblemInstance
from Node import Node
from random import random
from HillClimbing import hillClimbing

def iteratedLocalSearch(size, seed, nWalls, maxIterations,perturbation=0.25):
    startTime = time()
    solution = [-1,None]
    maze = getProblemInstance(size, seed, nWalls)
    x = Node(None, None, None, 0, "", 0, size)
    x.filler(maze)
    for i in range(maxIterations):
        perturbate(x,perturbation)
        y = hillClimbing(x)
        if y[0] > solution[0]:
            solution=y
        x=y[1]
        print("{}: {}".format(i,y[0]))

    return solution[:-1]+[time()-startTime]

def perturbate(node,perturbation):
    for i,j in enumerate(range(node.size)):
        if i!=0 and i != node.size-1 and random()<perturbation:
            if (i,j) in node.walls:
                node.walls.pop((i,j))
            else:
                node.walls.update({(i,j):-1})
            
if __name__ == "__main__":
    sol=iteratedLocalSearch(9,2020,0,40,0.2)
    print("Sol maze:")
    sol[1].show_maze()
    print("Score: {}".format(sol[0]))
    print("Time: {}".format(sol[2]))
