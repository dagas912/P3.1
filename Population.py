from Maze import getProblemInstance
from A_star import a_star as evaluate
from Node import Node
from random import random
from random import choices


class Population:

    # GeneratePopulation: Inicializara la poblacion la primera vez. Generada de forma aleatoria
    def __init__(self, size: int, seed: int, populationSize: int, generations: int, probCoross: float, mutationProb: float, individuals=None):
        # List that contains the individuals (idividual represented as mazes distribution) and their score
        self.individuals = []

        if individuals == None:
            for i in range(populationSize):
                maze = getProblemInstance(size, seed, i)
                root = Node(None, None, None, 0, "", 0, size)
                root.filler(maze)
                # individuals almacena un par de maze con su score de toda la poblacion en su dicionario (Creo que una lista serviria igual)
                self.individuals.append([evaluate(root), root.walls])
        else:
            self.individuals = individuals

        self.size = size  # TODO Size y Seed no se si seran utiles, pero por ahora se dejan
        self.seed = seed
        self.populationSize = populationSize
        self.generations = generations
        self.probCross = probCoross
        self.mutationProb = mutationProb

    def selectPopulation(self):  # Select some individuals by score
        res1, res2 = map(list, zip(*self.individuals))
        result = []
        for _ in self.individuals:
            choosen = choices(res2, res1)
            index = res2.index(choosen[0])
            result.append([res1[index], choosen[0]])
        return result

    def reEvaluate(self):  # Execute again the A* To update scores
        for index, elem in enumerate(self.individuals):
            root = Node(None, None, elem[1], 0, "", 0, size)
            self.individuals[index][0] = evaluate(root)

    def crossover(self):  # Crosses pairs of selected individuals
        score, walls = map(list, zip(*self.individuals))
        tempIndividuals = []
        for score, indv1 in self.individuals:
            if random() <= self.probCross:
                indv2 = choices(walls)[0]
                indv1.update(indv2)
            tempIndividuals.append([None, indv1])
        self.individuals = tempIndividuals

    #def mutation(self):  # Mutates the crossed individuals


    #def combine(self, prePopulation: Population): # Form the new population (Replace All or Takes the best)
