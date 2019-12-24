from Maze import getProblemInstance
from A_star import a_star as evaluate
from Node import Node
from random import randrange
from random import choices

class Population:

    #GeneratePopulation: Inicializara la poblacion la primera vez. Generada de forma aleatoria
    def __init__(self, size: int, seed: int, populationSize: int, generations: int, probCoross: float, mutationProb: float): 
        self.individuals = [] #List that contains the individuals (idividual represented as mazes distribution) and their score

        for i in range(populationSize):
            maze = getProblemInstance(size,seed,i)
            root = Node(None, None, None, 0, "", 0, size)
            root.filler(maze)
            self.individuals.append([evaluate(root),maze]) #individuals almacena un par de maze con su score de toda la poblacion en su dicionario (Creo que una lista serviria igual)
        self.individuals.sort()

        self.size = size #TODO Size y Seed no se si seran utiles, pero por ahora se dejan
        self.seed = seed
        self.populationSize = populationSize
        self.generations = generations
        self.probCross = probCoross
        self.mutationProb = mutationProb


    def selectPopulation(self): # Select some individuals by score
        res1, res2 = map(list, zip(*self.individuals)) 
        return choices(res2,res1,k=self.populationSize)
        
    
    '''def crossover(self): # Crosses pairs of selected individuals


    def mutation(self):  # Mutates the crossed individuals

    
    def reEvaluate(self): # Execute again the A* To update scores
        for elem in self.individuals:
            self.individuals[elem]=evaluate(elem)


    def combine(self, prePopulation: Population): # Form the new population (Replace All or Takes the best)'''
    