import SuperClass as sc
import progression as pg
import numpy as np
import pandas as pd
from random import randint

class genetique:
    '''
    Generic genetic algorithm
    '''
    def __init__(self, structure, mutation, upper_limit, population_size):
        self.a = 'Hello World'
        self.population
        self.mutation = mutation
        self.structure = structure
        self.upper_limit = upper_limit
        self.gene_size = len((self.structure.scheme + 1) / 2)
        self.population_size = population_size




class fitness_coefficient(genetique):
    '''
    Special function for coefficient genetic computation
    '''
    def __init__(self,):
        self.a = 'Hello World'

    def generate_first_population(self):
        '''
        Initialize population
        '''
        self.population = [[randint(-10,10) for i in range(self.gene_size)]for j in range(self.population_size)]

    def fitness_function(self):
        

    def fitness(self):
        '''
        Calculate fitness of a population
        Return a list with fitness of each gene
        '''
        result = []
        for i in range(len(self.population)):
            result.append(self.fitness_function(self.population))
        return(result)

    def optimize(self):
        '''
        update population to find the best one
        '''
        self.generate_first_population()

        i = 0
        while i < self.upper_limit:
            fitness = self.fitness()

            i += 1


class fitness_structure(genetique):
    '''
    Special function for structure computation
    '''
    def __init__(self):
        self.a = 'Hello World'

if __name__ == '__main__':
    # Environnement de test pour la fitness_coefficient
    fibonaci_structure = pg.Prog([sc.Term(1), '+', sc.Term(2)], [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025])
    test_coef = fitness_coefficient(fibonaci_structure, 500)
    test_coef.optimize()
    test_coef.print_population
