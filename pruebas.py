from Maze import *
import A_star
import sys
from Node import Node
from time import time
from HillClimbing import hillClimbing

#"AStar": a_star,


size = 5
seed = 1
nWalls = 5

startTime=time()
maze = getProblemInstance(size,seed,nWalls)
root = Node(None, None, None, 0, "", 0, size)
root.filler(maze)

'''i=0

for lel in root.generateNeighbours():
    print(A_star.a_star(lel))
    i+=1
    #input()

print(A_star.a_star(root))
print("Time: {}".format(time()-startTime))
print("A* Executed: {}".format(i+1))'''

score, solution,_, time = hillClimbing(root)
print("Score: {}".format(score))
solution.show_maze()
print("Time: {}".format(time))

Node(None,[(0,0),(0,size-1)],{(1,3):-1,(1,4):-1,(3,1):-1,(3,2):-1,(3,3):-1,(3,0):-1 },0,"",0,size ).show_maze()
print(A_star.a_star(Node(None,[(0,0),(0,size-1)],{(1,3):-1,(1,4):-1,(3,1):-1,(3,2):-1,(3,3):-1,(3,0):-1 } ,0,"",0,size )))