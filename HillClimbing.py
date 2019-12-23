from A_star import a_star as evaluate
from Maze import getProblemInstance
from Node import Node
from copy import deepcopy
import sys

def hillClimbing(initialSolution: Node):
    currentSolution = initialSolution
    currentScore = evaluate(currentSolution)
    improves = True
    while improves:
        improves = False
        neighbors = currentSolution.generateNeighbours()
        for neighbor in neighbors:
            score = evaluate(neighbor)
            if score > currentScore:
                currentSolution = neighbor
                print("LEEEEEEEEEEEEEL")
                currentSolution.show_maze()
                currentScore = score
                improves = True
    return currentSolution



if __name__ == "__main__":
    maze = getProblemInstance(5,2019)
    root = Node(None, None, None, 0, "", 0, 5)
    root.filler(maze)
    final = hillClimbing(root)
    final.show_maze()
    #hillClimbing(sys.argv[1:])