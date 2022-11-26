def socialist_distribution(population, minimum):
    def issatisfied(population, minimum):
        return all(list(map(lambda x: x >= minimum, population)))

    pop = population[::]
    satisfied = issatisfied(pop, minimum)
    while not satisfied:
        pop_c = pop[::]
        
        pop[pop.index((max(pop)))] -= 1
        pop[pop.index((min(pop)))] += 1
        
        if pop_c == pop:
            return []        
            
        satisfied = issatisfied(pop, minimum)
    return pop

# not solved lol
# print(socialist_distribution([24,48,22,19,37],30))
# print(socialist_distribution([2,3,5,45,45],30))