import sys

sys.path.append('../')

from Classes.Matrix import Matrix

if __name__ == '__main__':
    v1 = Matrix([[1, 0], [0, 1]])
    print(v1.trace())

    v1 = Matrix([[2, -5, 0], [4, 3, 7], [-2, 3, 4]])
    print(v1.trace())

    v1 = Matrix([[-2, -8, 4], [1, -23, 4], [0, 6, 4]])
    print(v1.trace())