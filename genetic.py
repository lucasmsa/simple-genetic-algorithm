import random
import math
import statistics

class SimpleGeneticAlgorithm():
    
    population = []
    fitness = []
    
    def __init__(self, pop_size, num_genes, n_iter, mutation_prob=2):
        
        self.pop_size = pop_size
        self.num_genes = num_genes
        self.n_iter = n_iter
        self.mutation_prob = mutation_prob
        self.population = self.generatePop()
        self.fitness = self.fitnessCalculus()
    
    
    def generatePop(self):
        
        """[First generation populated by pop_size
            with random values to its genes]
        
        Returns:
            [list] -- [Population that will be used
                       throughout the algorithm]
        """        
        
        for i in range(self.pop_size):
            
            temp = []
            
            for j in range(self.num_genes):
                
                temp.append(int(random.getrandbits(1)))
                
            self.population.append(temp)
        
        return self.population
    
    
    def fitnessCalculus(self):
        
        """[Calculating the fitness score of each individual
            which is based on the number of 1's that the chromosome
            has]
        
        Returns:
            [list] -- [list with fitness scores with corresponding
                       indexes to the population list]
        """        
        for individual in self.population:
            fitness_count = 0
            for gene in individual:
                if gene == 1:
                     fitness_count += 1
                   
            self.fitness.append(round(fitness_count/self.num_genes, 2))
        
        return self.fitness
    
    
    def selection(self):
        """[Selects the 2 best individuals from the population
            to generate new offspring]
        
        Returns:
            [2 int's] -- [Indexes of both parents]
        """        
        
        parent_a = max(self.fitness)
        index_parent_a = self.fitness.index(parent_a)
        self.fitness[index_parent_a] = -1.0
        parent_b = max(self.fitness)
        index_parent_b = self.fitness.index(parent_b)
        self.fitness[index_parent_a] = parent_a

        return index_parent_a, index_parent_b
    
    
    def crossover(self, parent_a, parent_b):
        """[Changing genes between parents to form
            offspring, based on a random crossover
            value (the ammount of genes swapped), also
            randomly picking right or left side of the 
            chromossome]
        
        Arguments:
            parent_a {[int]} -- [Index of parent a]
            parent_b {[int]} -- [Index of parent b]
        
        Returns:
            [2 list's] -- [2 newly formed offspring]
        """        
        
        crossoverPoint = random.randint(1, math.floor(self.num_genes/2))
        crossoverPart = int(random.getrandbits(1))
        li_copy = self.population[:]
        
        offspring_a = li_copy[parent_a]
        offspring_b = li_copy[parent_b]
        
        if crossoverPart == 0:
            
            for i in range(crossoverPoint):
                
                change_gene = offspring_a[i]
                offspring_a[i] = offspring_b[i]
                offspring_b[i] = change_gene
        else:
            
            for i in range(math.floor(self.num_genes/2), crossoverPoint + math.floor(self.num_genes/2)):
                
                change_gene = offspring_a[i]
                offspring_a[i] = offspring_b[i]
                offspring_b[i] = change_gene
            
        return offspring_a, offspring_b
        
        
    def mutation(self, offspring_a, offspring_b):
        """[Changes 1 gene in both offsprings, at a
            random position]
        
        Arguments:
            offspring_a {list]} -- [chromossome of offspring a]
            offspring_b {[list]} -- [chromossome of offspring b]
        
        Returns:
            [2 list's] -- [2 offsprings changed]
        """        

        mutation_gene_1 = random.randint(0, self.num_genes-1)
        mutation_gene_2 = random.randint(0, self.num_genes-1)
        
        if offspring_a[mutation_gene_1] == 0:
                   
            offspring_a[mutation_gene_1] = 1
        else:
            offspring_a[mutation_gene_1] = 0
        
        if offspring_b[mutation_gene_2] == 0:
                   
            offspring_b[mutation_gene_2] = 1
        else:
            offspring_b[mutation_gene_2] = 0   
        
        return offspring_a, offspring_b
    
    
    def fittestOffspring(self, offspring_a, offspring_b):
        """[Gets the offspring with the best fitness scores
            to substitute the individual in the population with 
            the worst fitness score (the other offspring will substitute
            the second least fit individual)]
        
        Arguments:
            offspring_a {list]} -- [chromossome of offspring a]
            offspring_b {[list]} -- [chromossome of offspring b]
        
        Returns:
            [2 list's and 2 floats] -- [returns both offsprings and their
                                        respective fitness values]
        """        
        
        fitness_a = 0
        for gene in offspring_a:
            if gene == 1:
                fitness_a += 1
                
        fitness_b = 0
        for gene in offspring_b:
            if gene == 1:
                fitness_b += 1
        
        fitness_a = round(fitness_a/self.num_genes, 2)
        fitness_b = round(fitness_b/self.num_genes, 2)
                
        if fitness_a >= fitness_b:
            return offspring_a, offspring_b, fitness_a, fitness_b
        else:
            return offspring_b, offspring_a, fitness_b, fitness_a


    def adjustPopulation(self, offspring_a, offspring_b):
        """[Changes two least fit individuals with the newly 
            formed offspring]
        
        Arguments:
            offspring_a {list]} -- [chromossome of offspring a]
            offspring_b {[list]} -- [chromossome of offspring b]
        
        Returns:
            [list] -- [population]
        """        
        
        print(f'fitness before change: {self.fitness}')  
        
        least_fit = min(self.fitness)
        index_least_fit = self.fitness.index(least_fit)
        self.fitness[index_least_fit] = 2
        
        second_least_fit = min(self.fitness)
        index_second_least_fit = self.fitness.index(second_least_fit)
        self.fitness[index_least_fit] = least_fit
        
        self.population[index_least_fit], self.population[index_second_least_fit], \
            self.fitness[index_least_fit], self.fitness[index_second_least_fit] = \
                self.fittestOffspring(offspring_a, offspring_b)
        
        print(f'fitness after change: {self.fitness}\n')  

        return self.population
    
    
    def generateOffspring(self):
        """[Main function loop:
            - selects best parents
            - do crossover operation
            - sometimes mutates genes
            - substitute 2 worst individuals
            
            Until an individual achieves maximum fitness or
            the number of iterations is achived]
        
        Returns:
            [string] -- [Informs best generation and its mean or if a fittest individual is found
                         informs the generation and the fitness scores of each individual]
        """        
        i = 1
        fittest_found = False
        sum_best_solution = 0
        best_solution = []
        best_generation = 0
        
        while i < self.n_iter + 1:
            parent_a, parent_b = self.selection()
            offspring_a, offspring_b = self.crossover(parent_a, parent_b)
            
            if random.randint(1, 10) <= self.mutation_prob:
                print('Mutation!')
                offspring_a, offspring_b = self.mutation(offspring_a, offspring_b)
            
            self.adjustPopulation(offspring_a, offspring_b)
            
            if 1.0 in self.fitness and i > 1:
                best_generation = i
                fittest_found = True
                break
            
            print(f'\nGENERATION -> [{i}], FITTEST -> [{max(self.fitness)}], MEAN -> [{round(statistics.mean(self.fitness), 2)}]\n')
            i += 1
            
            if sum(self.fitness) > sum_best_solution:
                sum_best_solution = sum(self.fitness[:])
                best_solution = self.fitness[:]
                best_generation = i
            
            
        if fittest_found == True:
            return f'Fittest Individual found on generation: [{best_generation - 1}] | {self.fitness}'
        else:
            return f'Best Generation: [{best_generation - 1}] | Mean Individuals fitness: [{round(statistics.mean(best_solution), 2)}]'
        
                       
gen = SimpleGeneticAlgorithm(pop_size=5, num_genes=5, n_iter=50, mutation_prob=2)
print(gen.generateOffspring())