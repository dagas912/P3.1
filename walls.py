"""import random
from copy import deepcopy
from Node import Node

class labyrinth:
    def __init__(self,walls,size,seed,state):
        self.size = size
        self.walls = walls
        self.seed = seed
        self.state = state
    @classmethod
    def initialState(self,maze,seed):
        walls = []
        state = []
        size = len(maze)
        for i in range(size):
            for j in range(size):
                if maze > 0:

        return self([],size,random.seed(seed),state)

    def generateNode(self):
        state = [(0,0),(0,self.size-1)]
        nodeWalls = dict();
        for wall in self.walls:
            nodeWalls[wall] = -1
        return Node(None,state,nodeWalls,0,"",0, self.size)

    def neighbour(self):
        result = []
        for wall in range(len(self.walls)):
            result += self.expand(wall)
        while True:
            new = (random.randint(1,self.size -2), random.randint(0,self.size -1))
            if new not in self.walls:
                auxWalls = deepcopy(self.walls)
                auxWalls.append(new)
                result.append(labyrinth(auxWalls,self.size,self.seed))
                break




        return result

    def generateMaze(self):
        result = [[0 for i in range(self.size)] for j in range(self.size)]
        for i in range(len(self.walls)):
            result[self.walls[i][0]][self.walls[i][1]] = -1
        return result

    def printMaze(self):
        aux = self.generateMaze()
        for i in range(len(aux)):
            row = ""
            for j in range(len(aux[0])):
                row = row + ("x " if aux[i][j] == -1 else str(aux[i][j]) + " ")
            print(row)
        return

    def expand(self,wall):
        x = self.walls[wall][0]
        y = self.walls[wall][1]
        result = []

        if y != 0  and (x, y - 1) not in self.walls:
            auxwalls = deepcopy(self.walls)
            auxwalls[wall] = (x, y - 1)
            result.append(labyrinth(auxwalls,self.size,self.seed))

        if y != (self.size - 1) and (x, y + 1) not in self.walls:
            auxwalls = deepcopy(self.walls)
            auxwalls[wall] = (x, y + 1)
            result.append(labyrinth(auxwalls,self.size,self.seed))

        if x != 1 and (x - 1, y) not in self.walls:
            auxwalls = deepcopy(self.walls)
            auxwalls[wall] = (x - 1, y)
            result.append(labyrinth(auxwalls,self.size,self.seed))

        if x != (self.size - 2) and (x + 1, y) not in self.walls:
            auxwalls = deepcopy(self.walls)
            auxwalls[wall] = (x + 1, y)
            result.append(labyrinth(auxwalls,self.size,self.seed))

        return result
    """