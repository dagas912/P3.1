def heuristic(node):
    #return sum(node.size-node.state[i][0] for i in range(len(node.state)))
    result = 0
    nodesize=node.size
    nodewalls=node.walls
    nodestate=node.state
    for car in node.state:
        result += nodesize - car[0]
        for i in range(car[0] + 1 , nodesize -1):
            if (i,car[1]) in nodewalls:
                result += 1
    return result