class Matrix(object):
    # Constructor
    def __init__(self, array):
        self.matrix = []

        # Check numbers of columns of each row
        for i in range(len(array)):
            if len(array[0]) != len(array[i]):
                print('\033[31mConstructor error : Invalid size input\033[0m')
                return

        # Fill the matrix
        for i in range(len(array)):
            self.matrix.append(array[i])

    # Debug function to print all values from Matrix object
    def print(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if j == len(self.matrix[i]) - 1:
                    print(self.matrix[i][j])
                else:
                    print(self.matrix[i][j], end=', ')
        print()

    # Return a 1D array with size
    def size(self):
        return 1

    # Return a boolean if the Matrix is a square
    def is_square(self):
        length = len(self.matrix)

    # Add a matrix with the current matrix
    def add(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(self.matrix[i]) == len(matrix[i]):
                    self.matrix[i][j] += matrix[i][j]
                else:
                    print('\033[31mAdd error : Invalid size between two matrices\033[0m')
                    return

    # Sub a matrix with the current matrix
    def sub(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(self.matrix[i]) == len(matrix[i]):
                    self.matrix[i][j] -= matrix[i][j]
                else:
                    print('\033[31mAdd error : Invalid size between two matrices\033[0m')
                    return

    # Multiply a matrix with a scalar
    def scl(self, scalar):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] *= scalar
