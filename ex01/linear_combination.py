import sys

sys.path.append('../')

from Classes.Vector import Vector
from Classes.Matrix import Matrix


# Special case
def linear_combination(arrays, scalars):
    combination_result = []

    # Simple matrix or vector gestion
    if isinstance(arrays, (Matrix, Vector)):
        if isinstance(arrays, Matrix):
            matrix = arrays.matrix
            modified_matrix = []

            # Check input size
            for i in range(len(matrix)):
                if len(matrix[i]) != len(matrix[0]) or len(scalars) != len(matrix[0]):
                    return None

            # Linear combination matrice
            for i in range(len(matrix)):
                value = 0
                for j in range(len(scalars)):
                    if j >= len(matrix):
                        value += matrix[i][len(matrix[i]) - 1] * scalars[j]
                    else:
                        value += matrix[i][j] * scalars[j]
                modified_matrix.append(value)
            return modified_matrix
        elif isinstance(arrays, Vector):
            vector = arrays.vector
            modified_vectors = []

            if isinstance(vector[0], (int, float)):
                for i in range(len(vector)):
                    value = 0
                    for j in range(len(scalars)):
                        value += vector[i] * scalars[j]
                    modified_vectors.append(value)
                return modified_vectors

                # Check size input
            for i in range(len(vector)):
                if len(vector[i]) != len(vector[0]) or len(scalars) != len(vector):
                    return None

            # Linear combination vector
            for i in range(len(vector[0])):
                value = 0
                for j in range(len(scalars)):
                    value += vector[j][i] * scalars[j]
                modified_vectors.append(value)
            return modified_vectors
    # Complex gestion list of matrices
    elif isinstance(arrays, list):
        for l in range(len(scalars)):
            matrix = []
            for i in range(len(arrays[l])):
                temp = []
                for j in range(len(arrays[l][i])):
                    temp.append(arrays[l][i][j] * scalars[l])
                matrix.append(temp)
            combination_result.append(matrix)

        final_matrix = Matrix(combination_result[0])
        for i in range(1, len(scalars)):
            final_matrix.add(combination_result[i])
        return final_matrix.matrix


if __name__ == '__main__':
    print('\033[34mVector part (linear combination)\033[0m')
    v1 = Vector([-42, 42])
    print(linear_combination(v1, [-1]))

    v1 = Vector([[-42], [-42], [-42]])
    print(linear_combination(v1, [-1, 1, 0]))

    v1 = Vector([[-42, 42], [1, 3], [10, 20]])
    print(linear_combination(v1, [1, -10, -1]))

    v1 = Vector([[-42, 100, -69.5], [1, 3, 5]])
    print(linear_combination(v1, [1, -10]))

    print('\033[34mMatrix part (linear combination)\033[0m')

    m1 = Matrix([-42, 42])
    print(linear_combination(m1, [-1]))

    m1 = Matrix([[-42], [-42], [-42]])
    print(linear_combination(m1, [-1, 1, 0]))

    m1 = Matrix([[-42, 42], [420, -420]])
    m2 = Matrix([[1, 3], [2, 4]])
    m3 = Matrix([[10, 20], [30, 40]])
    matrices = [m1.matrix, m2.matrix, m3.matrix]
    print(linear_combination(matrices, [1, -10, -1]))
