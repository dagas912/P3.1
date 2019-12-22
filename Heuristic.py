def heuristic(node):
    return sum(node.size-node.state[i][0] for i in range(len(node.state)))