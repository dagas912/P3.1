import sys
from Genetic import GeneticAlgorithm
from HillClimbing import hillClimbing
from RandomizedLocalSearch import randomizedLocalSearch
from Node import Node
from Maze import getProblemInstance

def assigment3(argv):
    size = int(argv[0])
    seed = int(argv[1])
    algorithm = argv[3].upper()

    error=False

    if algorithm == 'GENETIC':
        populationSize = int(argv[4])
        generations = int(argv[5])
        probCoross = float(argv[6])
        mutationProb = float(argv[7])
        sol=GeneticAlgorithm(size,seed,populationSize,generations, probCoross, mutationProb)
    elif algorithm == 'HILLCLIMBING':
        nWalls=int(argv[4])
        maze = getProblemInstance(size,seed,nWalls)
        root = Node(None, None, None, 0, "", 0, size)
        root.filler(maze)
        sol=hillClimbing(root)
    elif algorithm=='RANDOMLOCALSEARCH':
        nWalls=int(argv[4])
        maxIterations=int(argv[5])
        sol=randomizedLocalSearch(size,seed,nWalls,maxIterations)
    else:
        error=True
        print("Error selecting algorithm")

    if not error:
        print("Sol maze:")
        if algorithm=='GENETIC':
            Node(None, [(0,0),(0,size-1)], sol[1], 0, "", 0, size).show_maze()
        else:
            sol[1].show_maze()
        print("Score: {}".format(sol[0]))
        print("Time: {}".format(sol[2]))


if __name__ == "__main__":
    assigment3(sys.argv[1:])