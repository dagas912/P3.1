from Maze import *
import A_star
import sys
from Node import Node

#"AStar": a_star,


size = 15
seed = 2019

maze = getProblemInstance(size,seed)
root = Node(None, None,None,0,"",0, size)
root.filler(maze)
root.show_maze()
print("------------------------")
A_star.a_star(root)