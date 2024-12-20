import random

def create_population(pop_size, gene_length):
    return [[random.randint(0, 1) for _ in range(gene_length)] for _ in range(pop_size)]

def fitness(individual):
    return sum(individual)

def select(population):
    population.sort(key=fitness, reverse=True)
    return population[:len(population)//2]

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(individual, mutation_rate):
    return [gene if random.random() > mutation_rate else 1 - gene for gene in individual]

def genetic_algorithm(pop_size, gene_length, generations, mutation_rate):
    population = create_population(pop_size, gene_length)
    for _ in range(generations):
        selected = select(population)
        next_generation = []
        while len(next_generation) < pop_size:
            parent1, parent2 = random.choice(selected), random.choice(selected)
            child1, child2 = crossover(parent1, parent2)
            next_generation.append(mutate(child1, mutation_rate))
            next_generation.append(mutate(child2, mutation_rate))
        population = next_generation
    return max(population, key=fitness)

pop_size = 100
gene_length = 10
generations = 100
mutation_rate = 0.01

best_individual = genetic_algorithm(pop_size, gene_length, generations, mutation_rate)
print(best_individual)
