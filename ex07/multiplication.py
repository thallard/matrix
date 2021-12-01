import sys

sys.path.append('../')

from Classes.Vector import Vector
from Classes.Matrix import Matrix


if __name__ == '__main__':
    print('\033[35mMultiplication matrix with vector\033[0m')
    m1 = Matrix([[1, 0], [0, 1]])
    v1 = Vector([4, 2])
    print(m1.mul_vec(v1.vector))

    m1 = Matrix([[2, 0], [0, 2]])
    v1 = Vector([4, 2])
    print(m1.mul_vec(v1.vector))

    m1 = Matrix([[2, -2], [-2, 2]])
    v1 = Vector([4, 2])
    print(m1.mul_vec(v1.vector))

    print('\033[35mMultiplication vector with vector\033[0m')
    m1 = Matrix([[1, 0], [0, 1]])
    m2 = Matrix([[1, 0], [0, 1]])
    print(m1.mul_mat(m2.matrix))

    m1 = Matrix([[1, 0], [0, 1]])
    m2 = Matrix([[2, 1], [4, 2]])
    print(m1.mul_mat(m2.matrix))

    m1 = Matrix([[3, -5], [6, 8]])
    m2 = Matrix([[2, 1], [4, 2]])
    print(m1.mul_mat(m2.matrix))
