from A_star import *
from ShowMaze import *
from Maze import *
from Expand2 import *
from A_star import *
import sys

#"AStar": a_star,


size = 4
ncars = 4
seed = 2022

maze = getProblemInstance(size,ncars,seed)
root = Node(None, None,None,0,"",0, size)
root.filler(maze);
root.show_maze();
print("------------------------")
"""
result = root.expand()
result = result[1].expand()
for i in result:
    print("----------------------------------")
    i.show_maze()"""
a_star(root)