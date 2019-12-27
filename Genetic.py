from A_star import a_star as evaluate
from Population import Population
from time import time
from Node import Node
from copy import deepcopy


def GeneticAlgorithm(size: int, seed: int, populationSize: int, generations: int, probCoross: float, mutationProb: float):
    startTime = time()
    P = Population(size, seed, populationSize, generations, probCoross, mutationProb)  # Creates candidates individuals. Generate
    for _ in range(generations):
        _P = deepcopy(P.selectPopulation())  # Select some individuals by score
        #_P = Population(size, seed, populationSize, generations, probCoross, mutationProb,_P)
        _P.crossover()  # Crosses pairs of selected individuals
        _P.mutation()  # Mutates the crossed individuals
        _P.reEvaluate()  # Obtains the score of the new individuals
        P = _P.combine(P) # Form the new population (Replace All or Takes the best)
    return sorted(P.individuals, key=lambda x: x[0],reverse=True)[0]+[time()-startTime]

