#   A simple implementation of genetic algorithm for solving the 8 queens problem
#   Number of genes(weights) = 8 (contains position of the queen in each column (0 indexed))
#   Number of chromosomes = n

import numpy as np
import random

#fitness function returns fitness as 28 minus the error, as error would be 28 if all the queens were attacking each other
#error is equal to the number of queens attacking each other
def get_fitness(pos):
    error=0
    for i in range(len(pos)):
        for j in range(i):
            if pos[i]==pos[j]:
                error=error+1
            if pos[i]==pos[j]+i-j:
                error=error+1
            if pos[i]==pos[j]+j-i:
                error=error+1

    return 28-error

def choose_parents(num_parents,fitness):
    parent_indices=fitness.argsort()[-num_parents:][::-1]
    return parent_indices

#assuming a case where we take two parents and produce two offsprings
def crossover(parents,crossover_point):
    offspring=np.empty([len(parents),8])
    for k in range(0,len(parents),2):
        offspring[k,0:crossover_point]= parents[k,0:crossover_point]
        offspring[k,crossover_point:]=parents[k+1,crossover_point:]
        offspring[k+1,0:crossover_point]=parents[k+1,0:crossover_point]
        offspring[k+1,crossover_point:]=parents[k,crossover_point:]
    return offspring

def mutate(offspring):
    for i in range(offspring.shape[0]):
        j=random.randint(0,7)
        val=random.choice([1,-1])
        offspring[i][j]=offspring[i][j]+val
        if offspring[i][j]>7:
            offspring[i][j]=7
        if offspring[i][j]<0:
            offspring[i][j]=0
    return offspring

if __name__ == "__main__":

    #size is the number of population size where each population has 8 states
    size=8
    population=np.random.randint(low=0,high=7,size = (size,8))
    new_population=np.random.randint(low=0,high=7,size = (size,8))
    iter=0
    while 1:
        print("Iteration: "+ str(iter))
        iter=iter+1
        fitness=np.zeros(size)
        for i in range(size):
            fitness[i]=get_fitness(population[i])
            if fitness[i]==28:
                print("Final State:")
                board=np.zeros([8,8])
                for j in range(8):
                    board[j][population[i][j]]=1
                print(board)
                exit()
        print(fitness)
        #Selects the number of parents we choose for crossover (should be even)
        num_parents=4
        parent_indices=choose_parents(num_parents,fitness)
        parents=np.empty([num_parents,8])
        for i in range(num_parents):
            parents[i]=population[parent_indices[i]]
        # print(parents)

        #crossing over the num_parents
        offsprings=crossover(parents,4)
        # print(offsprings)

        new_population[0:num_parents,:]=parents
        new_population[num_parents:,:]=offsprings

        mutated_population=mutate(population)

        population=new_population
        # print(population)
