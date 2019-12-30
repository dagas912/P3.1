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
        individuals_append=self.individuals.append

        if individuals == None:
            for i in range(populationSize):
                maze = getProblemInstance(size, seed, i)
                root = Node(None, None, None, 0, "", 0, size)
                root.filler(maze)
                # individuals almacena un par de maze con su score de toda la poblacion en su dicionario (Creo que una lista serviria igual)
                individuals_append([evaluate(root), root.walls])
        else:
            self.individuals = individuals

        self.size = size  
        self.seed = seed
        self.populationSize = populationSize
        self.generations = generations
        self.probCross = probCoross
        self.mutationProb = mutationProb

    def selectPopulation(self):  # Select some individuals by score
        res1, res2 = map(list, zip(*self.individuals))
        result = []
        result_append=result.append

        localsize=self.size
        localseed=self.seed
        localpopulationSize=self.populationSize
        localgenerations=self.generations
        localprobCross=self.probCross
        localmutationProb=self.mutationProb
        localindividuals=self.individuals

        for _ in localindividuals:
            choosen = choices(res2, res1)
            index = res2.index(choosen[0])
            result_append([res1[index], choosen[0]])
        return Population(localsize, localseed, localpopulationSize, localgenerations, localprobCross, localmutationProb,result)

    def selectPopulationRanked(self):  # Select some individuals by score
        res1, res2 = map(list, zip(*self.individuals))
        total = sum(i for i in range(1, len(res2) + 1))
        res1 = [(len(res2) - i + 1)/ total for i in range(1,len(res2) + 1)]
        result = []
        result_append=result.append

        localsize=self.size
        localseed=self.seed
        localpopulationSize=self.populationSize
        localgenerations=self.generations
        localprobCross=self.probCross
        localmutationProb=self.mutationProb
        localindividuals=self.individuals

        for _ in localindividuals:
            choosen = choices(res2, res1)
            index = res2.index(choosen[0])
            result_append([res1[index], choosen[0]])
        return Population(localsize, localseed, localpopulationSize, localgenerations, localprobCross, localmutationProb,result)

    def reEvaluate(self):  # Execute again the A* To update scores

        localindividuals=self.individuals
        localsize=self.size

        for index, elem in enumerate(localindividuals):
            root = Node(None, [(0,0),(0,localsize-1)], elem[1], 0, "", 0, localsize)
            localindividuals[index][0] = evaluate(root) 

    def crossover(self):  # Crosses pairs of selected individuals
        score, walls = map(list, zip(*self.individuals))
        tempIndividuals = []
        tempIndividuals_append=tempIndividuals.append

        localprobCross=self.probCross
        localindividuals=self.individuals

        for score, indv1 in localindividuals:
            if random() <= localprobCross:
                indv2 = list(choices(walls)[0].keys())
                indv1 = list(indv1.keys())
                n = int(len(indv1)*random())
                indv = indv1[n:] + indv2[:n]
                indv =  dict.fromkeys(indv,-1)
                tempIndividuals_append([None, indv])
            else:
                tempIndividuals_append([None, indv1])
        localindividuals = tempIndividuals

    def crossoverOne(self):  # Crosses pairs of selected individuals
        score, walls = map(list, zip(*self.individuals))
        tempIndividuals = []
        tempIndividuals_append=tempIndividuals.append

        localprobCross=self.probCross
        localindividuals=self.individuals

        for score, indv1 in localindividuals:
            if random() <= localprobCross:
                indv2 = list(choices(walls)[0].keys())
                indv1 = list(indv1.keys())
                n = int(len(indv1) * random())
                child1 = indv1[n:] + indv2[:n]
                child2 = indv2[n:] + indv1[:n]
                child1 = dict.fromkeys(child1, -1)
                child2 = dict.fromkeys(child2, -1)
                tempIndividuals_append([None, child1])
                tempIndividuals_append([None, child2])
            else:
                tempIndividuals_append([None, indv1])
        localindividuals = tempIndividuals

    def crossoverTwo(self):  # Crosses pairs of selected individuals
        score, walls = map(list, zip(*self.individuals))
        tempIndividuals = []
        tempIndividuals_append=tempIndividuals.append

        localprobCross=self.probCross
        localindividuals=self.individuals

        for score, indv1 in localindividuals:
            if random() <= localprobCross:
                indv2 = list(choices(walls)[0].keys())
                indv1 = list(indv1.keys())
                n = int(len(indv1) * random())
                n2 = int((int(len(indv1) - n) * random()))
                child1 = indv1[:n] + indv2[n:n2] + indv1[n2:]
                child2 = indv2[:n] + indv1[n:n2] + indv2[n2:]
                child1 = dict.fromkeys(child1, -1)
                child2 = dict.fromkeys(child2, -1)
                tempIndividuals_append([None, child1])
                tempIndividuals_append([None, child2])
            else:
                tempIndividuals_append([None, indv1])
        localindividuals = tempIndividuals

    def mutation(self):  # Mutates the crossed individuals
        score, walls = map(list, zip(*self.individuals))
        tempIndividuals = []
        tempIndividuals_append=tempIndividuals.append

        localmutationProb=self.mutationProb
        localindividuals=self.individuals
        localsize=self.size

        for score, indv1 in localindividuals:
            if random() <= localmutationProb:
                y = randint(0, localsize-1)
                x = randint(1, localsize-2)
                if indv1.get((x,y)) != None: #El muro exist
                    indv1.pop((x,y))
                else: #El muro no existe
                    indv1.update({(x,y):-1}) 

            tempIndividuals_append([None, indv1])
        localindividuals = tempIndividuals

    def combine(self, prePopulation): # Form the new population (Replace All or Takes the best)
        aux = prePopulation.individuals + self.individuals
        aux = sorted(aux, key=lambda x: x[0],reverse=True)
        self.individuals = aux[:self.populationSize]
        return self
    
    def copy(self):
        aux = list(map(list,self.individuals))
        result = self(self.size, self.seed, self.populationSize, self.generations, self.probCoross, self.mutationProb,aux)
        return result