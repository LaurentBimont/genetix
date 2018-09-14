import SuperClass as sc
import numpy as np
import pandas as pd

class Prog:
    '''scheme is defined as followed

    Parameters
    -----------
    scheme :
        An array defined by the succession of Operand terms and
        pseudo_const terms
        ex : [Pseudo Constant, Operand, Pseudo Constant, Pseudo Constant, Operand, Pseudo Constant]
             [u_n-1, ^, n, 5, *, u_n-3]
        by default the operand between two adjacents Structure is addition
    coefficient :
        An array linked which each terms representing the multiplicative
        coefficient of the Structure term
        ex : [4,2,5,1]

    -----------
    The two previous examples give the following progression :
    u_n = 4 * u_n-1^(2*n)+ 5*5 * 1*u_n-3
    '''

    def __init__(self, scheme, true, start):
        '''
        scheme is the scheme
        true is the true values of the progression
        start is the indice where we can start calculating the serie
        '''
        self.scheme = scheme
        self.true = true
        self.coef_name_list = 'abcdefghijklmnopqrstuvwxyz'           # Coefficients are named thanks to a letter
        self.generate_progression()
        self.start = start

    def operand_graph(self, typ, a, b):
        if typ == '+':
            return(sc.Addition(a,b))
        elif typ == '*':
            return(sc.Multiplication(a,b))
        elif typ == '^':
            return(sc.Puissance(a,b))

    def generate_progression(self):
        '''
        Generate the ultimate variable from the structure proposed in scheme.
        as a reminder, operations terms are represented by strings : '*', '+', '^'
        Computational ordering is handle thanks to a queue list
        '''

        increment = 0
        new_queue, old_queue = [], []                           # New queue
        temp_scheme = self.scheme[:]
        for i in range(0,len(self.scheme),2):
            old_queue.append(sc.Multiplication(self.scheme[i], sc.Coefficient(self.coef_name_list[increment])))
            del temp_scheme[i-increment]
            increment += 1
        self.nb_coef = increment - 1
        self.scheme = temp_scheme[:]
        while len(self.scheme) != 0:
            increment = 0
            for i in range(0,len(self.scheme),2):
                new_queue.append(self.operand_graph(self.scheme[i-increment], old_queue[i], old_queue[i+1]))
                del self.scheme[i-increment]
                increment += 1
            new_queue, old_queue = [], new_queue
        self.ultimate = old_queue[0]

    def generate_graph(self, coef):
        '''
        Set up the graph from the ultimate variable previously computed

        coef : Initial coefficients vector to start the graph with
        '''
        self.graph = sc.Graph(self.true, self.start)                                 #
        self.graph.set_default_graph()
        self.dict_coef = {}
        for i in range(len(coef)):
            self.dict_coef[self.coef_name_list[i]] = coef[i]
        self.set_up_df()

    def set_up_df(self):
        '''
        Initiliaze a panda DataFrame with one column containing true values
        '''
        pandas_dict = {'true':self.true}
        self.df = pd.DataFrame(data = pandas_dict)

    def compute_apply(self, row):
        self.graph.n = row.name
        if row.name < self.start:
            return(row['true'])
        return(self.graph.value(self.ultimate, dict = self.dict_coef))

    def difference(self,row):
        return(abs(int(row['compute']) - int(row['true'])))

    def fitness(self):
        new_df = self.df.copy(deep=True)
        new_df['compute'] = new_df.apply(self.compute_apply, axis = 1)
        new_df['difference'] = new_df.apply(self.difference, axis = 1)       #valeur absolu de la difference
        return(new_df['difference'].sum())

    def update_coef(self, coef):
        self.dict_coef = {}
        for i in range(len(coef)):
            self.dict_coef[self.coef_name_list[i]] = coef[i]

if __name__ == '__main__':

    test = Prog([sc.Constant(2), '+', sc.Term(1), '+', sc.Nconstant(1), '+', sc.Term(1)], [1,3,5,6,5,4,2,5,8,5,6,5,2,5],2)
    test.generate_graph([1,1,1,1])
    print()
    print(test.fitness())
    test.update_coef([2,2,2,2])
    print(test.fitness())
    #print(test.generate_progression().value(G, dict = {'fal':3}))
