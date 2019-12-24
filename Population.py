from Maze import getProblemInstance
from A_star import a_star as evaluate
from Node import Node
from random import randrange
from random import choices

class Population:

    #GeneratePopulation: Inicializara la poblacion la primera vez. Generada de forma aleatoria
    def __init__(self, size: int, seed: int, populationSize: int, generations: int, probCoross: float, mutationProb: float, individuals=None): 
        self.individuals = [] #List that contains the individuals (idividual represented as mazes distribution) and their score

        if individuals == None:
            for i in range(populationSize):
                maze = getProblemInstance(size,seed,i)
                root = Node(None, None, None, 0, "", 0, size)
                root.filler(maze)
                self.individuals.append([evaluate(root),maze]) #individuals almacena un par de maze con su score de toda la poblacion en su dicionario (Creo que una lista serviria igual)
        else:
            self.individuals = individuals

        self.size = size #TODO Size y Seed no se si seran utiles, pero por ahora se dejan
        self.seed = seed
        self.populationSize = populationSize
        self.generations = generations
        self.probCross = probCoross
        self.mutationProb = mutationProb


    def selectPopulation(self): # Select some individuals by score
        res1, res2 = map(list, zip(*self.individuals)) 
        return choices(res2,res1,k=self.populationSize) # TODO Tiene que devolver a parte del laberinto seleccionado su score. Parece que va a tocar hacer algo mas a mano (hacer choices pero con un elemento, asi si se podra actualizar)
        
    def reEvaluate(self): # Execute again the A* To update scores
        for index,elem in enumerate(self.individuals):
            root = Node(None, None, None, 0, "", 0, size)
            root.filler(elem[1])
            self.individuals[index][0]=evaluate(root)
    
    '''def crossover(self): # Crosses pairs of selected individuals


    def mutation(self):  # Mutates the crossed individuals


    def combine(self, prePopulation: Population): # Form the new population (Replace All or Takes the best)'''
    