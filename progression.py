import numpy as np

class prog:
    def __init__(self, scheme, coefficient):
        '''scheme is defined as followed

        Parameters
        -----------
        scheme :
            An array defined by the succession of Operand terms and
            Structure terms
            ex : [Structure, Operand, Structure, Operand, Structure]
                 [u_n-1, ^, n, +, 5, *, u_n-3]

        coefficient :
            An array linked which each terms representing the multiplicative
            coefficient of the Structure term
            ex : [4,2,5,1]

        -----------
        The two previous examples give the following progression :
        u_n = 4 * u_n-1^(2*n)+ 5*5 * 1*u_n-3
         '''

        self.scheme = scheme
        self.coef = coefficient

    def make_calculation(self):
        for i in range(self.scheme)
