from A_star import a_star as evaluate
from Population import Population


def GeneticAlgorithm(size: int, seed: int, populationSize: int, generations: int, probCoross: float, mutationProb: float):
    P = Population(size, seed, populationSize, generations, probCoross, mutationProb)  # Creates candidates individuals. Generate
    stopCondition = False
    while not stopCondition:
        _P = P.selectPopulation()  # Select some individuals by score
        _P.crossover()  # Crosses pairs of selected individuals
        _P.mutation()  # Mutates the crossed individuals
        _P.reEvaluate()  # Obtains the score of the new individuals
        P = _P.combine(P) # Form the new population (Replace All or Takes the best)
    return  # TODO Que cojones tiene que devolver esto? El mejor individuo de la ultima generacion?


if __name__ == "__main__":
    GeneticAlgorithm(5, 2019, 100, 50, 1.0, 0.01)
