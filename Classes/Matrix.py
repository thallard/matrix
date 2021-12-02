class Matrix(object):
    # Constructor
    def __init__(self, array):
        self.matrix = []

        # One column gestion and populate matrix
        if isinstance(array[0], (int, float)):
            for i in range(len(array)):
                self.matrix.append(array[i])
            return

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

    # Return a 1D array with shape [rows, columns]
    def shape(self):
        return [len(self.matrix), len(self.matrix[0])]

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

    # Linear interpolation with scalar
    def lerp(self, target, interpolation):
        matrix_lerp = []

        # Gestion for one column
        if isinstance(target.matrix[0], (int, float)) and isinstance(self.matrix[0], (int, float)):
            for i in range(len(self.matrix)):
                matrix_lerp.append((target.matrix[i] - self.matrix[i]) * interpolation + self.matrix[i])
            return matrix_lerp

        # Compare shape of matrixes
        if self.shape() != target.shape():
            return None

        # Gestion for multiples columns
        for i in range(len(self.matrix)):
            values = []
            for j in range(len(self.matrix[i])):
                values.append((target.matrix[j][i] - self.matrix[j][i]) * interpolation + self.matrix[j][i])
            matrix_lerp.append(values)
        return matrix_lerp

    # Matrix multiplication with a vector
    def mul_vec(self, vector):
        new_vector = []

        for i in range(len(self.matrix)):
            value = 0
            for j in range(len(self.matrix[i])):
                value += self.matrix[i][j] * vector[j]
            new_vector.append(value)
        return new_vector

    # Matrix multiplication with a matrix
    def mul_mat(self, matrix):
        new_matrix = []

        for row in range(len(self.matrix)):
            temp = []
            for column in range(len(self.matrix[row])):
                value = 0
                for i in range(len(self.matrix[row])):
                    value += self.matrix[row][i] * matrix[i][column]
                temp.append(value)
            new_matrix.append(temp)
        return new_matrix
