import sys

def assigment3(argv):
    size = int(argv[0])
    seed = int(argv[1])
    algorithm = argv[3].upper()

    error=False

    if algorithm == 'GENETIC':
        from Genetic import GeneticAlgorithm

        populationSize = int(argv[4])
        generations = int(argv[5])
        probCoross = float(argv[6])
        mutationProb = float(argv[7])
        select = 0 if len(argv)<=9 else int(argv[9])
        cross = 0 if len(argv)<=10 else int(argv[10])

        select = int(argv[9]) if len(argv)>9 else 0
        cross = int(argv[10]) if len(argv)>10 else 0
        sol=GeneticAlgorithm(size,seed,populationSize,generations, probCoross, mutationProb,select,cross)
    elif algorithm == 'HILLCLIMBING':
        from Node import Node
        from HillClimbing import hillClimbing
        nWalls=int(argv[4])
        from Maze import getProblemInstance

        maze = getProblemInstance(size,seed,nWalls)
        root = Node(None, None, None, 0, "", 0, size)
        root.filler(maze)
        sol=hillClimbing(root)
    elif algorithm=='RANDOMLOCALSEARCH':
        from RandomizedLocalSearch import randomizedLocalSearch

        nWalls=int(argv[4])
        maxIterations=int(argv[5])
        sol=randomizedLocalSearch(size,seed,nWalls,maxIterations)
    elif algorithm == 'ITERATIVELOCALSEARCH':
        from IteratedLocalSearch import iteratedLocalSearch

        nWalls=int(argv[4])
        maxIterations=int(argv[5])
        sol=iteratedLocalSearch(size,seed,nWalls,maxIterations) if len(argv)==6 else iteratedLocalSearch(size,seed,nWalls,maxIterations,float(argv[6]))
    else:
        error=True
        print("Error selecting algorithm")

    if not error:
        print("Sol maze:")
        if algorithm=='GENETIC':
            from Node import Node
            Node(None, [(0,0),(0,size-1)], sol[1], 0, "", 0, size).show_maze()
        else:
            sol[1].show_maze()
        print("Expanded nodes: {}".format(sol[0][0]))
        print("Cost: {}".format(sol[0][1]))
        print("Time: {}".format(sol[2]))


if __name__ == "__main__":
    assigment3(sys.argv[1:])