import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

def dot_product(vector_one, vector_two):
    if len(vector_one) != len(vector_two):
        print('Inputs should have equal dimensions')
        return None

    prod = 0
    for i in range(len(vector_one)):
        prod += vector_one[i]*vector_two[i]

    return prod

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        det = 0
                
        if self.h==1:
            det = 1/self.g[0][0]
        else:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
        if a*d==c*b:
            raise ValueError('Matrix has no inverse')
        else:
            det = 1/((a*d)-(b*c))
        
        return det
    

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        sum_major_diag = 0
        for i in range(0, len(self.g)):
            sum_major_diag += self.g[i][i]
        
        return sum_major_diag

    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        inv = []
        
        if self.h==1:
            inv.append([1/self.g[0][0]])
        else:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
        
            inv = [[d, -b], [-c, a]]
            
            for i in range(0,len(inv)):
                for j in range(0, len(inv[0])):
                    inv[i][j] = inv[i][j] * self.determinant()
    
        return Matrix(inv)
    

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        matrix_transpose = []
        for j in range(0, self.w):
            row = []
            for i in range(0, self.h):
                row.append(self.g[i][j])
            matrix_transpose.append(row)
        
        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w


    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 

        sum_mat = []
        
        for i in range(0, len(self.g)):
            row = []
            for j in range(0, len(self.g[0])):
                row.append(self.g[i][j] + other[i][j])
            sum_mat.append(row)
            
        return Matrix(sum_mat)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)
        """
        return -1*self
    

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        return self + (-other)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        if self.w != other.h:
            print('Number of columns of Matrix A should be equal to number of rows in Matrix B.')
            return 
    
        product = []

        trans_B = other.T()

        for i in range(0, self.h):
            row = []
            for j in range(0, trans_B.h):
                row.append(dot_product(self.g[i],trans_B.g[j]))

            product.append(row)

        return Matrix(product)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.
        """
        if isinstance(other, numbers.Number):
            pass
            prod = []
        
            for i in range(0, len(self.g)):
                row = []
                for j in range(0, len(self.g[0])):
                    row.append(self.g[i][j] * other)
                prod.append(row)
            
        return Matrix(prod)
            