import sys

class Vector(object):
    # Constructor
    def __init__(self, array):
        self.vector = []

        # Fill the vector
        for i in range(len(array)):
            self.vector.append(array[i])

    # Debug function to print all values from Vector object
    def print(self):
        for i in range(len(self.vector)):
            if i == len(self.vector) - 1:
                print(self.vector[i])
            else:
                print(self.vector[i], end=', ')
        print()

    # Return a 1D array with shape [rows, columns]
    def shape(self):
        if isinstance(self.vector[0], (float, int)):
            return [len(self.vector), 1]
        return [len(self.vector), len(self.vector[0])]

    # Return a boolean if the Vector is a square
    def is_square(self):
        length = len(self.vector)

    # Add a vector with the current vector
    def add(self, vector):
        for i in range(len(vector)):
            if len(self.vector) == len(vector):
                self.vector[i] += vector[i]
            else:
                print('\033[31mAdd error : Invalid size between two matrices\033[0m')
                return

    # Sub a matrix with the current vector
    def sub(self, vector):
        for i in range(len(vector)):
            if len(self.vector) == len(vector):
                self.vector[i] -= vector[i]
            else:
                print('\033[31mAdd error : Invalid size between two matrices\033[0m')
                return

    # Multiply a matrix with a scalar
    def scl(self, scalar):
        for i in range(len(self.vector)):
            self.vector[i] *= scalar

    # Linear interpolation with a scalar
    def lerp(self, target, interpolation):
        vector_lerp = []
        if len(self.vector) != len(target.vector):
            return None

        for i in range(len(self.vector)):
            vector_lerp.append((target.vector[i] - self.vector[i]) * interpolation + self.vector[i])
        return vector_lerp

    # Dot product
    def dot(self, factor):
        if self.shape() != factor.shape():
            return None

        if self.vector == factor.vector:
            return self.vector[0]

        value = 0
        for i in range(len(self.vector)):
            value += self.vector[i] * factor.vector[i]
        return value

    # Norm using Manhattan distance
    def norm_1(self):
        norm = 0.0
        for i in range(len(self.vector)):
            norm += abs(self.vector[i])
        return round(norm ** 0.5, 5)

    # Euclidean norm
    def norm(self):
        norm = 0.0
        for i in range(len(self.vector)):
            norm += self.vector[i] ** 2
        return round(norm ** 0.5, 5)

    # Infinite norm using Chebyshev distance
    def norm_inf(self):
        value = -sys.maxsize

        for i in range(len(self.vector)):
            if value < self.vector[i]:
                value = self.vector[i]
        return round(value, 5)

    # Cross product
    def cross_product(self, vector):
        if self.shape()[0] != 3 or len(vector) != 3:
            return None

        cross_product = [self.vector[1] * vector[2] - self.vector[2] * vector[1],
                         self.vector[2] * vector[0] - self.vector[0] * vector[2],
                         self.vector[0] * vector[1] - self.vector[1] * vector[0]]
        return cross_product


