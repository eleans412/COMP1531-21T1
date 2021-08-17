
class Matrix:
    def __init__(self, m, n):
        """Initialises (with zeros) a matrix of dimensions m by n."""
        self.matrix = []
        while len(self.matrix) < m:
            M.append([])
            while len(self.matrix[-1]) < n:
                self.matrix[-1].append(0.0)
        return self.matrix


    def __str__(self):
        """Returns a string representation of this matrix as integers in the form:
          a b c
          d e f
          g h i
        Used as follows: s = str(m1)
        """

        # Convert each element into string
        string = [[str(element) for element in sub] for sub in self.matrix]

        return string

    def get(self, key):
        """Returns the (i,j)th entry of the matrix, where key is the tuple (i, j)

        Used as follows: x = matrix.get((0,0))
        * raises IndexError if (i,j) is out of bounds
        """
        k_is_true = False
        v_is_true = False
        k_location = 0
        v_location = 0
        result = ()

        for k, v in key:
            for i in range(len(self.matrix)):
                if matrix[i][j] == k:
                    k_is_true = True
                    k_location = i
                for h in range(len(self.matrix)):
                    if matrix[i][j] == v:
                        v_is_true = True
                        v_location = j

        if k_is_true == True and v_is_true == True:
            result.append((k_locationm v_location))
        return result

    def set(self, key, data):
        """Sets the (i,j)th entry of the matrix, where key is the tuple (i, j)

        and data is the number being added.
        Used as follows: matrix.set((0,0), 1)
        * raises IndexError if (i,j) is out of bounds
        * raises TypeError if data is not an integer
        """

        k_is_true = False
        v_is_true = False
        k_location = 0
        v_location = 0
        

        for k, v in key:
            for i in range(len(self.matrix)):
                if matrix[i][j] == k:
                    k_is_true = True
                    k_location = i
                for h in range(len(self.matrix)):
                    if matrix[i][j] == v:
                        v_is_true = True
                        v_location = j

        if k_is_true == True and v_is_true == True:
            self.matrix(k_locationm v_location)) = data

        return self.matrix

    def zeros_matrix(m,n):
        '''
        Creates a matrix filled with zeros
        '''

        M = []
        while len(M) < m:
            M.append([])
            while len(M[-1]) < n:
                M[-1].append(0.0)
        return M

    def add(self, other):
        """Adds self to another Matrix or integer, returning a new Matrix.

        This method should not modify the current matrix or other.
        Used as follows: m1.add(m2) => m1 + m2
        or: m1.add(3) => m1 + 3
        * raises TypeError if other is not a Matrix object or an integer
        * raises ValueError if the other Matrix does not have the same dimensions
        """
        # If an integer or not matrix raise Error
        if not isinstance(other, self):
            raise TypeError('Not a matrix/Is an integer, cannot be added')


        # Add matrix with matrix
        rowsA = len(self)
        colsA = len(self[0])
        rowsB = len(other)
        colsB = len(other[0])

        if rowsA != rowsB or colsA != colsB:
            raise ValueError('Matrices are not the same size')

        C = zeros_matrix(rowsA, colsB)

        for i in range(rowsA):
            for j in range(colsB):
                C[i][j] = A[i][j] + B[i][j]
        return C


    def mul(self, other):
        """Multiplies self with another Matrix or integer, returning a new Matrix.

        This method should not modify the current matrix or other.
        Used as follows: m1.mul(m2) m1 x m2 (matrix multiplication, not point-wise)
        or: m1.mul(3) => m1*3
        * raises TypeError if the other is not a Matrix object or an integer
        * raises ValueError if the other Matrix has incorrect dimensions
        """

        rowsA = len(self)
        colsA = len(self[0])
        rowsB = len(other)
        cols(B) = len(other[0])

        result = 
        # Scalar multiplication
        if isinstance(other, int):
            for i in  rowsA:
                for j in colsA:
                    C[i] += other * self[i][j]

        # If an integer or not matrix raise Error
        if not isinstance(other, self):
            raise TypeError('Not a matrix/Is an integer, cannot be added')
        
        # Matrix multiplication
        

        if colsA != rowsB:
            raise ValueError('Incorrect dimensions')

        C = zeros_matrix(rowsA, colsB)

        for i in range(rowsA):
            for j in range(colsB):
                total = 0
                for count in range(colsA):
                    total += A[i][count] * B[count][j]
                C[i][j] = total
        
        
        return C

