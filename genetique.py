# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 18:18:13 2017

@author: Utilisateur
"""
import numpy as np
from random import randint
from random import random

terme = [1, 1, 1]           #forme a un+2 + b un+1 + c un = 0
vrai_suite = np.array([1, 1, 2, 3, 5, 8, 13, 21, 34])

class genetix:
    def __init__(self, vrai_suite, nb_generation, nb_individu, nb_genes, maxi, mutation_rate, nb_selectionne):
        self.vrai_suite = vrai_suite
        self.nb_generation = nb_generation
        self. nb_individu =  nb_individu
        self.nb_genes = nb_genes
        self.generation_en_cours = 1
        self.maxi = maxi
        self.mutation_rate =mutation_rate
        self.nb_selectionne = nb_selectionne
        self.generation = np.array([[randint(1,maxi) for j in range(nb_genes)] for i in range(nb_individu) ])
        print(self.generation)
        self.new_generation = np.array([[0.0 for j in range(nb_genes)] for i in range(nb_individu) ])
        self.proba = 0
        self.result = 0
    
    def fitness(self, terme):
        test_suite = np.zeros(self.vrai_suite.shape[0])
        test_suite[0], test_suite[1] = terme[0], terme[1]
        assert(terme[0] != 0)
        for i in range(2, len(vrai_suite)):
            test_suite[i] = -(terme[1]*test_suite[i-1] + terme[2]*test_suite[i-2])/terme[0]
        return(np.sum(np.square(test_suite - vrai_suite)))/1000
        
    def find_proba(self):
        self.result = []
        for i in range(self.nb_individu):
            self.result.append((self.fitness(self.generation[i]), int(i)))
        self.result = sorted(self.result, key=lambda fitness: fitness[0]) 
        print(self.result)
        intermediate = np.array([1/(self.result[i][0]) for i in range(self.nb_selectionne)])
        print(intermediate)
        self.proba = np.exp(intermediate) / np.sum(np.exp(intermediate), axis=0)
        print(self.proba)
        
    def choose_proba(self, p):
        seuil = 0
        selectionnne = self.result[:self.nb_selectionne]
        print(selectionnne)
        
        for i in range(self.nb_selectionne):
            
            seuil += self.proba[i]
            if p < seuil:
                return(self.result[i][1])
        return(self.result[0][1])
        
    def New_generation(self):
        for i in range(self.nb_individu):
            for j in range(self.nb_genes):
                p = random()
                indice = self.choose_proba(p)
                m = random()
                if m < self.mutation_rate:
                    self.new_generation[i][j] = randint(1, self.maxi)
                else:
                    self.new_generation[i][j] = self.generation[indice][j]
        self.generation = np.copy(self.new_generation)
        self.new_generation = np.array([[0.0 for j in range(self.nb_genes)] for i in range(self.nb_individu) ])
    
    def principal(self):
        for j in range(self.nb_generation):
            self.find_proba()
            self.New_generation()
            self.generation_en_cours += 1
        
test = genetix(vrai_suite, 10, 10, 3, 10, 0.2, 3)  #vrai_suite, nb_generation, nb_individu, nb_genes, maxi, mutation_rate, nb_selectionne
test.principal()
#for i in range(test.nb_individu):
#    test.result.append((test.fitness(test.generation[i]), int(i)))
#print(test.result)

def fitness(terme, vrai_suite):
    test_suite = np.zeros(vrai_suite.shape[0])
    test_suite[0], test_suite[1] = terme[0], terme[1]
    assert(terme[0] != 0)
    for i in range(2, len(vrai_suite)):
        test_suite[i] = (terme[1]*test_suite[i-1] + terme[2]*test_suite[i-2])/terme[0]
    return(np.sum(np.square(test_suite - vrai_suite)))

