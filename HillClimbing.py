from A_star import a_star as evaluate
from time import time

def hillClimbing(initialSolution):
    startTime = time()
    evaluated=0
    currentSolution = initialSolution
    currentScore = evaluate(currentSolution)
    evaluated+=1
    improves = True
    while improves:
        improves = False
        neighbors = currentSolution.generateNeighbours()
        for neighbor in neighbors:
            score = evaluate(neighbor)
            evaluated+=1
            if score[0] > currentScore[0]:
                currentSolution = neighbor
                currentScore = score
                improves = True
    return [currentScore,currentSolution,evaluated,time()-startTime]
