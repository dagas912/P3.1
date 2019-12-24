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
            score = evaluate(neighbor)
            if score > currentScore:
                neighbor.show_maze()
                print("")
                currentSolution = neighbor
                currentScore = score
                improves = True
    print("Score: {}".format(currentScore))
    print("Time: {}".format(time()-startTime))
    return [currentSolution,currentScore]



if __name__ == "__main__":
    size = int(sys.argv[1])
    seed=int(sys.argv[2])
    nWalls = int(sys.argv[3])
    maze = getProblemInstance(size,seed,nWalls)
    root = Node(None, None, None, 0, "", 0, size)
    root.filler(maze)
    root.show_maze()
    print("\n")
    final = hillClimbing(root)
    print("")
    final[0].show_maze()