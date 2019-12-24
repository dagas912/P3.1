from Maze import getProblemInstance
from A_star import a_star as evaluate

class Population:

    #GeneratePopulation: Inicializara la poblacion la primera vez. Generada de forma aleatoria
    def __init__(self, size: int, seed: int, populationSize: int, generations: int, probCoross: float, mutationProb: float): 
        self.individuals = {} #Dict that contains the individuals (idividual represented as mazes distribution) and their score
        for i in range(populationSize):
            maze = getProblemInstance(size,seed,i)
            self.individuals[maze]=evaluate(maze) #TODO No se yo hasta que punto se puede usar un dicionario asi

        self.size = size #TODO Size y Seed no se si seran utiles, pero por ahora se dejan
        self.seed = seed
        self.populationSize = populationSize
        self.generations = generations
        self.probCross = probCoross
        self.mutationProb = mutationProb


    def selectPopulation(self): # Select some individuals by score

    
    def crossover(self): # Crosses pairs of selected individuals


    def mutation(self):  # Mutates the crossed individuals

    
    def reEvaluate(self): # Execute again the A* To update scores
        for elem in self.individuals:
            self.individuals[elem]=evaluate(elem)


    def combine(self, prePopulation: Population): # Form the new population (Replace All or Takes the best)
    