
############
class prog:
    def __init__(self, scheme, coefficient):
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

        self.scheme = scheme
        self.coef = coefficient

    def make_calculation(self):
        for i in range(self.scheme)
