
class Node:

    def __init__(self, parent, state,walls,depth, action, cost, size):
        self.parent = parent
        self.state = state
        self.walls = walls
        self.depth = depth
        self.action = action
        self.cost = cost
        self.size = size


#    @classmethod
#    def rootNode(self,size,seed):
#        return self(None, None,None,0,"",0, 5)
    
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
        #print(self.state)
        #print(self.walls)
        return

    
    def show_maze(self):
        aux = [["·" for i in range(self.size)] for j in range(self.size)]
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
        result_append=result.append
        cars = dict()

        localstate=self.state
        localwalls=self.walls
        localdepth=self.depth
        localcost=self.cost
        localsize=self.size

        for i in localstate:
            cars[i] = -1

        if y != 0 and (x, y - 1) not in localwalls and (x, y - 1) not in cars:
            auxcars = localstate[:]
            auxcars[car] = (x, y - 1)

            result_append(
                Node(self, auxcars, localwalls, localdepth + 1, "{}: left".format(str(car + 1)), localcost + 1, localsize))
        if y != (localsize - 1) and (x, y + 1) not in localwalls and (x, y + 1) not in cars:
            auxcars = localstate[:]
            auxcars[car] = (x, y + 1)

            result_append(
                Node(self, auxcars, localwalls, localdepth + 1, "{}: right".format(str(car + 1)), localcost + 1, localsize))
        if x != 0 and (x - 1, y) not in localwalls and (x - 1, y) not in cars:
            auxcars = localstate[:]
            auxcars[car] = (x - 1, y)

            result_append(
                Node(self, auxcars, localwalls, localdepth + 1, "{}: up".format(str(car + 1)), localcost + 1, localsize))

        if x != (localsize - 1) and (x + 1, y) not in localwalls and (x + 1, y) not in cars:
            auxcars = localstate[:]
            auxcars[car] = (x + 1, y)

            result_append(
                Node(self, auxcars, localwalls, localdepth + 1,  "{}: down".format(str(car + 1)), localcost + 1, localsize))
        return result

    
    def expand(self):
        result = []

        localstate=self.state
        movement=self.movement
        result_append=result.append

        for i in range(len(localstate)):
            for generated in movement(i):
                result_append(generated)
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

        localstate=self.state
        localsize=self.size

        for i in localstate:
            returned = i[0] == localsize - 1 and returned

        return returned

    
    def generateNeighbours(self):
        from random import choices
        from random import randint

        result = []
        
        result_append=result.append
        wallskeys=self.walls.keys()
        neigbourWalls=self.neigbourWalls
        localwalls=self.walls
        localsize=self.size
        localstate=self.state

        for wall in wallskeys:
            result += neigbourWalls(wall)
        if len(localwalls)>0:
            auxwalls = list(localwalls)
            chos = choices(auxwalls)
            auxwalls=dict(localwalls)
            auxwalls.pop(chos[0])
            result_append(Node(None,localstate,dict.fromkeys(auxwalls,-1),0,"",0,localsize))
        for _ in range(len(localwalls)*2+1):
            new = (randint(1,localsize -2), randint(0,localsize -1))
            if new not in localwalls:
                auxwalls = dict(self.walls)
                auxwalls[new] = -1
                result_append(Node(None, localstate, auxwalls, 0, "", 0, localsize))
                break
        return result if len(result)>0 else [Node(None,localstate,{(randint(1,localsize -2),randint(0,localsize -1)):-1},0,"",0,localsize)]

    
    def neigbourWalls(self,wall):
        x = wall[0]
        y = wall[1]
        result = []

        result_append=result.append
        localwalls=self.walls
        localstate=self.state
        localsize=self.size

        if y != 0 and (x, y - 1) not in localwalls:
            #auxcars = list(self.state)
            auxwalls = dict(localwalls)
            auxwalls.pop(wall)
            auxwalls[(wall[0]),wall[1] - 1] = -1
            result_append(Node(None, localstate, auxwalls, 0, "", 0, localsize))
        if y != (localsize - 1) and (x, y + 1) not in localwalls:
            #auxcars = list(self.state)
            auxwalls = dict(localwalls)
            auxwalls.pop(wall)
            auxwalls[(wall[0]),wall[1] + 1] = -1
            result_append(Node(None, localstate, auxwalls, 0, "", 0, localsize))
        if x != 1 and (x - 1, y) not in localwalls:
            #auxcars = list(self.state)
            auxwalls = dict(localwalls)
            auxwalls.pop(wall)
            auxwalls[(wall[0]-1),wall[1]] = -1
            result_append(Node(None, localstate, auxwalls, 0, "", 0, localsize))
        if x != (localsize - 2) and (x + 1, y) not in localwalls:
            #auxcars = list(self.state)
            auxwalls = dict(localwalls)
            auxwalls.pop(wall)
            auxwalls[(wall[0] + 1),wall[1]] = -1
            result_append(Node(None, localstate, auxwalls, 0, "", 0, localsize))

        return result
    def __hash__(self):
        localstate=self.state
        return hash(tuple(localstate))

    __slots__ = ['parent', 'state',"walls" ,'depth', 'action', 'cost','size']

