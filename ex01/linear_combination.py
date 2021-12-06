import sys

sys.path.append('../')

from Classes.Vector import Vector
from Classes.Matrix import Matrix

# Apply vector values with a scalar
def linear_combination(vectors, scalars):
    modified_vectors = []

    # One row vector gestion
    if isinstance(vectors[0], (int, float)):
        for i in range(len(vectors)):
            value = 0
            for j in range(len(scalars)):
                value += vectors[i] * scalars[j]
            modified_vectors.append(value)
        return modified_vectors

    # Check size input
    for i in range(len(vectors)):
        if len(vectors[i]) != len(vectors[0]) or len(scalars) != len(vectors):
            return None

    # Linear combination
    for i in range(len(vectors[0])):
        value = 0
        for j in range(len(scalars)):
            value += vectors[j][i] * scalars[j]
        modified_vectors.append(value)
    return modified_vectors


if __name__ == '__main__':
    print('\033[34mVector part (linear combination)\033[0m')
    vector1 = Vector([-42, 42])
    print(vector1.linear_combination([-1]))

    v1 = Vector([[-42], [-42], [-42]])
    print(v1.linear_combination([-1, 1, 0]))

    v1 = Vector([[-42, 42], [1, 3], [10, 20]])
    print(v1.linear_combination([1, -10, -1]))

    v1 = Vector([[-42, 100, -69.5], [1, 3, 5]])
    print(v1.linear_combination([1, -10]))

    print('\033[34mMatrix part (linear combination)\033[0m')

    m1 = Matrix([-42, 42])
    print(m1.linear_combination([-1]))

    m1 = Matrix([[-42], [-42], [-42]])
    print(m1.linear_combination([-1, 1, 0]))

