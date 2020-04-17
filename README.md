# Genetic Algorithm
- - - -
### Initial Population

	* Each individual is a possible solution to a problem you want to solve, the individuals are characterised by a set of parameters, that are called genes, these genes ( generally defined by a bit ) are merged into a string to form a Chromosome, that is the solution to the problem
	[ 1 0 1 0 (1) -> { Gene } 1 1 0 1 ] -> Chromosome
- - - -

### Fitness Function

	* Determines how fit the individual is, giving it a fitness score  that determines the probability for an individual to be chosen for reproduction 
	
- - - -

### Selection

	* Select the fittest individuals and let them pass their genes to the next generation, the individuals are selected based on their fitness score
	
- - - -

### Crossover 

	* One of the most important parts in the genetic algorithm, it chooses a random point, called the crossover point in the chromosome
	
	[ 0 0 0 1 | -> (Crossover Point) 1 1 ] -> Parent A
	[ 1 0 1 1 |  0 0 ] -> Parent B

	* The parents will exchange their genes until the crossover point is reached
	
	[ 0 0 0 1 | 1 0 ] -> Child A
	[ 1 0 1 1 | 1 1 ] -> Child B
- - - -

### Mutation

	* Some children may have mutations ( with a low probability ) and some of the bits can be flipped, it is done to maintain the diversity in the population, preventing bias and premature convergence
