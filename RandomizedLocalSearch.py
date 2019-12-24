import sys
from HillClimbing import hillClimbing
from Maze import getProblemInstance
from Node import Node
from random import randint
from time import time

def randomizedLocalSearch(argv):
    solution = [None,-1]
    maxIterations = int(argv[3])
    for iteration in range(maxIterations):
        maze=getProblemInstance(int(argv[0]),int(argv[1]),int(argv[2])+iteration*randint(1,2))

        x = Node(None, None, None, 0, "", 0, int(argv[0]))
        x.filler(maze)

        y=hillClimbing(x)
        if y[1] > solution[1]:
            solution=y
    return solution


if __name__ == "__main__":
    startTime = time()
    #sol=randomizedLocalSearch(['7','2019','0','10'])
    sol=randomizedLocalSearch(sys.argv[1:])
    print("\nFinal maze and score:" )
    sol[0].show_maze()
    print(sol[1])
    print("\nTime: {} sec".format(time()-startTime))
