from A_star import a_star as evaluate
from Maze import getProblemInstance
from Node import Node
from copy import deepcopy
from walls import labyrinth
import sys

def hillClimbing(initialSolution: Node): 
    currentSolution = initialSolution
    currentScore = evaluate(initialSolution)
    improves = True
    while improves:
        improves = False
        neighbors = labyrinth.neighbour(currentSolution)
        for neighbor in neighbors:
            score = evaluate(neighbor)
            if score > currentScore:
                currentSolution = neighbor
                currentScore = score
                improves = True
    return currentSolution



if __name__ == "__main__":
    maze = getProblemInstance(5,2019)
    root = Node(None, None,None,0,"",0, 5)
    root.filler(maze)
    hillClimbing(root)
    #hillClimbing(sys.argv[1:])