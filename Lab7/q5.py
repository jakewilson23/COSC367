"""Write a function roulette_wheel_select(population, fitness, r) that takes a list of individuals, a fitness
function, and a floating-point random number r in the interval [0, 1), and selects and returns an individual from the
population using the roulette wheel selection mechanism. The fitness function (which will be provided as an argument)
takes an individual and returns a non-negative number as its fitness. The higher the fitness the better. When
constructing the roulette wheel, do not change the order of individuals in the population."""


def roulette_wheel_select(population, fitness, r):
    sum_fitness = 0
    running_total = 0
    value_list = []
    for pop in population:
        sum_fitness += fitness(pop)
    for individual in population:
        if sum_fitness == 0:
            calculation = 0
        else:
            calculation = fitness(individual) / sum_fitness
        running_total += calculation
        value_list.append((individual, running_total))
    for value in value_list:
        if value[1] >= r:
            return value[0]


def main():
    # Test 1
    population = ['a', 'b']

    def fitness(x):
        return 1  # everyone has the same fitness

    for r in [0, 0.33, 0.49999, 0.51, 0.75, 0.99999]:
        print(roulette_wheel_select(population, fitness, r))

    # Test 2
    population = [0, 1, 2]

    def fitness(x):
        return x

    for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
        print(roulette_wheel_select(population, fitness, r))


if __name__ == "__main__":
    main()
