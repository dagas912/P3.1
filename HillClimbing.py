from A_star import a_star as evaluate
from time import time

def hillClimbing(initialSolution):
    startTime = time()
    currentSolution = initialSolution
    currentScore = evaluate(currentSolution)
    improves = True
    while improves:
        improves = False
        neighbors = currentSolution.generateNeighbours()
        for neighbor in neighbors:
            score = evaluate(neighbor)
            if score[0] > currentScore[0]:
                currentSolution = neighbor
                currentScore = score
                improves = True
    return [currentScore,currentSolution,time()-startTime]
