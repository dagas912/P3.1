from Maze import *
import A_star
import sys
from Node import Node
from time import time

#"AStar": a_star,


size = 5
seed = 2019
nWalls = 10

maze = getProblemInstance(size,seed,nWalls)

startTime=time()
root = Node(None, None, None, 0, "", 0, size)
root.filler(maze)
root.show_maze()
print(A_star.a_star(root))
print("Time: {}".format(time()-startTime))

