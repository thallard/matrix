import sys

sys.path.append('../')

from Classes.Matrix import Matrix

if __name__ == '__main__':
    print('\033[35mDeterminant on matrices (subject)\033[0m')
    # m1 = Matrix([[1, -1], [-1, 1]])
    # print(m1.determinant())

    m1 = Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
    print(m1.determinant())

    m1 = Matrix([[1, 0, 5], [2, 1, 6], [3, 4, 0]])
    print(m1.determinant())

    m1 = Matrix([[8, 5, -2, 4], [4, 2.5, 20, 4], [8, 5, 1, 4], [28, -4, 17, 1]])
    print(m1.determinant())

    print('\033[35mDeterminant on matrices (correction)\033[0m')
    m1 = Matrix([[0, 0], [0, 0]])
    print(m1.determinant())

    m1 = Matrix([[1, 0], [0, 1]])
    print(m1.determinant())

    m1 = Matrix([[2, 0], [0, 2]])
    print(m1.determinant())

    m1 = Matrix([[1, 1], [1, 1]])
    print(m1.determinant())

    m1 = Matrix([[0, 1], [1, 0]])
    print(m1.determinant())

    m1 = Matrix([[1, 2], [3, 4]])
    print(m1.determinant())

    m1 = Matrix([[-7, 5], [4, 6]])
    print(m1.determinant())

    m1 = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]])
    print(m1.determinant())

