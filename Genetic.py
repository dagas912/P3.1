from Population import Population
from time import time
from copy import deepcopy


def GeneticAlgorithm(size: int, seed: int, populationSize: int, generations: int, probCoross: float, mutationProb: float):
    startTime = time()
    P = Population(size, seed, populationSize, generations, probCoross, mutationProb)  # Creates candidates individuals. Generate
    for i in range(generations):
        print("\nGen {}".format(i))
        _P = deepcopy(P.selectPopulation())  # Select some individuals by score
        print("Population selected")
        #_P = Population(size, seed, populationSize, generations, probCoross, mutationProb,_P)
        _P.crossover()  # Crosses pairs of selected individuals
        print("Crossover realized")
        _P.mutation()  # Mutates the crossed individuals
        print("Idividuals mutated")
        _P.reEvaluate()  # Obtains the score of the new individuals
        print("New individuals evaluated")
        P = _P.combine(P) # Form the new population (Replace All or Takes the best)
        print("Generations combined")
    return sorted(P.individuals, key=lambda x: x[0],reverse=True)[0]+[time()-startTime]


if __name__ == "__main__":
    size = 5
    aux = GeneticAlgorithm(size, 2020, 20, 50, 0.85, 0.15)
    print("Time : " + str(aux[2]))
    print("Steps : " + str(aux[0]))
    from Node import Node
    root = Node(None, [(0, 0), (0, size - 1)], aux[1], 0, "", 0, size)
    root.show_maze()
