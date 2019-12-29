import sys
from HillClimbing import hillClimbing
from Maze import getProblemInstance
from Node import Node
from random import randint
from time import time

def randomizedLocalSearch(size, seed, nWalls, maxIterations):
    startTime=time()
    solution = [-1,None]
    for iteration in range(maxIterations):
        maze=getProblemInstance(size,seed,nWalls+iteration*randint(1,2))

        x = Node(None, None, None, 0, "", 0, size)
        x.filler(maze)

        y=hillClimbing(x)
        if y[0] > solution[0]:
            solution=y
    return solution[:-1]+[time()-startTime]


