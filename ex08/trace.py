import sys

sys.path.append('../')

from Classes.Matrix import Matrix

if __name__ == '__main__':
    print('\033[35mTrace with matrices (subject)\033[0m')
    v1 = Matrix([[1, 0], [0, 1]])
    print(v1.trace())

    v1 = Matrix([[2, -5, 0], [4, 3, 7], [-2, 3, 4]])
    print(v1.trace())

    v1 = Matrix([[-2, -8, 4], [1, -23, 4], [0, 6, 4]])
    print(v1.trace())

    print('\033[35mTrace with matrices (correction)\033[0m')
    v1 = Matrix([[0, 0], [0, 0]])
    print(v1.trace())

    v1 = Matrix([[1, 0], [0, 1]])
    print(v1.trace())

    v1 = Matrix([[1, 2], [3, 4]])
    print(v1.trace())

    v1 = Matrix([[8, -7], [4, 2]])
    print(v1.trace())

    v1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print(v1.trace())