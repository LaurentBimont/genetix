import SuperClass as sc
import progression as pg
import numpy as np
import pandas as pd

class genetique:
    '''
    Generic genetic algorithm
    '''
    def __init__(self):
        self.a = 'Hello World'

class fitness_coefficientt(genetique):
    '''
    Special function for coefficient genetic computation
    '''
    def __init__(self):
        self.a = 'Hello World'

        

class fitness_structure(genetique):
    '''
    Special function for structure computation
    '''
    def __init__(self):
        self.a = 'Hello World'

if __name__ == '__main__':
    # Environnement de test pour la fitness_coefficient
    test = pg.prog([sc.Term(1), '+', sc.Term(2)], [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025])
