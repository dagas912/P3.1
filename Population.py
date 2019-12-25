from Maze import getProblemInstance
from A_star import a_star as evaluate
from Node import Node
from random import random
from random import choices
from random import randint


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
        return Population(self.size, self.seed, self.populationSize, self.generations, self.probCross, self.mutationProb,result)

    def reEvaluate(self):  # Execute again the A* To update scores
        for index, elem in enumerate(self.individuals):
            root = Node(None, [(0,0),(0,self.size-1)], elem[1], 0, "", 0, self.size)
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

    def mutation(self):  # Mutates the crossed individuals
        score, walls = map(list, zip(*self.individuals))
        tempIndividuals = []
        for score, indv1 in self.individuals:
            if random() <= self.mutationProb:
                y = randint(0, self.size-1)
                x = randint(1, self.size-2)
                if indv1.get((x,y)) != None: #El muro exist
                    indv1.pop((x,y))
                else: #El muro no existe
                    indv1.update({(x,y):-1}) 

            tempIndividuals.append([None, indv1])
        self.individuals = tempIndividuals

    def combine(self, prePopulation): # Form the new population (Replace All or Takes the best)
        aux = prePopulation.individuals + self.individuals
        aux = sorted(aux, key=lambda x: x[0],reverse=True)
        self.individuals = aux[:int(len(aux)/2)]
        return self
    def copy(self):
        aux = list(map(list,self.individuals))
        result = self(self.size, self.seed, self.populationSize, self.generations, self.probCoross, self.mutationProb,aux)
        return result