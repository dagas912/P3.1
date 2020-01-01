

def showResult(sol: list, algorithm: str, size: int):
    if sol != None:
        print("A*_Executed;{}".format(sol[2]))
        print("Expanded_nodes;{}".format(sol[0][0]))
        print("Cost;{}".format(sol[0][1]))
        print("Time;{}".format(sol[-1]))

        print("Sol_maze;")
        if algorithm=='GENETIC':
            from Node import Node
            Node(None, [(0,0),(0,size-1)], sol[1], 0, "", 0, size).show_maze()
        else:
            sol[1].show_maze()
        
        print("")