from Maze import *
import A_star
import sys
from Node import Node

#"AStar": a_star,


size = 10
seed = 2019
nWalls = -1

maze = getProblemInstance(size,seed,nWalls)
root = Node(None, None,None,0,"",0, size)
root.filler(maze)
root.show_maze()
print("------------------------")
for lel in root.generateNeighbours():
    print("----------------------")
    lel.show_maze()

root = Node(None, None, None, 0, "", 0, size)
root.filler(maze)
root.show_maze()
A_star.a_star(root)

