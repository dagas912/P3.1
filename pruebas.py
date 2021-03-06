from Maze import *
import A_star
import sys
from Node import Node
from time import time
from HillClimbing import hillClimbing

#"AStar": a_star,


size = 9
seed = 2020
nWalls = 30

startTime=time()
maze = getProblemInstance(size,seed,nWalls)
root = Node(None, None, None, 0, "", 0, size)
root.filler(maze)
root.show_maze()

'''i=0

for lel in root.generateNeighbours():
    print(A_star.a_star(lel))
    i+=1
    #input()

print(A_star.a_star(root))
print("Time: {}".format(time()-startTime))
print("A* Executed: {}".format(i+1))'''

score, solution, time = hillClimbing(root)
print("Score: {}".format(score))
solution.show_maze()
print("Time: {}".format(time))