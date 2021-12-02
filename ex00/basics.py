import sys

sys.path.append('../')

from Classes.Matrix import Matrix
from Classes.Vector import Vector

if __name__ == '__main__':
    print('\033[32mMatrix part (row)\033[0m')
    matrix1 = Matrix([[1, 1, 1], [1, 1, 1]])
    matrix2 = Matrix([[1, 1, 1], [1, 1, 1]])

    # Invalid constructor
    matrix3 = Matrix([[1, 1, 1], [1, 1]])

    # Print
    matrix1.print()

    # Add
    matrix1.add(matrix2.matrix)
    matrix1.print()

    # Sub
    matrix1.sub(matrix2.matrix)
    matrix1.print()

    # Multiplication with scalar
    matrix1.scl(10)
    matrix1.print()

    print('\033[32mVector part\033[0m')
    vector1 = Vector([1, 1, 1])
    vector2 = Vector([1, 1, 1])

    # Print
    vector1.print()

    # Add
    vector1.add(vector2.vector)
    vector1.print()

    # Sub
    vector1.sub(vector2.vector)
    vector1.print()

    # Multiplication with scalar
    vector1.scl(10)
    vector1.print()
