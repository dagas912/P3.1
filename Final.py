from DepthFirst import *
from BreathFirst import *
from A_star import *
from BestFirst import *
from DepthLimited import *
from A_star import *
from Maze import *
from Node import *
from ShowMaze import *
import sys

if len(sys.argv) != 6 and len(sys.argv) != 7:
    print("Not enough arguments")
    print("This programme require 4 parameters:")
    print("\t1: The size of the maze")
    print("\t2: The number of cars used")
    print("\t3: The seed to gene")
    print("\t4: A --")
    print("\t5: The algorithm to be used")
    print("\t6: Extra argument if needed")
    exit()
operation = {
    "DepthFirst": depth_first_search,
    "BreathFirst": breath_first_search,
    "AStar": a_star,
    "BestFirst": best_first,
    "DepthLimited" : depth_limit_search
}
root = Node(None, getProblemInstance(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])), 0, "", 0,[])
root.carlistfiller();
show_maze(root)

if(sys.argv[5] == "DepthLimited" and len(sys.argv) == 7):
    operation[sys.argv[5]](root,int(sys.argv[6]))
    exit()
elif(sys.argv[5] != "DepthLimited" and len(sys.argv) == 6 and sys.argv[5] in operation):
    operation[sys.argv[5]](root)
else:
    print("Not enough arguments or incorrect")

