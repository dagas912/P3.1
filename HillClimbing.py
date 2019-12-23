from A_star import a_star as evaluate
from Maze import getProblemInstance
from Node import Node
from copy import deepcopy
from time import time
import sys

def hillClimbing(initialSolution: Node):
    startTime = time()
    currentSolution = initialSolution
    currentScore = evaluate(currentSolution)
    improves = True
    while improves:
        improves = False
        neighbors = currentSolution.generateNeighbours()
        for neighbor in neighbors:
            nodeNeighbor = neighbor
            score = evaluate(nodeNeighbor)
            if score > currentScore:
                nodeNeighbor.show_maze()
                print("")
                currentSolution = neighbor
                currentScore = score
                improves = True
    print("Score: {}".format(score))
    print("Time: {}".format(time()-startTime))
    return currentSolution



if __name__ == "__main__":
    size = 10
    seed=2019
    nWalls = 25
    maze = getProblemInstance(size,seed,nWalls)
    root = Node(None, None, None, 0, "", 0, size)
    root.filler(maze)
    root.show_maze()
    print("\n")
    final = hillClimbing(root)
    print("")
    final.show_maze()
    #hillClimbing(sys.argv[1:])