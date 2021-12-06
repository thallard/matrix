import sys


# Verify content provided in matrices
def is_valid(array):
    # One row gestion
    if isinstance(array[0], (int, float)):
        for i in range(len(array)):
            if not isinstance(array[i], (int, float)):
                print('\033[31mIncorrect value given (' + str(array[i]) + ').\033[0m')
                sys.exit(1)
        return 1
    elif not isinstance(array[0], list):
        print('\033[31mIncorrect type given.\033[0m')
        sys.exit(1)

    # Multiples rows gestion
    for i in range(len(array)):
        for j in range(len(array[i])):
            if not isinstance(array[i][j], (int, float)):
                print('\033[31mIncorrect value given (' + str(array[i]) + ').\033[0m')
                sys.exit(1)


class Matrix(object):
    # Constructor
    def __init__(self, array):
        # Verify content of array
        is_valid(array)
        self.matrix = []

        # One column gestion and populate matrix
        if isinstance(array[0], (int, float)):
            for i in range(len(array)):
                self.matrix.append([array[i]])
            return

        # Check if matrice given is valid
        for i in range(len(array)):
            if len(array[0]) != len(array[i]):
                print('\033[31mConstructor error : Invalid size input\033[0m')
                return

        # Populate matrix for multiples columns
        for i in range(len(array[0])):
            row = []
            for j in range(len(array)):
                row.append(array[j][i])
            self.matrix.append(row)

    # Debug function to print all values from Matrix object
    def print(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])
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

    # Apply vector values with a scalar
    def linear_combination(self, scalars):
        modified_matrix = []

        # Check size input
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(self.matrix[0]) or len(scalars) != len(self.matrix):
                return None

        # print(len(self.matrix))
        # Linear combination
        for i in range(len(self.matrix)):
            value = 0
            for j in range(len(scalars)):
                if j >= len(self.matrix[i]):
                    value += self.matrix[i][len(self.matrix[i]) - 1] * scalars[j]
                else:
                    value += self.matrix[i][j] * scalars[j]
            modified_matrix.append(value)
        return modified_matrix

    # Linear interpolation with scalar
    def lerp(self, target, interpolation):
        matrix_lerp = []

        # Gestion for one column
        # if isinstance(target.matrix[0], (int, float)) and isinstance(self.matrix[0], (int, float)):
        #     for i in range(len(self.matrix)):
        #         matrix_lerp.append((target.matrix[i] - self.matrix[i]) * interpolation + self.matrix[i])
        #     return matrix_lerp

        # Compare shape of matrixes
        if self.shape() != target.shape():
            return None

        # Gestion for multiples columns
        for i in range(len(self.matrix)):
            values = []
            for j in range(len(self.matrix[i])):
                values.append((target.matrix[i][j] - self.matrix[i][j]) * interpolation + self.matrix[i][j])
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

    # Matrix trace
    def trace(self):
        # Check if it's a square
        if self.shape()[0] != self.shape()[1]:
            return None

        tr = 0
        for i in range(len(self.matrix)):
            tr += self.matrix[i][i]
        return tr

    # Transpose matrix
    def transpose(self):
        if self.shape()[1] == 1:
            return None
        save = []
        for i in range(len(self.matrix)):
            temp = []
            for j in range(len(self.matrix[i])):
                temp.append(self.matrix[j][i])
            save.append(temp)
        self.matrix = save
        return self.matrix

    # Row echelon form using Gaussian elimination
    def row_echelon(self):
        row_echelon_matrix = []

        return row_echelon_matrix
