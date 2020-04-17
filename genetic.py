import random

class SimpleGeneticAlgorithm():
    
    population = []
    fitness = []
    
    def __init__(self, pop_size, num_genes):
        
        self.pop_size = pop_size
        self.num_genes = num_genes
        self.population = self.generatePop()
        self.fitness = self.fitnessCalculus()
    
    def generatePop(self):
        
        for i in range(self.pop_size):
            
            temp = []
            
            for j in range(self.num_genes):
                
                temp.append(int(random.getrandbits(1)))
                
            self.population.append(temp)
        
        return self.population
    
    def fitnessCalculus(self):
        
        for individual in self.population:
            fitness_count = 0
            for gene in individual:
                if gene == 1:
                     fitness_count += 1
                   
            self.fitness.append(round(fitness_count/self.num_genes, 2))
        
        return self.fitness
    
    def selection(self):
        
        parent_a = max(self.fitness)
        index_parent_a = self.fitness.index(parent_a)
        self.fitness[index_parent_a] = -1.0
        parent_b = max(self.fitness)
        index_parent_b = self.fitness.index(parent_b)
        self.fitness[index_parent_a] = parent_a
        
        print(f'Fittest parent A: {parent_a}, [index: {index_parent_a}]\nFittest parent B: {parent_b}, [index: {index_parent_b}]')
        
        return index_parent_a, index_parent_b
    
    def crossover(self, parent_a, parent_b):
        
        crossoverPoint = random.randint(1, self.num_genes - 1)
        
        print(self.population[parent_a])
        print(self.population[parent_b])
        print(f'crossover point: {crossoverPoint}')
        
        for i in range(crossoverPoint):
            
            change_gene = self.population[parent_a][i]
            self.population[parent_a][i] = self.population[parent_b][i]
            self.population[parent_b][i] = change_gene
        
        print(self.population[parent_a])
        print(self.population[parent_b])
        
        return self.population[parent_a], self.population[parent_b]
        
    def mutation(self, parent_a, parent_b):

        mutation_gene_1 = random.randint(0, self.num_genes-1)
        mutation_gene_2 = random.randint(0, self.num_genes-1)
        
        print(f'mutation gene 1: {mutation_gene_1}')
        print(f'mutation gene 2: {mutation_gene_2}')
        
        print(self.population[parent_a])
        print(self.population[parent_b])
        
        print('------------------------------')
        if self.population[parent_a][mutation_gene_1] == 0:       
            self.population[parent_a][mutation_gene_1] = 1
        else:
            self.population[parent_a][mutation_gene_1] = 0
        
        if self.population[parent_b][mutation_gene_2] == 0:       
            self.population[parent_b][mutation_gene_2] = 1
        else:
            self.population[parent_b][mutation_gene_2] = 0   
        
        print(self.population[parent_a])
        print(self.population[parent_b])
        
    def changeLeastFit(self, parent_a, parent_b):
        
        self.fitnessCalculus()

        least_fit = min(self.fitness)
        index_least_fit = self.fitness.index(least_fit)
        print(index_least_fit, len(self.population))
        
        if self.fitness[parent_a] > self.fitness[parent_b]:
            fittest_child = self.population[parent_a]
        else:
            fittest_child = self.population[parent_b]
        
        print(self.population)
        self.population[index_least_fit] = fittest_child
        print(self.population)
        
        return self.population[index_least_fit]
    
    
    def generateOffspring(self):
        pass

                       
gen = SimpleGeneticAlgorithm(10, 10)
child_a, child_b = gen.selection()
print(child_a, child_b)
print(gen.crossover(child_a, child_b))
print(gen.mutation(child_a, child_b))
print(gen.changeLeastFit(child_a, child_b))