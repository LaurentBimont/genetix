import numpy as np

############ Operand Super Class ################
class Operand:
    '''
    Three types of operations that are going to be compute within a computational graph in order to speed up and ease the calculation of the progression.
    '''
    def __init__(self, inputs=[]):
        self.inputs = inputs
        self.ouput = []

    def compute(self):
        pass

class Puissance(Operand):
    def __init__(self, a, n):
        super().__init__([a,n])

    def compute(self):
        return(self.inputs[0]**self.inputs[1])

class Addition(Operand):
    def __init__(self, a, b):
        super().__init__([a,b])

    def compute(self):
        return(self.inputs[0]+self.inputs[1])

class Multiplication(Operand):
    def __init__(self, a, b):
        super().__init__([a,b])

    def compute(self):
        return(self.inputs[0]*self.inputs[1])

############ Structure Super Class ##################
class PseudoConst:
    '''Differents types of constant, some need to know at wich n we are, output a value at this step'''
    def __init__(self):
        self.output_value = None


    def return_value(self):
        pass

class Constant(PseudoConst):
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
        return(_default_graph.y_true[_default_graph.n - self.a])
########### Graph ###############
class Graph:
    def __init__(self, y_true, n):
        self.y_true = y_true
        self.n = n
        self.output = []

    def set_default_graph(self):
        global _default_graph
        _default_graph = self

g = Graph([1,3,5,8,45,20], 5)
g.set_default_graph()
A = Term(2)
print(A.return_value())
