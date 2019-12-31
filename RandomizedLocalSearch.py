
from HillClimbing import hillClimbing
from Maze import getProblemInstance
from Node import Node
from random import randint
from time import time

def randomizedLocalSearch(size, seed, nWalls, maxIterations):
    startTime=time()
    solution = [[-1,-1],None]
    for iteration in range(maxIterations):
        newSeed=seed+randint(0,5000)
        newNWalls=randint(0,size*(size-3))
        maze=getProblemInstance(size,newSeed,newNWalls) if iteration > 0 else getProblemInstance(size,seed,nWalls)

        x = Node(None, None, None, 0, "", 0, size)
        x.filler(maze)

        y=hillClimbing(x)
        if y[0][0] > solution[0][0]:
            solution=y
        print("{},{},{}: {}".format(iteration,newSeed,newNWalls,y[0]))
    return solution[:-1]+[time()-startTime]


