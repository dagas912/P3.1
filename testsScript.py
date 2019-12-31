import sys
from os import system

def tests(argv):
    size = list(map(int,argv[0].split(',')))
    seed = list(map(int,argv[1].split(',')))
    algorithm = argv[3].upper()
    nWalls_nPopulation = list(map(int,argv[4].split(',')))
    nIterations_nGenerations = [1] if len(argv)<=5 else list(map(int,argv[5].split(',')))
    propPermut_probCross = [0.25] if len(argv)<=6 else list(map(float,argv[6].split(',')))
    probMutation = [] if len(argv)<=7 else list(map(float,argv[6].split(',')))

    for lsize in size:
        for lseed in seed:
            if algorithm == 'ITERATIVELOCALSEARCH' or algorithm == 'RANDOMLOCALSEARCH' or algorithm == 'HILLCLIMBING':
                for lnWalls_nPopulation in nWalls_nPopulation:
                    for lnIterations_nGenerations in nIterations_nGenerations:
                        for lpropPermut_probCross in propPermut_probCross:
                            if algorithm == 'ITERATIVELOCALSEARCH':
                                call = '{} {} -- {} {} {} {}'.format(lsize,lseed,algorithm,lnWalls_nPopulation,lnIterations_nGenerations,lpropPermut_probCross)
                                filename='{}_Size{}_Seed{}_nIterations{}_Perturb{}.txt'.format(algorithm,lsize,lseed,lnIterations_nGenerations,lpropPermut_probCross)
                            elif algorithm == 'RANDOMLOCALSEARCH':
                                call = '{} {} -- {} {} {}'.format(lsize,lseed,algorithm,lnWalls_nPopulation,lnIterations_nGenerations)
                                filename='{}_Size{}_Seed{}_nIterations{}.txt'.format(algorithm,lsize,lseed,lnIterations_nGenerations)
                            elif algorithm == 'HILLCLIMBING':
                                call = '{} {} -- {} {}'.format(lsize,lseed,algorithm,lnWalls_nPopulation)
                                filename='{}_Size{}_Seed{}.txt'.format(algorithm,lsize,lseed)
                            
                            system("python assigment3.py {} > .\\tests\{}".format(call,filename))

            

if __name__ == "__main__":
    tests(sys.argv[1:])