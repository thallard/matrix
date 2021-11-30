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
