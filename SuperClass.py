'''
This class is made to compute efficiently a graph that represents a progression, It allows to change fastly the different coefficients.
It also offers the flexibility needed by a genetic algorithm to try different scheme and to find new ones.
'''


import numpy as np
import pandas as pd
############ Operand Super Class ################
class Operand:
    '''
    Three types of operations that are going to be compute within a computational graph in order to speed up and ease the calculation of the progression.
    '''
    def __init__(self, inputs=[]):
        self.input_nodes = inputs
        self.ouput = []

    def compute(self):
        pass

class Puissance(Operand):
    def __init__(self, a, n):
        super().__init__([a,n])


    def compute(self, x_var, n_var):
        self.inputs = [x_var, n_var]
        return(self.inputs[0]**self.inputs[1])

class Addition(Operand):
    def __init__(self, a, b):
        super().__init__([a,b])

    def compute(self, a_var, b_var):
        self.inputs = [a_var, b_var]
        return(self.inputs[0]+self.inputs[1])

class Multiplication(Operand):
    def __init__(self, a, b):
        super().__init__([a,b])

    def compute(self, a_var, b_var):
        self.inputs = [a_var, b_var]
        return(self.inputs[0]*self.inputs[1])

############ Pseudo Constant Class ##################
class PseudoConst:
    '''Differents types of constant, some need to know at wich n we are, output a value at this step'''
    def __init__(self):
        self.output = None

    def return_value(self):
        pass

class Constant(PseudoConst): #Regler pour navoir que 1 comme constante possible (le coefficient se chargera du reste)
    '''a is a constant real'''
    def __init__(self, a):
        super().__init__()
        self.a = a

    def return_value(self):
        return(self.a)

class Nconstant(PseudoConst):
    '''
    The returned value will be n + a
    a is a real
    '''
    def __init__(self, a):
        super().__init__()
        self.a = a

    def return_value(self):
        return(_default_graph.n + self.a)

class Term(PseudoConst):
    '''
    the output value will be u_n-a
    a is a positive integer
    '''
    def __init__(self, a):
        super().__init__()
        self.a = a

    def return_value(self):
        if _default_graph.n - self.a >= 0:
            return(_default_graph.y_true[_default_graph.n - self.a])
        else:
            print('increase the starting number, can not compute U_n-',self.a,' because first value is for n = ',_default_graph.n)
            return(0)

############ Coefficient Class ##################
class Coefficient:
    def __init__(self, name):
        self.output = None
        self.name = name

########### Graph ###############
class Graph:
    def __init__(self, y_true, n):
        '''
        y_true : true progrssion
        n : rank at which we are, useful to compute n-1 ou u_n-1
        '''
        self.y_true = y_true
        self.n = n
        self.output = None

    def set_default_graph(self):
        global _default_graph
        _default_graph = self

    def value(self, node, dict):
        #assert isinstance(node, Operand):
        order_of_operations = self.compute_graph_structure(node)
        for op in order_of_operations:
            if isinstance(op, Coefficient):
                op.output = dict[op.name]
            elif isinstance(op, PseudoConst):
                op.output = op.return_value()
            elif isinstance(op, Operand):
                op.inputs = [input_node.output for input_node in op.input_nodes]
                op.output = op.compute(*op.inputs)
        return(node.output)

    def compute_graph_structure(self, operand):
        ''''''
        nodes_postorder = []
        def recurse(node):
            if isinstance(node, Operand):
                for input_node in node.input_nodes:
                    recurse(input_node)
            nodes_postorder.append(node)
        recurse(operand)
        return nodes_postorder

if __name__ == '__main__':
    prog = [0]
    for i in range(1,1000):
        prog.append(2*prog[-1] + i**2)

    print(prog[:5])
    g = Graph(prog, 4)
    g.set_default_graph()
    Te = Coefficient('fal')
    Z = Constant(1)
    A = Multiplication(Te, Z)
    B = Term(1)
    C = Nconstant(0)
    D = Constant(2)
    E = Multiplication(A, B)
    F = Puissance(C,D)
    G = Addition(E,F)
    test = [0]

    print(g.value(G, dict = {'fal':3}))
