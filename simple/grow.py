import numpy as np
import matplotlib.pyplot as plt

def growth_rate(population, space):
    """
    Returns number of population increment in then ext cycle.
    growth rate is based on population and space
    Higher space left -> higher growth rate
    Higher population -> higher growth rate
    
    When space approaches 0, growth rate approaches 0 too.
    growth_rate never exceeds space.
    When there's plenty of space, the space term should disappear.
    """
    population_coeff = 10000 # >0 larger means grow slower usually take 10xtotal space
    space_coeff = 1
    rate = space_coeff * space * (1-np.exp(-population/population_coeff))
    rate = np.minimum(space, rate)
    print('growth rate: ', rate)
    return rate

def next_state(population, space):
    """
    calculates the next population and space based on current
    population and space left
    """

    unit_size = 1 # space that one unit of population takes
    new_population = growth_rate(population, space)
    return (population + new_population, space - new_population * unit_size)
    
if __name__ == '__main__':
    initial_population = 1
    initial_space = 1000
    cycle = 0
    pop = [initial_population]
    space = [initial_space]
    cyc = [cycle]
    while cycle < 100 and space[-1] > 0:
        print('cycle: ', cycle)
        cycle += 1
        cyc.append(cycle)
        next_pop, next_space = next_state(pop[-1], space[-1])
        pop.append(next_pop)
        space.append(next_space)
    plt.subplot(211)
    plt.plot(cyc, pop, 'r--', cyc, space, 'bs')
    plt.show()
