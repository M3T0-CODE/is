import random

POP_SIZE = 10
GENOME_SIZE = 5
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.7
NUM_GENERATIONS = 50


def fitness_function(x):
    return x ** 2


def initialize_population(pop_size, genome_size):
    population = []
    for _ in range(pop_size):
        genome = ''.join(random.choice('01') for _ in range(genome_size))
        population.append(genome)
    return population


def binary_to_decimal(binary_genome):
    return int(binary_genome, 2)


def select(population, fitness_values):
    tournament_size = 3
    tournament = random.sample(list(zip(population, fitness_values)), tournament_size)
    tournament.sort(key=lambda x: x[1], reverse=True)
    return tournament[0][0]


def crossover(parent1, parent2):
    if random.random() > CROSSOVER_RATE:
        return parent1, parent2
    crossover_point = random.randint(1, len(parent1) - 1)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2


def mutate(genome):
    if random.random() < MUTATION_RATE:
        mutation_point = random.randint(0, len(genome) - 1)
        mutated_genome = list(genome)
        mutated_genome[mutation_point] = '1' if mutated_genome[mutation_point] == '0' else '0'
        return ''.join(mutated_genome)
    return genome


def genetic_algorithm():
    population = initialize_population(POP_SIZE, GENOME_SIZE)

    for generation in range(NUM_GENERATIONS):
        fitness_values = [fitness_function(binary_to_decimal(genome)) for genome in population]

        next_generation = []

        while len(next_generation) < POP_SIZE:
            parent1 = select(population, fitness_values)
            parent2 = select(population, fitness_values)

            offspring1, offspring2 = crossover(parent1, parent2)
            next_generation.append(mutate(offspring1))
            if len(next_generation) < POP_SIZE:
                next_generation.append(mutate(offspring2))

        population = next_generation
        max_fitness = max(fitness_values)
        print(f"Generation {generation + 1}: Max Fitness = {max_fitness}")

    final_fitness_values = [fitness_function(binary_to_decimal(genome)) for genome in population]
    best_genome = population[final_fitness_values.index(max(final_fitness_values))]
    best_solution = binary_to_decimal(best_genome)
    print(f"\nBest solution: {best_solution}, Fitness = {max(final_fitness_values)}")


genetic_algorithm()
