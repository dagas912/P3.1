import sys
from os import system
from time import time

def tests(argv):
    size = list(map(int,argv[0].split(',')))
    seed = list(map(int,argv[1].split(',')))
    algorithm = argv[3].upper()
    nWalls_nPopulation = list(map(int,argv[4].split(',')))
    nIterations_nGenerations = [1] if len(argv)<=5 else list(map(int,argv[5].split(',')))
    propPermut_probCross = [0.25] if len(argv)<=6 else list(map(float,argv[6].split(',')))
    probMutation = [] if len(argv)<=7 else list(map(float,argv[7].split(',')))
    select = [0] if len(argv)<=9 else list(map(int,argv[9].split(',')))
    cross = [0] if len(argv)<=10 else list(map(int,argv[10].split(',')))

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
                            if algorithm != 'HILLCLIMBING':
                                splitTxt(filename,lnIterations_nGenerations)

            elif algorithm == 'GENETIC':
                for lnWalls_nPopulation in nWalls_nPopulation:
                    for lnIterations_nGenerations in nIterations_nGenerations:
                        for lpropPermut_probCross in propPermut_probCross:
                            for lprobMutation in probMutation:
                                for lselect in select:
                                    for lcross in cross:
                                        call = '{} {} -- {} {} {} {} {} -- {} {}'.format(lsize,lseed,algorithm,lnWalls_nPopulation,lnIterations_nGenerations,lpropPermut_probCross,lprobMutation,lselect,lcross)
                                        filename='{}_{}_{}_{}_{}_{}_{}_{}_{}.txt'.format(algorithm,lsize,lseed,lnWalls_nPopulation,lnIterations_nGenerations,lpropPermut_probCross,lprobMutation,lselect,lcross)
                                        system("python assigment3.py {} > .\\tests\{}".format(call,filename))
                                        splitTxt(filename,lnIterations_nGenerations)


def splitTxt(filename: str, iteraciones: int):
    f=open(".\\tests\{}".format(filename),"r")

    lines=f.readlines()

    if filename[0] != 'G':
        filename_end=filename[filename.index('s')+len(str(iteraciones))+1:]
        for nI in range(iteraciones):
            i=filename.index('s')
            filename=filename[:i+1]+str(nI+1)+filename_end
            print(filename)
            nf=open(".\\tests\{}".format(filename),"w+")
            nf_write=nf.write
            cont = False
            for line in lines:
                if line[:len(str(nI))+2] == 'I{};'.format(nI+1) or line[:len(str(nI))+3] == 'I{};'.format(nI+1): #Next iteration
                    break
                elif line[:len(str(nI))+2] == 'I{};'.format(nI) or cont or line[:len(str(nI))+3] == 'I{};'.format(nI): #Iteration itself
                    cont=True
                    nf_write(line)
                elif line[0] == 'I' and not cont: #Previous iterations
                    nf_write(line)
            nf.close()
    else:
        ii=0
        ie=-1
        for i in range(4):
            if i != 3:
                ie=filename[:ie].rindex('_')
            else:
                ii=filename[:ie-4].rindex('_')
        filename_start=filename[:ii]
        filename_end=filename[ie:]

        for nI in range(iteraciones):
            filename=filename_start+'_'+str(nI+1)+filename_end
            print(filename)
            nf=open(".\\tests\{}".format(filename),"w+")
            nf_write=nf.write
            cont=False
            for line in lines:
                if line[:len(str(nI))+2] == 'G{}B'.format(nI+1) or line[:len(str(nI))+3] == 'G{}B;'.format(nI+1):
                    break
                elif line[:len(str(nI))+2] == 'G{}B'.format(nI) or line[:len(str(nI))+3] == 'G{}B;'.format(nI) or cont:
                    cont=True
                    nf_write(line)
                elif line[0] == 'G' and not cont:
                    nf_write(line)
            nf.close()
            
    print()
    f.close()

if __name__ == "__main__":
    startTime=time()
    tests(sys.argv[1:])
    print("Tests Time: {}".format(time()-startTime))