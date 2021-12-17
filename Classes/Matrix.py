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
                sys.exit(1)

        # Populate matrix for multiples columns
        for i in range(len(array)):
            row = []
            for j in range(len(array[i])):
                row.append(array[i][j])
            self.matrix.append(row)

    # Debug function to print all values from Matrix object
    def print(self, condition=True):
        for i in range(len(self.matrix)):
            print(self.matrix[i])
        if condition:
            print()

    # Return a 1D array with shape [rows, columns]
    def shape(self):
        return [len(self.matrix), len(self.matrix[0])]

    # Return a boolean if the Matrix is a square
    def is_square(self):
        if len(self.matrix[0]) == len(self.matrix):
            return True
        return False

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
                temp.append(self.matrix[i][j])
            save.append(temp)
        self.matrix = save
        return self.matrix

    # Row echelon form using Gaussian elimination
    def row_echelon(self):
        # Clone my matrix
        matrix = []
        for i in range(len(self.matrix)):
            line = []
            for j in range(len(self.matrix[i])):
                line.append(self.matrix[i][j])
            matrix.append(line)

        lead = 0
        for row in range(len(self.matrix)):
            if len(self.matrix[0]) <= lead:
                return matrix
            i = row
            while matrix[i][lead] == 0:
                i += 1
                if len(self.matrix) == i:
                    i = row
                    lead += 1
                    if len(self.matrix[0]) == lead:
                        return matrix
            # Swap lines i with row
            matrix[i], matrix[row] = matrix[row], matrix[i]
            pivot = matrix[row][lead]
            matrix[row] = [m / float(pivot) for m in matrix[row]]

            # Cancel each line by multiplying it with the lead
            for i in range(len(self.matrix)):
                if i != row:
                    pivot = matrix[i][lead]
                    matrix[i] = [i_matrix - pivot * row_matrix for row_matrix, i_matrix in zip(matrix[row], matrix[i])]
            lead += 1
        return matrix

    # Private recursive function for determinant
    def __det(self, matrix, size, final_matrix, scalar):
        if size == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        elif size >= 3:
            determinant = 0
            for column in range(size):
                new = []
                for row in range(1, size):
                    line = []
                    for i in range(size):
                        if i != column:
                            line.append(matrix[row][i])
                    new.append(line)
                value = matrix[0][column] * self.__det(new, size - 1, final_matrix, scalar)

                # Add or substrate depends on column
                if column % 2 == 1:
                    value = -value
                determinant += value
            return determinant

    # Public function with return determinant of a square matrice
    def determinant(self):
        matrix = []

        # Check if the matrice given is a square
        if not self.is_square():
            return 0

        # Clone the matrice
        for i in range(len(self.matrix)):
            matrix.append(self.matrix[i])
        return self.__det(matrix, len(matrix), [], False)

    # Return inverse of the given matrice
    def inverse(self):
        matrix = []

        # Clone the given matrice
        for i in range(len(self.matrix)):
            line = []
            for j in range(len(self.matrix[i])):
                line.append(self.matrix[i][j])
            matrix.append(line)

        # Check if the matrice is singular
        if self.determinant() == 0:
            print('\033[33mThe given matrice is singular.\033[0m')
            return 0














