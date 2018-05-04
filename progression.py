import SuperClass as sc
import numpy as np

class prog:
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

    def __init__(self, scheme, coefficient):
        self.scheme = scheme
        self.coef = coefficient

    def operand_graph(self, typ, a, b):
        if typ == '+':
            return(sc.Addition(a,b))
        elif typ == '*':
            return(sc.Multiplication(a,b))
        elif typ == '^':
            return(sc.Puissance(a,b))

    def generate_graph(self):
        '''
        Generate a graph from the structure proposed in scheme.
        as a reminder, operations terms are represented by strings : '*', '+', '^'
        Computational ordering is handle thanks to a queue list
        '''
        coef_name_list = 'abcdefghijklmnopqrstuvwxyz'
        increment = 0
        new_queue, old_queue = [], []
        temp_scheme = self.scheme[:]
        for i in range(0,len(self.scheme),2):
            print(i)
            old_queue.append(sc.Multiplication(self.scheme[i], sc.Coefficient(coef_name_list[increment])))
            del temp_scheme[i]
            increment += 1
        self.scheme = temp_scheme[:]
        while len(self.scheme) != 0:
            increment = 0
            for i in range(0,len(self.scheme),2):
                new_queue.append(self.operand_graph(self.scheme[i], old_queue[i], old_queue[i+1]))
                del self.scheme[i-increment]
                increment += 1


if __name__ == '__main__':

    test = prog([sc.Constant(2), '+', sc.Term(1), '^', sc.Nconstant(1), '*', sc.Term(5)], [])
    test.generate_graph()
