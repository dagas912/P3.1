from Population import Population
from time import time
from copy import deepcopy


def GeneticAlgorithm(size: int, seed: int, populationSize: int, generations: int, probCoross: float, mutationProb: float, select=0, cross=0):
    startTime = time()
    P = Population(size, seed, populationSize, generations, probCoross, mutationProb)  # Creates candidates individuals. Generate
    for i in range(generations):
        _P = deepcopy(P.selectPopulation()) if select==0 else deepcopy(P.selectPopulationRanked())  # Select some individuals by score
        
        _P.crossover() if cross==0 else (_P.crossoverOne() if cross==1 else _P.crossoverTwo()) # Crosses pairs of selected individuals
        
        _P.mutation()  # Mutates the crossed individuals
        
        _P.reEvaluate()  # Obtains the score of the new individuals
        
        aux=_P.combine(P)

        P = aux[0] # Form the new population (Replace All or Takes the best)

        print("G{}BestIndividual;{}".format(i,aux[1]))
        print("G{}MeanIndividuals;{}".format(i,aux[2]))
    
    return sorted(P.individuals, key=lambda x: x[0],reverse=True)[0]+[populationSize*generations,time()-startTime]


if __name__ == "__main__":
    size = 5
    aux = GeneticAlgorithm(size, 2020, 20, 20, 0.85, 0.15, 0, 2)
    print("Time : " + str(aux[2]))
    print("Steps : " + str(aux[0]))
    from Node import Node
    root = Node(None, [(0, 0), (0, size - 1)], aux[1], 0, "", 0, size)
    root.show_maze()
