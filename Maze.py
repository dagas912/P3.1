
import random
def getProblemInstance(n, seed, nWallsParam):
    """ This method generates a new problem instance. Cells with value 0 means empty cells. Cells with value -1 are walls. Cells with value i (1..n) are occupied by the i-th car.
    Returns a maze (problem instance)
    Parameters: n -- size of the maze (Int) nCars -- number of Cars (<=n) (Int) seed -- or the random generator (Int)
    """
    maze = [[0 for i in range(n)] for j in range(n)]
    random.seed(seed)
    # placing walls
    nWalls = int(n * (n-2) * 0.2) if nWallsParam<0 or nWallsParam>n*(n-2) else nWallsParam
    i=0
    while i < nWalls:
        x=random.randint(0,n-3) + 1
        y=random.randint(0,n-1)
        if maze[x][y]==0:
            maze[x][y] = -1
        else: 
            0
            i-=1
        i +=1 
    
    maze[0][0] = 1
    maze[0][-1] = 2 
    return maze