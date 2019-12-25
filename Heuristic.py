def heuristic(node):
    #return sum(node.size-node.state[i][0] for i in range(len(node.state)))
    result = 0
    for car in node.state:
        result += node.size - car[0]
        for i in range(car[0] + 1 , node.size -1):
            if (i,car[1]) in node.walls:
                result += 1
    return result