from copy import deepcopy
class Node:

    def __init__(self, parent, state,walls,depth, action, cost, size):
        self.parent = parent
        self.state = state
        self.walls = walls
        self.depth = depth
        self.action = action
        self.cost = cost
        self.size = size
        self.walls = walls

    def filler(self,maze):
        self.walls = dict()
        self.state = []
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] > 0 :
                    if len(self.state) < maze[i][j] :
                        for m in range(maze[i][j] -len(self.state)):
                            self.state.append((-1,-1))
                    self.state[maze[i][j] - 1] = (i,j)
                elif maze[i][j] == -1:
                    self.walls[(i,j)] = -1
        print(self.state)
        print(self.walls)
        return

    def show_maze(self):
        aux = [[0 for i in range(self.size)] for j in range(self.size)]
        count = 1
        for i in self.state:
            aux[i[0]][i[1]] = count
            count += 1
        for i in self.walls.keys():
            aux[i[0]][i[1]] = -1

        for i in range(len(aux)):
            row = ""
            for j in range(len(aux[0])):
                row = row + ("x " if aux[i][j] == -1 else str(aux[i][j]) + " ")
            print(row)
        return

    def movement(self,car):
        x = self.state[car][0]
        y = self.state[car][1]
        result = []
        cars = dict()
        for i in self.state:
            cars[i] = -1

        if y != 0 and (x, y - 1) not in self.walls and (x, y - 1) not in cars:
            auxcars = deepcopy(self.state)
            auxcars[car] = (x, y - 1)

            result.append(
                Node(self, auxcars, self.walls, self.depth + 1, str(car + 1) + ": left", self.cost + 1, self.size))
        if y != (self.size - 1) and (x, y + 1) not in self.walls and (x, y + 1) not in cars:
            auxcars = deepcopy(self.state)
            auxcars[car] = (x, y + 1)

            result.append(
                Node(self, auxcars, self.walls, self.depth + 1, str(car + 1) + ": right", self.cost + 1, self.size))
        if x != 0 and (x - 1, y) not in self.walls and (x - 1, y) not in cars:
            auxcars = deepcopy(self.state)
            auxcars[car] = (x - 1, y)

            result.append(
                Node(self, auxcars, self.walls, self.depth + 1, str(car + 1) + ": up", self.cost + 1, self.size))

        if x != (self.size - 1) and (x + 1, y) not in self.walls and (x + 1, y) not in cars:
            auxcars = deepcopy(self.state)
            auxcars[car] = (x + 1, y)

            result.append(
                Node(self, auxcars, self.walls, self.depth + 1, str(car + 1) + ": down", self.cost + 1, self.size))
        return result

    def expand(self):
        result = []
        for i in range(len(self.state)):
            for generated in self.movement(i):
                result.append(generated)
        return result

    def recoverpath(self):
        original = self
        solution = []
        while original.action != '':
            solution.append(original.action)
            original = original.parent
        solution.reverse()
        return solution

    def testgoal(self):
        returned = True
        for i in self.state:
            returned = i[0] == self.size - 1 and returned

        return returned
    def __hash__(self):
        return hash(tuple(self.state))

    __slots__ = ['parent', 'state',"walls" ,'depth', 'action', 'cost','size']

