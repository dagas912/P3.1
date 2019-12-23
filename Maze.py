import sys
import random
def getProblemInstance(n, seed, nWallsParam):
    """ This method generates a new problem instance. Cells with value 0 means empty cells. Cells with value -1 are walls. Cells with value i (1..n) are occupied by the i-th car.
    Returns a maze (problem instance)
    Parameters: n -- size of the maze (Int) nCars -- number of Cars (<=n) (Int) seed -- or the random generator (Int)
    """
    maze = [[0 for i in range(n)] for j in range(n)]
    random.seed(seed)
    # placing walls
    nWalls = int(n * (n-2) * 0.4) if nWallsParam<0 else nWallsParam
        
    for i in range(nWalls):
        maze[random.randint(0,n-3) + 1][random.randint(0,n-1)] = -1
    
    maze[0][0] = 1
    maze[0][-1] = 2 
    return maze